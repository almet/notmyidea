# Cheese & code - Wrap-up


This week-end I hosted a *cheese & code* session in the country-side of
Angers, France.

We were a bunch of python hackers and it rained a lot, wich forced us to
stay inside and to code. Bad.

We were not enough to get rid of all the cheese and the awesome meals,
but well, we finally managed it pretty well.

Here is a summary of what we worked on:

## Daybed

Daybed started some time ago, and intend to be a replacement to google
forms, in term of features, but backed as a REST web service, in python,
and open source.

In case you wonder, daybed is effectively the name of a couch. We chose
this name because of the similarities (in the sound) with **db**, and
because we're using **CouchDB** as a backend.

![Daybed is a big couch\!](/images/daybed.jpg)

We mainly hacked on daybed and are pretty close to the release of the
first version, meaning that we have something working.

[The code](http://github.com/spiral-project/daybed) is available on
github, and we also wrote [a small
documentation](http://daybed.rtfd.org) for it.

Mainly, we did a lot of cleanup, rewrote a bunch of tests so that it
would be easier to continue to work on the project, and implemented some
minor features. I'm pretty confidend that we now have really good basis
for this project.

Also, we will have a nice todolist application, with the backend **and**
the frontend, in javascript / html / css, you'll know more when it'll be
ready :-)

Once we have something good enough, we'll release the first version and
I'll host it somewhere so that people can play with it.

## Cornice

Daybed is built on top of [Cornice](http://cornice.rtfd.org), a
framework to ease the creation of web-services.

At Pycon France, we had the opportunity to attend a good presentation
about [SPORE](https://github.com/SPORE/specifications). SPORE is a way
to describe your REST web services, as WSDL is for WS-\* services. This
allows to ease the creation of generic SPORE clients, which are able to
consume any REST API with a SPORE endpoint.

Here is how you can let cornice describe your web service for you

```python

from cornice.ext.spore import generate_spore_description
from cornice.service import Service, get_services

spore = Service('spore', path='/spore', renderer='jsonp')
@spore.get
def get_spore(request):
    services = get_services()
    return generate_spore_description(services, 'Service name',
                                      request.application_url, '1.0')
```

And you'll get a definition of your service, in SPORE, available at
/spore.

Of course, you can use it to do other things, like generating the file
locally and exporting it wherever it makes sense to you, etc.

I released today [Cornice 0.11](http://crate.io/packages/cornice/),
which adds into other things the support for SPORE, plus some other
fixes we found on our way.

## Respire

Once you have the description of the service, you can do generic clients
consuming them\!

We first wanted to contribute to [spyre](https://github.com/bl0b/spyre)
but it was written in a way that wasn't supporting to POST data, and
they were using their own stack to handle HTTP. A lot of code that
already exists in other libraries.

While waiting the train with [Rémy](http://natim.ionyse.com/), we hacked
something together, named "Respire", a thin layer on top of the awesome
[Requests](http://python-requests.org) library.

We have a first version, feel free to have a look at it and provide
enhancements if you feel like it. We're still hacking on it so it may
break (for the better), but that had been working pretty well for us so
far.

You can [find the project on
github](http://github.com/spiral-project/respire), but here is how to
use it, really quickly (these examples are how to interact with daybed)

```python

>>> from respire import client_from_url

>>> # create the client from the SPORE definition
>>> cl = client_from_url('http://localhost:8000/spore')

>>> # in daybed, create a new definition
>>> todo_def = {
...    "title": "todo",
...    "description": "A list of my stuff to do",
...    "fields": [
...        {
...            "name": "item",
...            "type": "string",
...            "description": "The item"
...        },
...        {
...            "name": "status",
...            "type": "enum",
...            "choices": [
...                "done",
...                "todo"
...            ],
...            "description": "is it done or not"
...        }
...    ]}
>>> cl.put_definition(model_name='todo', data=todo_def)
>>> cl.post_data(model_name='todo', data=dict(item='make it work', status='todo'))
{u'id': u'9f2c90c0529a442cfdc03c191b022cf7'}
>>> cl.get_data(model_name='todo')
```

Finally, we were out of cheese so everyone headed back to their
respective houses and cities.

Until next time?
