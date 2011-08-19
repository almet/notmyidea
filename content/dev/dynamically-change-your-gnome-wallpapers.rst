Dynamically change your gnome desktop wallpaper
###############################################

:date: 2010-10-11

In gnome, you can can use a XML file to have a dynamic wallpaper.
It's not so easy, and you can't just tell: use the pictures in this folder to do
so.

You can have a look to the git repository if you want: http://github.com/ametaireau/gnome-background-generator

Some time ago, I've made a little python script to ease that, and you can now
use it too. It's named "gnome-background-generator", and you can install it via
pip for instance.

.. code-block:: shell

   $ pip install gnome-background-generator

Then, you have just to use it this way:

.. code-block:: shell

    $ gnome-background-generator -p ~/Images/walls -s
    /home/alexis/Images/walls/dynamic-wallpaper.xml generated

Here is a extract of the `--help`:

.. code-block:: shell

    $ gnome-background-generator --help
    usage: gnome-background-generator [-h] [-p PATH] [-o OUTPUT]
                                      [-t TRANSITION_TIME] [-d DISPLAY_TIME] [-s]
                                      [-b]

    A simple command line tool to generate an XML file to use for gnome
    wallpapers, to have dynamic walls

    optional arguments:
      -h, --help            show this help message and exit
      -p PATH, --path PATH  Path to look for the pictures. If no output is
                            specified, will be used too for outputing the dynamic-
                            wallpaper.xml file. Default value is the current
                            directory (.)
      -o OUTPUT, --output OUTPUT
                            Output filename. If no filename is specified, a
                            dynamic-wallpaper.xml file will be generated in the
                            path containing the pictures. You can also use "-" to
                            display the xml in the stdout.
      -t TRANSITION_TIME, --transition-time TRANSITION_TIME
                            Time (in seconds) transitions must last (default value
                            is 2 seconds)
      -d DISPLAY_TIME, --display-time DISPLAY_TIME
                            Time (in seconds) a picture must be displayed. Default
                            value is 900 (15mn)
      -s, --set-background  '''try to set the background using gnome-appearance-
                            properties
      -b, --debug
