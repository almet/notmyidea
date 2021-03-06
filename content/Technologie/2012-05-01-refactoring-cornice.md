# Refactoring Cornice

After working for a while with [Cornice](http://cornice.readthedocs.com)
to define our APIs at [Services](http://docs.services.mozilla.com), it
turned out that the current implementation wasn't flexible enough to
allow us to do what we wanted to do.

Cornice started as a toolkit on top of the
[pyramid](http://docs.pylonsproject.org/en/latest/docs/pyramid.html)
routing system, allowing to register services in a simpler way. Then we
added some niceties such as the ability to automatically generate the
services documentation or returning the correct HTTP headers [as defined
by the HTTP
specification](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)
without the need from the developer to deal with them nor to know them.

If you're not familiar with Cornice, here is how you define a simple
service with it:

```python

from cornice.service import Service
bar = Service(path="/bar")

@bar.get(validators=validators, accept='application/json')
def get_drink(request):
    # do something with the request (with moderation).
```

This external API is quite cool, as it allows to do a bunch of things
quite easily. For instance, we've written our
[token-server](https://github.com/mozilla-services/tokenserver) code on
top of this in a blast.

## The burden

The problem with this was that we were mixing internally the service
description logic with the route registration one. The way we were doing
this was via an extensive use of decorators internally.

The API of the cornice.service.Service class was as following
(simplified so you can get the gist of it).

```python

class Service(object):

    def __init__(self, **service_kwargs):
        # some information, such as the colander schemas (for validation),
        # the defined methods that had been registered for this service and
        # some other things were registered as instance variables.
        self.schemas = service_kwargs.get(schema', None)
        self.defined_methods = []
        self.definitions = []

    def api(self, **view_kwargs):
        """This method is a decorator that is being used by some alias
        methods.
        """
        def wrapper(view):
            # all the logic goes here. And when I mean all the logic, I
            # mean it.
            # 1. we are registering a callback to the pyramid routing
            #    system so it gets called whenever the module using the
            #    decorator is used.
            # 2. we are transforming the passed arguments so they conform
            #    to what is expected by the pyramid routing system.
            # 3. We are storing some of the passed arguments into the
            #    object so we can retrieve them later on.
            # 4. Also, we are transforming the passed view before
            #    registering it in the pyramid routing system so that it
            #    can do what Cornice wants it to do (checking some rules,
            #    applying validators and filters etc.
        return wrapper

    def get(self, **kwargs):
        """A shortcut of the api decorator"""
        return self.api(request_method="GET", **kwargs)
```

I encourage you to go read [the entire
file](https://github.com/mozilla-services/cornice/blob/4e0392a2ae137b6a11690459bcafd7325e86fa9e/cornice/service.py#L44).
on github so you can get a better opinion on how all of this was done.

A bunch of things are wrong:

  - first, we are not separating the description logic from the
    registration one. This causes problems when we need to access the
    parameters passed to the service, because the parameters you get are
    not exactly the ones you passed but the ones that the pyramid
    routing system is expecting. For instance, if you want to get the
    view get\_drink, you will instead get a decorator which contains
    this view.
  - second, we are using decorators as APIs we expose. Even if
    decorators are good as shortcuts, they shouldn't be the default way
    to deal with an API. A good example of this is [how the resource
    module consumes this
    API](https://github.com/mozilla-services/cornice/blob/4e0392a2ae137b6a11690459bcafd7325e86fa9e/cornice/resource.py#L56).
    This is quite hard to follow.
  - Third, in the api method, a bunch of things are done regarding
    inheritance of parameters that are passed to the service or to its
    decorator methods. This leaves you with a really hard to follow path
    when it comes to add new parameters to your API.

## How do we improve this?

Python is great because it allows you to refactor things in an easy way.
What I did isn't breaking our APIs, but make things way simpler to
hack-on. One example is that it allowed me to add features that we
wanted to bring to Cornice really quickly (a matter of minutes), without
touching the API that much.

Here is the gist of the new architecture:

```python

class Service(object):
    # we define class-level variables that will be the default values for
    # this service. This makes things more extensible than it was before.
    renderer = 'simplejson'
    default_validators = DEFAULT_VALIDATORS
    default_filters = DEFAULT_FILTERS

    # we also have some class-level parameters that are useful to know
    # which parameters are supposed to be lists (and so converted as such)
    # or which are mandatory.
    mandatory_arguments = ('renderer',)
    list_arguments = ('validators', 'filters')

    def __init__(self, name, path, description=None, **kw):
        # setup name, path and description as instance variables
        self.name = name
        self.path = path
        self.description = description

        # convert the arguments passed to something we want to store
        # and then store them as attributes of the instance (because they
        # were passed to the constructor
        self.arguments = self.get_arguments(kw)
        for key, value in self.arguments.items():
            setattr(self, key, value)

        # we keep having the defined_methods tuple and the list of
        # definitions that are done for this service
        self.defined_methods = []
        self.definitions = []

    def get_arguments(self, conf=None):
        """Returns a dict of arguments. It does all the conversions for
        you, and uses the information that were defined at the instance
        level as fallbacks.
        """

    def add_view(self, method, view, **kwargs):
        """Add a view to this service."""
        # this is really simple and looks a lot like this
        method = method.upper()
        self.definitions.append((method, view, args))
        if method not in self.defined_methods:
            self.defined_methods.append(method)

    def decorator(self, method, **kwargs):
    """This is only another interface to the add_view method, exposing a
    decorator interface"""
        def wrapper(view):
            self.add_view(method, view, **kwargs)
            return view
        return wrapper
```

So, the service is now only storing the information that's passed to it
and nothing more. No more route registration logic goes here. Instead, I
added this as another feature, even in a different module. The function
is named register\_service\_views and has the following signature:

```python

register_service_views(config, service)
```

To sum up, here are the changes I made:

1.  Service description is now separated from the route registration.
2.  cornice.service.Service now provides a hook\_view method, which is
    not a decorator. decorators are still present but they are optional
    (you don't need to use them if you don't want to).
3.  Everything has been decoupled as much as possible, meaning that you
    really can use the Service class as a container of information about
    the services you are describing. This is especially useful when
    generating documentation.

As a result, it is now possible to use Cornice with other frameworks. It
means that you can stick with the service description but plug any other
framework on top of it. cornice.services.Service is now only a
description tool. To register routes, one would need to read the
information contained into this service and inject the right parameters
into their preferred routing system.

However, no integration with other frameworks is done at the moment even
if the design allows it.

The same way, the sphinx description layer is now only a consumer of
this service description tool: it looks at what's described and build-up
the documentation from it.

The resulting branch is not merged yet. Still, you can [have a look at
it](https://github.com/mozilla-services/cornice/tree/refactor-the-world).

Any suggestions are of course welcome :-)
