# Wrap up of the distutils2 paris' sprint

Finally, thanks to a bunch of people that helped me to pay my train and
bus tickets, I've made it to paris for the distutils2 sprint.

They have been a bit more than 10 people to come during the sprint, and
it was very productive. Here's a taste of what we've been working on:

  - the datafiles, a way to specify and to handle the installation of
    files which are not python-related (pictures, manpages and so on).
  - mkgcfg, a tool to help you to create a setup.cfg in minutes (and
    with funny examples)
  - converters from setup.py scripts. We do now have a piece of code
    which reads your current setup.py file and fill in some fields in
    the setup.cfg for you.
  - a compatibility layer for distutils1, so it can read the setup.cfg
    you will wrote for distutils2 :-)
  - the uninstaller, so it's now possible to uninstall what have been
    installed by distutils2 (see PEP 376)
  - the installer, and the setuptools compatibility layer, which will
    allow you to rely on setuptools' based distributions (and there are
    plenty of them\!)
  - The compilers, so they are more flexible than they were. Since
    that's an obscure part of the code for distutils2 commiters (it
    comes directly from the distutils1 ages), having some guys who
    understood the problematics here was a must.

Some people have also tried to port their packaging from distutils1 to
distutils2. They have spotted a number of bugs and made some
improvements to the code, to make it more friendly to use.

I'm really pleased to see how newcomers went trough the code, and
started hacking so fast. I must say it wasn't the case when we started
to work on distutils1 so that's a very good point: people now can hack
the code quicker than they could before.

Some of the features here are not *completely* finished yet, but are on
the tubes, and will be ready for a release (hopefully) at the end of the
week.

Big thanks to logilab for hosting (and sponsoring my train ticket) and
providing us food, and to bearstech for providing some money for
breakfast and bears^Wbeers.

Again, a big thanks to all the people who gave me money to pay the
transport, I really wasn't expecting such thing to happen :-)
