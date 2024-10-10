---
title: Debian Python packaging
tags: debian, packaging, python, stdeb, pyproject
---

Recently, I did some Debian python packaging, for the [Dangerzone](https://github.com/freedomofpress/dangerzone) project.

I was pretty happy to find an excuse to learn about Debian packaging: I'm a long time user of Debian, and [their culture](https://www.debian.org/social_contract) resonates well with me.

More specifically, we [switched from stdeb to pybuild](https://github.com/freedomofpress/dangerzone/pull/901).
Stdeb wasn't working for us on Debian trixie (at the time at least), and after some tinkering, we figured it could be better to use the pybuild tools instead.

At a first glance, all of this seemed overly complicated. There is *a lot* of documentation about how to do debian packaging, almost to the point where I didn't know where to start. Hopefully, [Kunal](https://legoktm.com) pointed me to the right direction and gave me a help when I was stuck (thanks!).

It turns out to be less complex that expected. Sure there is a bunch of moving pieces, but in the end, doing the packaging work was pretty straightforward.

Building a `.deb` package is done in two steps:

1. Filling in the `debian` folder with the proper information
2. Running the `dpkg-buildpackage` utility, which will output the `.deb`

## The `debian` folder

Most of the work is to write the proper files in the `debian` folder, and call `dpkg-buildpackage`. Here is how it looks:

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

Let's describe these files:

### `debian/changelog`

Contains... the changelog! The format is documented [here](https://www.debian.org/doc/debian-policy/ch-source.html#s-dpkgchangelog) ; In our case it looks like this:

```
dangerzone (0.7.0) unstable; urgency=low

  * Removed stdeb in favor of direct debian packaging tools

 -- Freedom of the Press Foundation   <info@freedom.press>  Tue, 27 Aug 2024 14:39:28 +0200
```

### `debian/control`

This contains the actual project description and dependencies:

```
Source: dangerzone
Maintainer: Freedom of the Press Foundation <info@freedom.press>
Section: python
Priority: optional
Build-Depends: dh-python, python3-setuptools, python3, dpkg-dev, debhelper (>= 9)
Standards-Version: 4.5.1
Homepage: https://github.com/freedomofpress/dangerzone
Rules-Requires-Root: no

Package: dangerzone
Architecture: any
Depends: ${misc:Depends}, ${python3:Depends}, podman, python3, python3-pyside2.qtcore, python3-pyside2.qtgui, python3-pyside2.qtwidgets, python3-pyside2.qtsvg, python3-appdirs, python3-click, python3-xdg, python3-colorama, python3-requests, python3-markdown, python3-packaging
Description: Take potentially dangerous PDFs, office documents, or images
  Dangerzone is an open source desktop application that takes potentially dangerous PDFs, office documents, or images and converts them to safe PDFs. It uses disposable VMs on Qubes OS, or container technology in other OSes, to convert the documents within a secure sandbox.
.
```

All the fields are almost self-explanatory, and [documented here](https://www.debian.org/doc/debian-policy/ch-controlfields.html).

In our case, here are the ones worth mentionning:

- `Rules-Requires-Root` allows to tell that the building of the package doesn't actually require root privileges.
- Some specific templates are used, like ${python3:Depends} in the `Depends` definition. This will be filled-in by pybuild.

### `debian/rules`

This is basically a Makefile containing the targets to build the actual package. In our case, because we are delegating the build steps to pybuild, it's almost empty. It looks like this:

```Makefile
#!/usr/bin/make -f
export PYBUILD_NAME=dangerzone
export DEB_BUILD_OPTIONS=nocheck

%:
	dh $@ --with python3 --buildsystem=pybuild    
```

### `debian/source/*`

Contains some information on how to get the source. Depending on how you want to do it there are multiple ways to do this. In our case, because the `debian` folder is part of the repository we want to package, we use the `3.0 (native)` format, which will create a compressed file (tarball).

`debian/source/format` defines this format:
```
3.0 (native)    
```

`debian/source/options` specifies the options that can be useful when creating the tar file that will be used as a source. As you can see, we instruct it to ignore a few folders we don't want to package:

```
compression = "gzip"
tar-ignore = "dev_scripts"
tar-ignore = ".*"
tar-ignore = "__pycache__"    
```

### Additional `debian/*` files

- `debian/copyright` contains [the license information about the package](https://www.debian.org/doc/debian-policy/ch-source.html#copyright-debian-copyright).
- `debian/compat` contains some metadata information about the version of the packaging standard this uses. In our case [`10`]();

## Pybuild

I've mentionned we are using [pybuild](https://wiki.debian.org/Python/Pybuild). Pybuild is doing the work of getting the dependencies out of `setup.py`, or `pyproject.toml`.

### Pyproject

In the case you are using `pyproject.toml` (and you should!), you can use [`pybuild-plugin-pyproject`](https://packages.debian.org/bookworm/pybuild-plugin-pyproject) to get the dependencies out of it.

On Dangerzone, at the time of writing this we are still supporting Ubuntu Focal, which doesn't provide this pyproject plugin, hence why it is not configured.

If we had to do it, we would do the following:

1. Add it to the build dependencies in `debian/control`
2. Upate the `debian/rules` file to specify the following:

```
export PYBUILD_SYSTEM=pyproject
```

Hope it's useful :-)
