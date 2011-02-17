Sprinting on distutils2 in Tours
################################

:date: 2010-07-06

Yesterday, as I was traveling to Tours, I've took some time to
visit Éric, another student who's working on distutils2 this
summer, as a part of the GSoC. Basically, it was to take a drink,
discuss a bit about distutils2, our respective tasks and general
feelings, and to put a face on a pseudonym. I'd really enjoyed this
time, because Éric knows a lot of things about mercurial and python
good practices, and I'm eager to learn about those. So, we have
discussed about things, have not wrote so much code, but have some
things to propose so far, about documentation, and I also provides
here some bribes of conversations we had.
Documentation
~~~~~~~~~~~~~

While writing the PyPI simple index crawler documentation, I
realized that we miss some structure, or how-to about the
documentation. Yep, you read well. We lack documentation on how to
make documentation. Heh. We're missing some rules to follow, and
this lead to a not-so-structured final documentation. We probably
target three type of publics, and we can split the documentation
regarding those:

-  **Packagers** who want to distribute their softwares.
-  **End users** who need to understand how to use end user
   commands, like the installer/uninstaller
-  **packaging coders** who *use* distutils2, as a base for
   building a package manager.

We also need to discuss about a pattern to follow while writing
documentation. How many parts do we need ? Where to put the API
description ? etc. That's maybe seems to be not so important, but I
guess the readers would appreciate to have the same structure all
along distutils2 documentation.
Mercurial
~~~~~~~~~

I'm really *not* a mercurial power user. I use it on daily basis,
but I lack of basic knowledge about it. Big thanks Éric for sharing
yours with me, you're of a great help. We have talked about some
mercurial extensions that seems to make the life simpler, while
used the right way. I've not used them so far, so consider this as
a personal note.

-  hg histedit, to edit the history
-  hg crecord, to select the changes to commit

We have spent some time to review a merge I made sunday, to
re-merge it, and commit the changes as a new changeset. Awesome.
These things make me say I **need** to read
`the hg book <http://hgbook.red-bean.com/read/>`_, and will do as
soon as I got some spare time: mercurial seems to be simply great.
So ... Great. I'm a powerful merger now !
On using tools
~~~~~~~~~~~~~~

Because we *also* are *hackers*, we have shared a bit our ways to
code, the tools we use, etc. Both of us were using vim, and I've
discovered vimdiff and hgtk, which will completely change the way I
navigate into the mercurial history. We aren't "power users", so we
have learned from each other about vim tips. You can find
`my dotfiles on github <http://github.com/ametaireau/dotfiles>`_,
if it could help. They're not perfect, and not intended to be,
because changing all the time, as I learn. Don't hesitate to have a
look, and to propose enhancements if you have !
On being pythonic
~~~~~~~~~~~~~~~~~

My background as an old Java user disserves me so far, as the
paradigms are not the same while coding in python. Hard to find the
more pythonic way to do, and sometimes hard to unlearn my way to
think about software engineering. Well, it seems that the only
solution is to read code, and to re-read import this from times to
times !
`Coding like a pythonista <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html>`_
seems to be a must-read, so, I know what to do.
Conclusion
~~~~~~~~~~

It was really great. Next time, we'll need to focus a bit more on
distutils2, and to have a bullet list of things to do, but days
like this one are opportunities to catch ! We'll probably do
another sprint in a few weeks, stay tuned !

