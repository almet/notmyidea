---
title: Debian packaging for python
tags: debian, packaging, python, stden, pyproject
status: draft
---

Recently, for [Dangerzone](https://github.com/freedomofpress/dangerzone), we [switched from stdeb to pybuild](https://github.com/freedomofpress/dangerzone/pull/901).

Stdeb wasn't working for us on Debian trixie (at the time at least), and after some tinkering, we figured it could be better to use the pybuild tools instead. I was pretty happy to find an excuse to learn about Debian packaging, as I really like the Debian project [and the culture behind it](https://www.debian.org/social_contract).

I have to say that at a first glance, this seemed overly complicated. There is *a lot* of documentation about how to do debian packaging, almost to the point where I didn't know where to start. Hopefully, [Kunal](https://legoktm.com) pointed me to the right direction.

And, it turns out I was completly wrong about the complexity. Sure there is a lot of moving pieces, but in the end, doing the packaging work was pretty straightforward. This is partially due to the fact we are packaging a client-side application, meaning we avoid some complexity about WSGI to HTTP "bridges".

In the end, most of the work is to write the proper files in the `debian` folder, and call `dpkg-buildpackage`.

## The `debian` folder

Here is the file structure:

```
debian/
├── changelog
├── compat
├── control
├── copyright
├── rules
└── source
    ├── format
    └── options
```

Let get to each of the interesting files one by one:

- `debian/changelog` contains the changelog. The format actually means something and is documented here ;
- `debian/control` contains the actual project description and dependencies, we'll get back to this in a bit ;
- `debian/rules` is a Makefile containing the targets to build the actual package ;
- `debian/compat` contains some metadata information about the version of the packaging standard this uses ;
- `debian/source/*`  contains some information on how to get the source. Depending
- I leave `debian/copyright` out of the picture, it's just

## Pybuild
