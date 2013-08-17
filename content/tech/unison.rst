Working directly on your server? How to backup and sync your dev environment with unison
########################################################################################

:date: 16/03/2011
:tags: freebsd, unison

I have a server running freebsd since some time now, and was wondering about
the possibility to directly have a development environment ready to use when
I get a internet connexion, even if I'm not on my computer.

Since I use vim to code, and spend most of my time in a console while
developing, it's possible to work via ssh, from everywhere.

The only problem is the synchronisation of the source code, config files etc.
from my machine to the server.

Unison provides an interesting way to synchronise two folders, even over
a network. So let's do it !

Creating the jail
=================

In case you don't use FreeBSD, you can skip this section.

.. code-block:: bash

    # I have a flavour jail named default
    $ ezjail-admin -f default workspace.notmyidea.org 172.19.1.6
    $ ezjail-admin start workspace.notmyidea.org

In my case, because the "default" flavour contains already a lot of interesting
things, my jail come already setup with ssh, bash and vim for instance, but
maybe you'll need it in your case.

I want to be redirected to the ssh of the jail when I connect to the host with
the 20006 port. Add lines in `/etc/pf.conf`::

    workspace_jail="172.19.1.6"
    rdr on $ext_if proto tcp from any to $ext_ip port 20006 -> $workspace_jail port 22

Reload packet filter rules

.. code-block:: bash

    $ /etc/rc.d/pf reload

Working with unison
===================

Now that we've set up the jail. Set up unison on the server and on your client.
Unison is available on the freebsd ports so just install it

.. code-block:: bash

    $ ssh notmyidea.org -p 20006
    $ make -C /usr/ports/net/unison-nox11 config-recursive
    $ make -C /usr/ports/net/unison-nox11 package-recursive

Install as well unison on your local machine. Double check to install the same
version on the client and on the server. Ubuntu contains the 2.27.57 as well as
the 2.32.52.

Check that unison is installed and reachable via ssh from your machine

.. code-block:: bash

    $ ssh notmyidea.org -p 20006 unison -version
    unison version 2.27.157
    $ unison -version
    unison version 2.27.57

Let sync our folders
====================

The first thing I want to sync is my vim configuration. Well, it's already `in
a git repository <http://github.com/ametaireau/dotfiles/>`_ but let's try to use
unison for it right now.

I have two machines then: `workspace`, the jail, and `ecureuil` my laptop.

.. code-block:: bash

    unison .vim ssh://notmyidea.org:20006/.vim
    unison .vimrc ssh://notmyidea.org:20006/.vimrc


It is also possible to put all the informations in a config file, and then to
only run `unison`. (fire up `vim ~/.unison/default.prf`.

Here is my config::

    root = /home/alexis
    root = ssh://notmyidea.org:20006

    path = .vimrc
    path = dotfiles
    path = dev

    follow = Name *

My vimrc is in fact a symbolic link on my laptop, but I don't want to specify
each of the links to unison. That's why the `follow = Name *` is for.

The folders you want to synchronize are maybe a bit large. If so, considering
others options such as rsync for the first import may be a good idea (I enjoyed
my university huge upload bandwith to upload 2GB in 20mn ;)

Run the script frequently
=========================

Once that done, you just need to run the unison command line some times when
you want to sync your two machines. I've wrote a tiny script to get some
feedback from the sync:

.. code-block:: python

    import os
    from datetime import datetime

    DEFAULT_LOGFILE = "~/unison.log"
    PROGRAM_NAME = "Unison syncer"

    def sync(logfile=DEFAULT_LOGFILE, program_name=PROGRAM_NAME):
        # init
        display_message = True
        error = False

        before = datetime.now()
        # call unison to make the sync
        os.system('unison -batch > {0}'.format(logfile))

        # get the duration of the operation
        td = datetime.now() - before
        delta = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6

        # check what was the last entry in the log
        log = open(os.path.expanduser(logfile))
        lines = log.readlines()
        if 'No updates to propagate' in lines[-1]:
            display_message = False
        else:
            output = [l for l in lines if "Synchronization" in l]

            message = output[-1]
            message += " It took {0}s.".format(delta)

        if display_message:
            os.system('notify-send -i {2} "{0}" "{1}"'.format(program_name, message, 
                'error' if error else 'info'))

    if __name__ == "__main__":
        sync()

This is probably perfectible, but that does the job.

Last step is to tell you machine to run that frequently. That's what `crontab` 
is made for, so let's `crontab -e`::

    $ * */3 * * * . ~/.Xdbus; /usr/bin/python /home/alexis/dev/python/unison-syncer/sync.py

The `~/.Xdbus` allows cron to communicate with your X11 session. Here is its
content.

.. code-block:: bash

    #!/bin/bash

    # Get the pid of nautilus
    nautilus_pid=$(pgrep -u $LOGNAME -n nautilus)

    # If nautilus isn't running, just exit silently
    if [ -z "$nautilus_pid" ]; then
    exit 0
    fi

    # Grab the DBUS_SESSION_BUS_ADDRESS variable from nautilus's environment
    eval $(tr '\0' '\n' < /proc/$nautilus_pid/environ | grep '^DBUS_SESSION_BUS_ADDRESS=')

    # Check that we actually found it
    if [ -z "$DBUS_SESSION_BUS_ADDRESS" ]; then
    echo "Failed to find bus address" >&2
    exit 1
    fi

    # export it so that child processes will inherit it
    export DBUS_SESSION_BUS_ADDRESS

And it comes from `here <http://ubuntuforums.org/showthread.php?p=10148738#post10148738>`_.

A sync takes about 20s + the upload time on my machine, which stay acceptable for 
all of my developments.
