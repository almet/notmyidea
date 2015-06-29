Web distribution signing
########################

:lang: en
:date: 2015-06-29
:headline: Bringing trust back between software authors and user agents.

.. note:: I'm not a crypto expert, nor pretend to be one. These are thoughts
          I want to share with the crypto community to actually see if any
          solution exists to solve this particular problem.

One `often pointed <http://www.tonyarcieri.com/whats-wrong-with-webcrypto>`_
flaw in web-based cryptographic applications is the fact that there is no way
to trust online software distributions. Put differently, you don't actually
trust the software authors but are rather trusting the software distributors
and certificate authorities (CAs).

Attack vectors
==============

Let's try to describe a few potential attacks:

*Application Authors* just released a new version of their open source web
crypto messaging application. *Indie Hoster* installs it on their servers so
that a wide audience can actually use it.

Someone alters the files on *Indie Hoster* servers, effectively replacing them with
other *altered files* with less security properties / a backdoor. This someone could either be
*Evil Attacker* or *Indie Hoster* which can already alter these files because
they're distributing them.

Trusted *Certificate Authorities* (read "governments") can also trick to
User Agents (i.e. Firefox) into thinking they're talking to *Indie Hoster* even
if they're actually talking to a different party.

**Altered files** are being served to the User Agents, and *Evil Attacker* now
has a way to actually attack the end users.

Problem Mitigation
==================

I hope it's clear by now that we miss a way to create trust between
*Application Authors* and *User Agents*. The User-Agent has to trust
*Certificate Authorities* and *Indie Hoster*.

I believe this specific problem had been solved, at least partially, for
desktop software distribution: *Crypto Experts* audit the software, sign it
somehow and then this signature can be checked locally during installation or
runtime.

For web applications, we don't have such a mechanism, but it should be
possible. Consider the following:

- *App Authors* publish a new version of their software; They provide a hash of
  each of their distributed files;
- *Crypto Experts* audit these files and sign the hashes with their private
  key;
- *User Agents* have a way to add the certificate for *Crypto Experts*;
- When a *User Agent* downloads files, it checks if they're signed.

Chosing who you trust
=====================

.. note:: And now is the time I start talking about things I don't know. But
          maybe you trust me?

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

Now, I honestly have no idea if this thing is practicable, and I'm pretty sure
this design has many security problems attached to it. But that's a problem
I would really like to see solved one day, so here the start of the discussion,
don't hesitate to `get in touch </pages/about.html>`_!
