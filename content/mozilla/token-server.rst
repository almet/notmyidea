Mozilla - The sagrada token server
##################################

:date: 19-03-2012
:tags: sagrada, python, browserid
:status: draft

Since I started, back in december, we started a new project on the services
team, which aims to bring a central authentication point on our server side.
This had been motivated by the fact that we are switching our services
authentication mechanism from basic HTTP auth to browserid (this was basically
for sync in the first place, and now for AITC, a.k.a Market Place APIs).

- A Token Server ?
- Services architecture (server / nodes)
- MAC auth
- Crypto / Signing
  - HKDF
  - Signing the tokens
  - Parsing browserid assertions
- Resources

A token server ?
================

So, we don't want to be tied to any authentication mean on our platform. The
best way to accomplish this is to chose one and to provide a way to map all the
potential authentication means to the chosen one.

In addition to trade a browserid assertion for another authentication token,
the mission of the token server is to retrieve the node allocation of a
particular user, and eventually assign it to a node.

To resume, we take any authentication scheme (browserid for now) and
trade it for another one we can use for all of our services. This has several
advantages:

* We don't need to check the browserid assertion at each request. This avoids
  doing crypto at each request.
* As said, we are able to deal with different authentication schemes. If we
  want to use openid, we just need to add support for it on one location
* The node allocation is done anyways (the user need to know wich node it is
  assigned to) so it doesn't add an extra call for this.

Our architecture
================

I'm talking about nodes, users and services. Let's clarifiy a bit all this.
Because at the services team, we mostly care about being able to scale our
infrastructures without (too much) pain, we try to avoid SPOFs (Single Point Of
Failure) of any sort. For this purpose we expose at the authentication layer
information about the node that need to be retrieved by the clients.

What? clients? Okay, here is what the authentication looks like::

    User-Agent              Token Server                Node
        |                        |                       |
        |     <bid assertion>    |                       |
        |----------------------->|                       |
        |                        |                       |
        |<token + userid + node> |                       |
        |<-----------------------|                       |
        |                        |                       |
        |                <service-data + token>          |
        |----------------------------------------------->|

In HTTP terms, looks like this, the user agent (client) gives a browserid
assertion and receives back information about the service it should deal with

::

    > HTTP POST http://token.services.mozilla.org/1.0/<app>/<app-version>
    > Data: # some authentication information (browserid assertion in our case)
    < Header: 200 OK
    < Data: "{'id': token, 'key': secret, 'uid': uid, 'api_endpoint': api_endpoint}"

(This is an hand crafted request/response flow)

We don't bother about the signing and crypto details in here as it is explained
in a later section, but basically, we asked for a node, with a specific
browserid assertions and now we have an *api_endpoint* to send our requests
against, along with the token.

Crypto details
==============

All the flow is explained in our documentation, for the token server
