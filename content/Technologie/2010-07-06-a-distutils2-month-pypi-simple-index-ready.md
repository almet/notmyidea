# Introducing the distutils2 index crawlers


I'm working for about a month for distutils2, even if I was being a bit
busy (as I had some class courses and exams to work on)

I'll try do sum-up my general feelings here, and the work I've made so
far. You can also find, if you're interested, my weekly summaries in [a
dedicated wiki page](http://wiki.notmyidea.org/distutils2_schedule).

## General feelings

First, and it's a really important point, the GSoC is going very well,
for me as for other students, at least from my perspective. It's a
pleasure to work with such enthusiast people, as this make the global
atmosphere very pleasant to live.

First of all, I've spent time to read the existing codebase, and to
understand what we're going to do, and what's the rationale to do so.

It's really clear for me now: what we're building is the foundations of
a packaging infrastructure in python. The fact is that many projects
co-exists, and comes all with their good concepts. Distutils2 tries to
take the interesting parts of all, and to provide it in the python
standard libs, respecting the recently written PEP about packaging.

With distutils2, it will be simpler to make "things" compatible. So if
you think about a new way to deal with distributions and packaging in
python, you can use the Distutils2 APIs to do so.

## Tasks

My main task while working on distutils2 is to provide an installation
and an un-installation command, as described in PEP 376. For this, I
first need to get informations about the existing distributions (what's
their version, name, metadata, dependencies, etc.)

The main index, you probably know and use, is PyPI. You can access it at
<http://pypi.python.org>.

## PyPI index crawling

There is two ways to get these informations from PyPI: using the simple
API, or via xml-rpc calls.

A goal was to use the version specifiers defined
in[PEP 345](http://www.python.org/dev/peps/pep-0345/) and to provides a
way to sort the grabbed distributions depending our needs, to pick the
version we want/need.

### Using the simple API

The simple API is composed of HTML pages you can access at
<http://pypi.python.org/simple/>.

Distribute and Setuptools already provides a crawler for that, but it
deals with their internal mechanisms, and I found that the code was not
so clear as I want, that's why I've preferred to pick up the good ideas,
and some implementation details, plus re-thinking the global
architecture.

The rules are simple: each project have a dedicated page, which allows
us to get informations about:

  - the distribution download locations (for some versions)
  - homepage links
  - some other useful informations, as the bugtracker address, for
    instance.

If you want to find all the distributions of the "EggsAndSpam" project,
you could do the following (do not take so attention to the names here,
as the API will probably change a bit):

```python

>>> index = SimpleIndex()
>>> index.find("EggsAndSpam")
[EggsAndSpam 1.1, EggsAndSpam 1.2, EggsAndSpam 1.3]
```

We also could use version specifiers:

```python

>>> index.find("EggsAndSpam (< =1.2)")
[EggsAndSpam 1.1, EggsAndSpam 1.2]
```

Internally, what's done here is the following:

  - it process the <http://pypi.python.org/simple/FooBar/> page,
    searching for download URLs.
  - for each found distribution download URL, it creates an object,
    containing informations about the project name, the version and the
    URL where the archive remains.
  - it sort the found distributions, using version numbers. The default
    behavior here is to prefer source distributions (over binary ones),
    and to rely on the last "final" distribution (rather than beta,
    alpha etc. ones)

So, nothing hard or difficult here.

We provides a bunch of other features, like relying on the new PyPI
mirroring infrastructure or filter the found distributions by some
criterias. If you're curious, please browse the [distutils2
documentation](http://distutils2.notmyidea.org/).

### Using xml-rpc

We also can make some xmlrpc calls to retreive informations from PyPI.
It's a really more reliable way to get informations from from the index
(as it's just the index that provides the informations), but cost
processes on the PyPI distant server.

For now, this way of querying the xmlrpc client is not available on
Distutils2, as I'm working on it. The main pieces are already present
(I'll reuse some work I've made from the SimpleIndex querying, and [some
code already set up](http://github.com/ametaireau/pypiclient)), what I
need to do is to provide a xml-rpc PyPI mock server, and that's on what
I'm actually working on.

## Processes

For now, I'm trying to follow the "documentation, then test, then code"
path, and that seems to be really needed while working with a community.
Code is hard to read/understand, compared to documentation, and it's
easier to change.

While writing the simple index crawling work, I must have done this to
avoid some changes on the API, and some loss of time.

Also, I've set up [a
schedule](http://wiki.notmyidea.org/distutils2_schedule), and the goal
is to be sure everything will be ready in time, for the end of the
summer. (And now, I need to learn to follow schedules ...)
