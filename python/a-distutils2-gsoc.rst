A Distutils2 GSoC
#################

:date: 2010-05-01

WOW. I've been accepted to be a part of the
`Google Summer Of Code <http://code.google.com/intl/fr/soc/>`_
program, and will work on `python <http://python.org/>`_
`distutils2 <http://hg.python.org/distutils2/>`_, with
`a <http://pygsoc.wordpress.com/>`_
`lot <http://konryd.blogspot.com/>`_ `of <http://ziade.org/>`_
(intersting!) `people <http://zubin71.wordpress.com/>`_.

    So, it's about building the successor of Distutils2, ie. "the
    python package manager". Today, there is too many ways to package a
    python application (pip, setuptools, distribute, distutils, etc.)
    so there is a huge effort to make in order to make all this
    packaging stuff interoperable, as pointed out by
    the `PEP 376 <http://www.python.org/dev/peps/pep-0376/>`_.

In more details, I'm going to work on the Installer / Uninstaller 
features of Distutils2, and on a PyPI XML-RPC client for distutils2. 
Here are the already defined tasks:

-  Implement Distutils2 APIs described in PEP 376.
-  Add the uninstall command.
-  think about a basic installer / uninstaller script. (with deps)
   -- similar to pip/easy\_install
-  in a pypi subpackage;
-  Integrate a module similar to setuptools' package\_index'
-  PyPI XML-RPC client for distutils 2:
   http://bugs.python.org/issue8190

As I'm relatively new to python, I'll need some extra work in order
to apply all good practice, among other things that can make a
developper-life joyful. I'll post here, each week, my advancement,
and my tought about python and especialy python packaging world.
