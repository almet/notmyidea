API description using cornice and colander
##########################################

:status: draft

One of the goals we want to accomplish with Cornice is to describe the web
services in a nice and easy way, for the developer. This for different reasons.

Having web services described in some ways allows you do do interesting things,
such as automatically generating a documentation, or a client, for instance.
REST services are supposed to be discoverable, but in a lot of situations,
that's not the case, and it can be a pain to implement a client for them, even
if most of what is being done there is shared between a lot of web services.

In cornice, we already generate some documentation, but this one is incomplete in
different ways. For instance, it is currently not possible to get information
about the inputs you are waiting for, in the different locations (body,
headers and query string).

For instance, if you want to describe that a *POST* on `/foobar` needs the
*foo* and *bar* parameters, and that you eventually could add a *baz*
parameter, you can't, or you have to describe it manually in the documentation
of the web service.

Cornice, while not tied to `Colander`_, tries to make a good use of it when
possible. So it is possible to do validation of the incoming data (in different
locations) and, at the same time, documentation of the web service.

To do so, you have to use a particular `schema` keyword in the decorator. Here
is an example of definition

.. code-block:: python

    from cornice import Service
    from colander import MappingSchema, SchemaNode, String

    foobar = Service(name="foobar", path="/foobar")


    class Foobar(MappingSchema):
        foo = SchemaNode(String(), location="body")
        bar = SchemaNode(String(), location="headers")
        baz = SchemaNode(String(), default=None)


    @foobar.get(scheme=Foobar)
    def foobar_get(request):
        # do something here

.. _Colander: http://docs.pylonsproject.org/projects/colander/en/latest/

The output documentation currently looks like this:

.. image:: images/cornice-exampledoc-validation.png

The plans for the future are to be able to put direct curl calls in the
documentation to demonstrate how the service behaves for instance, and why not
creating a tiny python client able to consume the cornice APIs.
