An amazing summer of code working on distutils2
###############################################

:Date: 2010-08-16

The `Google Summer of Code <http://code.google.com/soc/>`_ I've
spent working on `distutils2 <http://hg.python.org/distutils2/>`_
is over. It was a really amazing experience, for many reasons.

First of all, we had a very good team, we were 5 students working
on distutils2: `Zubin <http://zubin71.wordpress.com>`_,
`Éric <http://wokslog.wordpress.com/>`_,
`Josip <http://gsoc.djolonga.com/>`_,
`Konrad <http://konryd.blogspot.com/>`_ and me. In addition,
`Mouad <http://mouadino.blogspot.com/>`_ have worked on the PyPI
testing infrastructure. You could find what each person have done
on
`the wiki page of distutils2 <http://bitbucket.org/tarek/distutils2/wiki/GSoC_2010_teams>`_.

We were in contact with each others really often, helping us when
possible (in #distutils), and were continuously aware of the state
of the work of each participant. This, in my opinion, have bring us
in a good shape.

Then, I've learned a lot. Python packaging was completely new to me
at the time of the GSoC start, and I was pretty unfamiliar with
python good practices too, as I've been introducing myself to
python in the late 2009.

I've recently looked at some python code I wrote just three months
ago, and I was amazed to think about many improvements to made on
it. I guess this is a good indicator of the path I've traveled
since I wrote it.

This summer was awesome because I've learned about python good
practices, now having some strong
`mercurial <http://mercurial.selenic.com/>`_ knowledge, and I've
seen a little how the python community works.

Then, I would like to say a big thanks to all the mentors that have
hanged around while needed, on IRC or via mail, and especially my
mentor for this summer, `Tarek Ziadé <http://tarek.ziade.org>`_.

Thanks a lot for your motivation, your leadership and your
cheerfulness, even with a new-born and a new work!

Why ?
-----

I wanted to work on python packaging because, as the time pass, we
were having a sort of complex tools in this field. Each one wanted
to add features to distutils, but not in a standard way.

Now, we have PEPs that describes some format we agreed on (see PEP
345), and we wanted to have a tool on which users can base their
code on, that's `distutils2 <http://hg.python.org/distutils2/>`_.

My job
------

I had to provides a way to crawl the PyPI indexes in a simple way,
and do some installation / uninstallation scripts.

All the work done is available in
`my bitbucket repository <http://bitbucket.org/ametaireau/distutils2/>`_.

Crawling the PyPI indexes
~~~~~~~~~~~~~~~~~~~~~~~~~

There are two ways of requesting informations from the indexes:
using the "simple" index, that is a kind of REST index, and using
XML-RPC.

I've done the two implementations, and a high level API to query
those twos. Basically, this supports the mirroring infrastructure
defined in PEP 381. So far, the work I've done is gonna be used in
pip (they've basically copy/paste the code, but this will change as
soon as we get something completely stable for distutils2), and
that's a good news, as it was the main reason for what I've done
that.

I've tried to have an unified API for the clients, to switch from
one to another implementation easily. I'm already thinking of
adding others crawlers to this stuff, and it was made to be
extensible.

If you want to get more informations about the crawlers/PyPI
clients, please refer to the distutils2 documentation, especially
`the pages about indexes <http://distutils2.notmyidea.org/library/distutils2.index.html>`_.

You can find the changes I made about this in the
`distutils2 <http://hg.python.org/distutils2/>`_ source code .

Installation / Uninstallation scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next step was to think about an installation script, and an
uninstaller. I've not done the uninstaller part, and it's a smart
part, as it's basically removing some files from the system, so
I'll probably do it in a near future.

`distutils2 <http://hg.python.org/distutils2/>`_ provides a way to
install distributions, and to handle dependencies between releases.
For now, this support is only about the last version of the
METADATA (1.2) (See, the PEP 345), but I'm working on a
compatibility layer for the old metadata, and for the informations
provided via PIP requires.txt, for instance.

Extra work
~~~~~~~~~~

Also, I've done some extra work. this includes:


-  working on the PEP 345, and having some discussion about it
   (about the names of some fields).
-  writing a PyPI server mock, useful for tests. you can find more
   information about it on the
   `documentation <http://distutils.notmyidea.org>`_.

Futures plans
-------------

As I said, I've enjoyed working on distutils2, and the people I've
met here are really pleasant to work with. So I *want* to continue
contributing on python, and especially on python packaging, because
there is still a lot of things to do in this scope, to get
something really usable.

I'm not plainly satisfied by the work I've done, so I'll probably
tweak it a bit: the installer part is not yet completely finished,
and I want to add support for a real
`REST <http://en.wikipedia.org/wiki/Representational_State_Transfer>`_
index in the future.

We'll talk again of this in the next months, probably, but we
definitely need a real
`REST <http://en.wikipedia.org/wiki/Representational_State_Transfer>`_
API for `PyPI <http://pypi.python.org>`_, as the "simple" index
*is* an ugly hack, in my opinion. I'll work on a serious
proposition about this, maybe involving
`CouchDB <http://couchdb.org>`_, as it seems to be a good option
for what we want here.

Issues
------

I've encountered some issues during this summer. The main one is
that's hard to work remotely, especially being in the same room
that we live, with others. I like to just think about a project
with other people, a paper and a pencil, no computers. This have
been not so possible at the start of the project, as I needed to
read a lot of code to understand the codebase, and then to
read/write emails.

I've finally managed to work in an office, so good point for
home/office separation.

I'd not planned there will be so a high number of emails to read,
in order to follow what's up in the python world, and be a part of
the community seems to takes some times to read/write emails,
especially for those (like me) that arent so confortable with
english (but this had brought me some english fu !).

Thanks !
--------

A big thanks to `Graine Libre <http://www.graine-libre.fr/>`_ and
`Makina Corpus <http://www.makina-corpus.com/>`_, which has offered
me to come into their offices from time to time, to share they
cheerfulness ! Many thanks too to the Google Summer of Code program
for setting up such an initiative. If you're a student, if you're
interested about FOSS, dont hesitate any second, it's a really good
opportunity to work on interesting projects!


