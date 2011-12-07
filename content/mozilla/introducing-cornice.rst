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
            request.errors.add('body', 'awesome', 'You lack awesomeness!')


    @service.get(validator=(is_awesome))
    def get1(request):
        return {"test": "succeeded"}


All the errors collected during the validation process, or after, are collected
before returning the request. If any, a error 400 is fired up, with the list of
problems encoutred encoded as a nice json list (we plan to support multiple
formats in the future)

As you might have seen, `request.errors.add` takes three parameters: **location**,
**name** and **description**.

**location** is where the error arised. It can either be "body", "query", "headers"
or "path". **name** is the name of the variable causing problem, if any, and
**description** contains a more detailled message.

Here is an example of a malformed request::

    $ # run a demo app

To describe a web service in *cornice*, you have to write something like this

.. code-block:: python
    
