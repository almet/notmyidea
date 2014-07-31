What's Hawk and how to use it?
##############################

:date: 2014-07-31

We recently had to implement `the Hawk authentication scheme
<https://github.com/hueniverse/hawk>`_ for a number of projects, and we came up
creating two libraries to ease integration into pyramid and node.js apps.

But maybe you don't know Hawk. Hawk is a relatively new technology, crafted by
one of the original OAuth specification authors, that intends to replace the
2-legged OAuth authentication scheme using a simpler approach.

It is an authentication scheme for HTTP, built around HMAC digests of
requests and responses.

Every authenticated client request has an Authorization header containing a MAC
and some additional metadata, and each server response to authenticated
requests contains a Server-Authorization header that authenticates the
response, so the client is sure it comes from the right server.


Exchange of the hawk id and hawk secret
=======================================

To sign the requests, a client needs to retrieve a token id and secret from the
server.

Hawk itself does not define how the hawk id and secret should be exchanged
between the server and the client. The excellent team behind `Firefox Accounts
<http://accounts.firefox.com>`_ put together a scheme to do that, which acts
like the following:

.. note:: 

  All this derivation crazyness might seem a bit complicated, but don't worry,
  we put together some libraries that takes care of that for you automatically.

  If you are not interested into these details, you can directly jump to the
  next section to see how to use the libraries.

When your server application needs to send you the credentials, it will return
it inside a specific `Hawk-Session-Token` header.

In order to get the hawk credentials to use on the client you will need to:

First, do an `HKDF derivation <http://en.wikipedia.org/wiki/HKDF>`_ on the
given session token. You'll need to use the following parameters::

    key_material = HKDF(hawk_session, "", 'identity.mozilla.com/picl/v1/sessionToken', 32*2)

The "identity.mozilla.com/picl/v1/sessionToken" is a reference to this way of
deriving the credentials, not an actual URL.

Then, the key material you'll get out of the HKDF need to be separated into two
parts, the first 32 hex caracters are the hawk id, and the next 32 ones are the
hawk key.

Credentials::

    credentials = {
        'id': keyMaterial[0:32],
        'key': keyMaterial[32:64],
        'algorithm': 'sha256'
    }

Httpie
======

To showcase APIs in the documentation, I like to use `httpie
<https://github.com/jakubroztocil/httpie>`_, a curl-replacement with a nicer
API, built around `the python requests library <http://python-requests.org>`_.

Luckily, HTTPie allows you to plug different authentication schemes for it, so `I wrote
a wrapper <https://github.com/mozilla-services/requests-hawk>`_ around `mohawk
<https://github.com/kumar303/mohawk>`_ to add hawk support to the requests lib.

Doing hawk requests in your terminal is now as simple as::

    $ pip install requests-hawk httpie
    $ http GET localhost:5000/registration --auth-type=hawk --auth='id:key'

In addition, it will help you to craft requests using the requests library::
  
    import requests
    from requests_hawk import HawkAuth

    hawk_auth = HawkAuth(
      credentials={'id': id, 'key': key, 'algorithm': 'sha256'})

    requests.post("/url", auth=hawk_auth)

Alternatively, if you don't have the token id and secret, you can pass the hawk
session token I talked about earlier and the lib will take care of the
derivation for you::

    hawk_auth = HawkAuth(
        hawk_session=resp.headers['hawk-session-token'],
        server_url=self.server_url
    )
    requests.post("/url", auth=hawk_auth)

Integrate with python pyramid apps
==================================

If you're writing pyramid applications, you'll be happy to learn that `Ryan
Kelly <https://www.rfk.id.au/blog/>`_ put together a library that makes Hawk
work as an Authentication provider for them. I'm chocked how simple it
is to use it.

Here is a demo of how we implemented it for Daybed::

  from pyramid_hawkauth import HawkAuthenticationPolicy
  
  policy = HawkAuthenticationPolicy(decode_hawk_id=get_hawk_id)
  config.set_authentication_policy(authn_policy)

The `get_hawk_id` function is a function that takes a request and
a tokenid and returns a tuple of `(token_id, token_secret)`.

How you want to store the tokens and retrieve them is up to you. The default
implementation (e.g. if you don't pass a `decode_hawk_id` function) decodes the
secret from the token itself, using a master secret on the server (so you don't
need to store anything).

Integrate with node.js Express apps
===================================

We had to implement Hawk authentication for two node.js projects and finally
came up factorizing everything in a library for express, named `express-hawkauth
<https://github.com/mozilla-services/express-hawkauth>`_.

In order to plug it in your application, you'll need to use it as
a middleware::

    var express = require("express");
    var hawk = require("express-hawkauth");
    app = express();

    var hawkMiddleware = hawk.getMiddleware({
      hawkOptions: {},
      getSession: function(tokenId, cb) {
        // A function which pass to the cb the key and algorithm for the
        // given token id. First argument of the callback is a potential
        // error.
        cb(null, {key: "key", algorithm: "sha256"});
      },
      createSession: function(id, key, cb) {
        // A function which stores a session for the given id and key.
        // Argument returned is a potential error.
        cb(null);
      },
      setUser: function(req, res, tokenId, cb) {
        // A function that uses req and res, the hawkId when they're known so
        // that it can tweak it. For instance, you can store the tokenId as the
        // user.
        req.user = tokenId;
      }
    });

    app.get('/hawk-enabled-endpoint', hawkMiddleware);


If you pass the `createSession` parameter, all non-authenticated requests will
create a new hawk session and return it with the response, in the
`Hawk-Session-Token` header.

If you want to only check a valid hawk session exists (without creating a new
one), just create a middleware which doesn't have any `createSession` parameter
defined.

Some reference implementations
==============================

As a reference, here is how we're using the libraries I'm talking about, in
case that helps you to integrate with your projects.

- The Mozilla Loop server `uses hawk as authentication once you're logged in with
  a valid BrowserID assertion
  <https://github.com/mozilla-services/loop-server/blob/master/loop/index.js#L70-L133>`_;
  request, to keep a session between client and server;
- `I recently added hawk support on the Daybed project
  <https://github.com/spiral-project/daybed/commit/f178b4e43015fa077430798dcd3d0886c7611caf>`_
  (that's a pyramid / cornice) app.
