PyPI on CouchDB
###############

By now, there are two ways to retrieve data from PyPI (the Python Package
Index). You can both rely on xml/rpc or on the "simple" API. The simple
API is not so simple to use as the name suggest, and have several existing
drawbacks.

Basically, if you want to use informations coming from the simple API, you will
have to parse web pages manually, to extract informations using some black
vodoo magic. Badly, magic have a price, and it's sometimes impossible to get
exactly the informations you want to get from this index. That's the technique
currently being used by distutils2, setuptools and pip.

On the other side, while XML/RPC is working fine, it's requiring extra work
to the python servers each time you request something, which can lead to
some outages from time to time. Also, it's important to point out that, even if
PyPI have a mirroring infrastructure, it's only for the so-called *simple* API,
and not for the XML/RPC.

CouchDB
=======

Here comes CouchDB. CouchDB is a document oriented database, that
knows how to speak REST and JSON. It's easy to use, and provides out of the box
a replication mechanism.

So, what ?
==========

Hmm, I'm sure you got it. I've wrote a piece of software to link informations from
PyPI to a CouchDB instance. Then you can replicate all the PyPI index with only
one HTTP request on the CouchDB server. You can also access the informations
from the index directly using a REST API, speaking json. Handy.

So PyPIonCouch is using the PyPI XML/RPC API to get data from PyPI, and
generate records in the CouchDB instance.

The final goal is to avoid to rely on this "simple" API, and rely on a REST
insterface instead. I have set up a couchdb server on my server, which is
available at http://couchdb.notmyidea.org/_utils/pypi/. There is not a lot to
see there for now, but I've done the first import from PyPI yesterday and all
went fine: it's possible to access the metadata of all PyPI projects via a REST
interface. Next step is to write a client for this REST interface in
distutils2.

Example
=======

For now, you can use pypioncouch via the command line, or via the python API.

Using the command line
----------------------

You can do something like that for a full import. This **will** take long,
because it's fetching all the projects at pypi and importing their metadata::

    $ pypioncouch --fullimport http://your.couchdb.instance/
    
If you already have the data on your couchdb instance, you can just update it
with the last informations from pypi. **However, I recommend to just replicate
the principal node, hosted at http://couchdb.notmyidea.org/pypi/**, to avoid
the duplication of nodes::

    $ pypioncouch --update http://your.couchdb.instance/

The principal node is updated once a day by now, I'll try to see if it's
enough, and ajust with the time.

Using the python API
--------------------

You can also use the python API to interact with pypioncouch::

    >>> from pypioncouch import XmlRpcImporter, import_all, update
    >>> full_import()
    >>> update()

What's next ?
=============

I want to make a couchapp, in order to navigate PyPI easily. Here are some of
the features I want to propose:

* List all the available projects
* List all the projects, filtered by specifiers
* List all the projects by author/maintainer
* List all the projects by keywords
* Page for each project.
* Provide a PyPI "Simple" API equivalent, even if I want to replace it, I do
  think it will be really easy to setup mirrors that way, with the out of the
  box couchdb replication

I also still need to polish the import mechanism, so I can directly store in
couchdb:

* The OPML files for each project
* The upload_time as couchdb friendly format (list of int)
* The tags as lists (currently it's only a string separated by spaces

The work I've done by now is available on
https://bitbucket.org/ametaireau/pypioncouch/. Keep in mind that it's still
a work in progress, and everything can break at any time. However, any feedback
will be appreciated !
