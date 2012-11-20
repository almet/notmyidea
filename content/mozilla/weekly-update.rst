Mozilla's weekly update #1
##########################

:date: 20-09-2012
:status: draft

My day-to-day work is changing a lot these days, as I'm working on different
tools and working across different teams.  I thought it could be useful to have
a place to put updates weekly about what's going-on. This can be extra useful
for folks that are not on the same timezone I am (I'm looking at you,
California), so let's try this.

I'm not used to post regularly, but I will try to update the blog with an entry
each week, if there is something interesting to say.

Circus
======

As you may know, last week we had a sprint about Circus at PyconFR, we now have
a bunch of folks interested by the project now, and some activity on our irc
channel (#mozilla-circus on freenode).

I've written `a more comprehensive wrap-up about this sprint
<http://blog.notmyidea.org/circus-sprint-at-pyconfr.html>`_, so have a look at
it if you're interested!

Vaurien
=======

Vaurien is a TCP proxy which can be useful for our load-testing. its goal is to
sometimes let the traffic go trough, sometimes play a bit with it (add delays,
timeouts, close the socket etc) to check how the stack is behaving when under
pressure.

The code isn't used to test our services yet but we have something interesting
to show: http://github.com/mozilla-services/vaurien/

I will not explain the specifics here, I've tried to make `the README
<https://github.com/mozilla-services/vaurien#vaurien>`_ explicit enough.

Marteau
=======

`Marteau <https://github.com/mozilla-services/marteau/>`_ is the tool we're
using to throw load-test to our services, to check that they're able to handle
it. It's basically a frontend to Funkload. Tarek worked on adding real-time
feedback from the nodes (when in distributed mode, Funkload clients are
deployed on some nodes and send traffic to the service from there), and I am
working on making this available on the web interface. This means playing a bit
with web-sockets and javascript, yay.

Marketplace packaging
=====================

Currently, the application behind market place, `Zamboni
<https://github.com/mozilla/zamboni>`_ uses a non-standard mechanism to deal
with its dependencies. A `vendor` folder contains the packages themselves, in
the form of git submodules. This comes with some drawbacks such as the fact
that it's not easy to upgrade dependencies etc, and very long updates of the
repository, into other things.

We were also dependant on github to deploy Marketplace, which isn't reliable at
all, especially when you know that github was down last week, for instance. We
now have a local PyPI mirror at Mozilla, and we use it to avoid reaching the
internet for something else than our code.

This also means that we need to pull all the dependencies out of this `vendor`
folder, and rely on PyPI packages when they are up to date. Then we will be
able to directly use `pip` to deal with dependency management and packaging.

Splitting up the Marketplace
============================

Zamboni is currently one big django project. This led to something quite hard
to understand and hard to deal with., especially for newcomers. Also, it means
that all the aspects of the site are inter-connected and that you need to be
comfortable with the whole infrastructure of the project to add new features
/ fix bugs.

Splitting this big project into smaller chunks can allow to have something
easier to work on. We're trying to do that these days. More on this later :)

That's all for now, I'll try to keep you posted on all this, see you next week
:-)
