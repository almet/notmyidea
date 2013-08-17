Understanding Zamboni
#####################

:status: draft

Behind the `firefox marketplace <http://marketplace.firefox.com>`_ and
`AMO <http://addons.mozilla.com>`_ is a big giant codebase, named Zamboni (you
know, this big machine that goes and clean the playground after hockey games).

I've been working on it since quite some time now, and I'm still a bit scared
about it, because it contains code that's useful for both the marketplace and
AMO.

Since it's open-source, I think we can probably make it more useful to other
teams with different usecases, but the reality is that currently it's kinda
hard to understand what it's doing, and how.

So here is an attemp of introduction to this codebase; It's also useful to me
because I'm sure I'll understand more things about it all by doing this
description post.

File Structure
==============

The first thing I like to look at is the file structure.
In our case, we have something like this::

    apps
    mkt

    lib

    configs
    default
    docs
    locale
    media
    migrations
    requirements
    scripts
    services
    sites
    templates
    vendor
    wsgi

Yes, that's a bunch of folders. And each of them contains python packages and
modules :-)

Django applications
-------------------

The framework behind all this is the django framework. And it uses the concept
of "applications" to separate the concerns.

`apps` contains applications used by AMO, `mkt` is the code of the marketplace.

`mkt` is dependent on `apps`, but that's not true the other way around.

In apps:

* **abuse** contains some django models definitions and a helper to register
  abuse on apps or users.
* **access** contains some utilities to manage ACLs.

In mkt:

* 

Libraries
---------

Some of the code is not directly tied to django, and shouldn't; that's what we
call libraries. It's something different from the external libraries we depend
on; these are tied to the business we are in. In there, you can find the
following bits at the time of writing:

* **crypto** takes care of the app-signing and receipt-signing logic. You want
  to use it for instance to sign an app (it generates a manifest and signature,
  and deal with the exchanges that have to be done with the signing server).
* **es**, XXX what is this doing? It seems related to django, a kind of cache?

* **geoip** is taking care of calling the geoip server to turn IP adresses into
  geographic information.

* **licences** contains the texts of different licences with an utility tool to
  return their texts.
* **metrics** contains the logic that sends metric information to the different
  systems (currently monolith and our internal hbase cluster)
* **pay_server** is a client for the pay_server.
* **product_json** contains json values; I'm not sure used for what. XXX
* **recommend** contains some C code and its python bindings to compute
  correlation coefficients between lists of items.
* **video** contains a lib used to get information (screenshots, encodings, metadata) out of video files.
* there is also a bunch of python modules at the root of the `libs` folder XXX


Apps
----

Configs
-------

Default
-------
