Web distribution signing
########################

:lang: en
:date: 2015-10-12
:headline: Bringing trust back between software authors and user agents.

.. note:: I'm not a crypto expert, nor pretend to be one. These are thoughts
          I want to share with the crypto community to actually see if any
          solution exists to solve this particular problem.

One `often pointed <http://www.tonyarcieri.com/whats-wrong-with-webcrypto>`_
flaw in web-based cryptographic applications is the fact that there is no way
to trust online software distributions. Put differently, you don't actually
trust the software authors but are rather trusting the software distributors
and certificate authorities (CAs).

I've been talking with a few folks in the past months about that and they
suggested me to publish something to discuss the matter. So here I come!

The problem (Attack vectors)
============================

Let's try to describe a few potential attacks:

*Application Authors* just released a new version of their open source web
crypto messaging application. An *Indie Hoster* installs it on their servers so
a wide audience can actually use it.

Someone alters the files on *Indie Hoster* servers, effectively replacing them with
other *altered files* with less security properties / a backdoor. This someone could either be
an *Evil Attacker* which found its way trough, the *Indie Hoster* or a CDN
which delivers the files,

Trusted *Certificate Authorities* ("governments" or "hacking team") can also
trick the User Agents (i.e. Firefox) into thinking they're talking to *Indie
Hoster* even though they're actually talking to a different server.

**Altered files** are then being served to the User Agents, and *Evil Attacker*
now has a way to actually attack the end users.

Problem Mitigation
==================

Part of the problem is solved by the recently introduced `Sub Resource
Integrity <https://w3c.github.io/webappsec/specs/subresourceintegrity/>`_
(SRI). To quote them: "[it] defines a mechanism by which user agents may verify
that a fetched resource has been delivered without unexpected manipulation.".

SRI is a good start, but isn't enough: it ensures the assets (JavaScript files,
mainly) loaded from a specific HTML page are the ones the author of the HTML
page intends. However, SRI doesn't allow the User Agent to ensure the HTML page
is the one he wants.

In other words, we miss a way to create trust between *Application Authors* and
*User Agents*. The User-Agent currently has to trust the *Certificate
Authorities* and the delivery (*Indie Hoster*).

For desktop software distribution: *Crypto Experts* audit the software, sign it
somehow and then this signature can be checked locally during installation or
runtime. It's not automated, but at least it's possible.

For web applications, we don't have such a mechanism, but it should be
possible. Consider the following:

- *App Authors* publish a new version of their software; They provide a hash of
  each of their distributed files (including the HTML files);
- *Crypto Experts* audit these files and sign the hashes somehow;
- *User Agents* can chose to trust some specific *Crypto Experts*;
- When a *User Agent* downloads files, it checks if they're signed by a trusted
  party.


Chosing who you trust
=====================

In terms of user experience, handling certificates is hard, and that's where
the community matters. Distributions such as `Tails <https://tails.boom.org>`_
could chose who they trust to verify the files, and issue warnings / refuse to
run the application in case files aren't verified.

But, as highligted earlier, CAs are hard to trust. A new instance of the same
CA system wouldn't make that much differences, expect the fact that
distributions could ship with a set of trusted authorities (for which
revocation would still need to be taken care of).

.. epigraph::

  [...] users are vulnerable to MitM attacks by the authority, which can vouch
  for, or be coerced to vouch for, false keys. This weakness has been
  highlighted by recent CA scandals. Both schemes can also be attacked if the
  authority does not verify keys before vouching for them.

  -- `SoK : Secure Messaging <http://cacr.uwaterloo.ca/techreports/2015/cacr2015-02.pdf>`_;

It seems that some other systems could allow for something more reliable:

.. epigraph::

  Melara et al proposed CONIKS, using a series of chained commitments to Merkle
  prefix trees to build a key directory [...] for which individual users can
  efficiently verify the consistency of their own entry in the directory
  without relying on a third party.
  
  This “self- auditing log” approach makes the system partially have no
  auditing required (as general auditing of non-equivocation is still required)
  and also enables the system to be privacy preserving as the entries in the
  directory need not be made public. This comes at a mild bandwidth cost not
  reflected in our table, estimated to be about 10 kilobytes per client per day
  for self-auditing.

  -- `SoK : Secure Messaging <http://cacr.uwaterloo.ca/techreports/2015/cacr2015-02.pdf>`_;

Now, I honestly have no idea if this thing solves the whole problem, and I'm pretty sure
this design has many security problems attached to it.

However, that's a problem I would really like to see solved one day, so here
the start of the discussion, don't hesitate to `get in touch
</pages/about.html>`_!
