Introducing cornice
###################

:date: 06/12/2011

Wow, already my third working day at mozilla. Since Monday, I've been working with
Tarek Ziadé, on a pyramid REST-ish toolkit named `cornice <https://github.com/mozilla-services/cornice>`_.

Its goal is to take all the hard bits appart from you when implementing a web
service, so you can focus on what's important. Cornice provides you facilities
for validation of any kind.

The goal is to simplify your work, but we don't want to reinvent the wheel, so
it is easily pluggable with validations frameworks, such as Collander.

Handling errors and validation
==============================

We have changed the way errors are handled. Here is how it works:

.. code-block:: python

    service = Service(name="service", path="/service")


    def is_awesome(request):
        if not 'awesome' in request.GET:
            request.errors.add('body', 'awesome',
                                'the awesome parameter is required')


    @service.get(validator=is_awesome)
    def get1(request):
        return {"test": "yay!"}


All the errors collected during the validation process, or after, are collected
before returning the request. If any, a error 400 is fired up, with the list of
problems encoutred encoded as a nice json list (we plan to support multiple
formats in the future)

As you might have seen, `request.errors.add` takes three parameters: **location**,
**name** and **description**.

**location** is where the error arised. It can either be "body", "query", "headers"
or "path". **name** is the name of the variable causing problem, if any, and
**description** contains a more detailled message.

Let's run this simple service, with `bin/paster serve` and send some queries to
it::

    $ curl -v http://127.0.0.1:5000/service
    > GET /service HTTP/1.1
    > Host: 127.0.0.1:5000
    > Accept: */*
    >
    * HTTP 1.0, assume close after body
    < HTTP/1.0 400 Bad Request
    < Content-Type: application/json; charset=UTF-8
    [{"location": "body", "name": "awesome", "description": "You lack awesomeness!"}

I've removed the extra clutter from the curl's output, but you got the general idea.

The content returned is in JSON, and I know exactly what I have to do: add an
"awesome" parameter in my query. Let's do it again::

    $ curl http://127.0.0.1:5000/service?awesome=yeah
    {"test": "yay!"}

Validators can also attach extra information about validations to the request, 
using `request.validated`. It is a standard dict automatically attached to the 
requests. 

For instance, in our validator, we can chose to validate the parameter passed
and use it in the body of the webservice:

.. code-block:: python

    service = Service(name="service", path="/service")


    def is_awesome(request):
        if not 'awesome' in request.GET:
            request.errors.add('body', 'awesome',
                                'the awesome parameter is required')
        else:
            request.validated['awesome'] = 'awesome ' + request.GET['awesome']


    @service.get(validator=is_awesome)
    def get1(request):
        return {"test": request.validated['awesome']}
    
::

    curl http://127.0.0.1:5000/service?awesome=yeah
    {"test": "awesome yeah"}

     

Dealing with "Accept" headers
=============================

The HTTP spec defines a **Accept** header the client can send so the response
is encoded the right way. A resource, available at an URL, can be available in
different formats. This is especially true for web services.

Cornice can help you to deal with this. The services you define can tell which
content-types they can deal with, and this will be checked against the
**Accept** headers sent by the client.

Let's refine a bit our previous example, by specifying which content-types are
supported, using the `accept` parameter:

.. code-block:: python

    @service.get(validator=is_awesome, accept=("application/json", "text/json"))
    def get1(request):
        return {"test": "yay!"}

Now, if you specifically ask for XML, for instance, cornice will throw a 406
with the list of accepted content-types::

    $ curl -vH "Accept: application/xml" http://127.0.0.1:5000/service
    > GET /service HTTP/1.1
    > Host: 127.0.0.1:5000
    > Accept: application/xml
    > 
    < HTTP/1.0 406 Not Acceptable
    < Content-Type: application/json; charset=UTF-8
    < Content-Length: 33
    < 
    ["application/json", "text/json"]


Building your documentation automatically
=========================================

XXX
