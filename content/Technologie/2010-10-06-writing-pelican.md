# Pelican, a simple static blog generator in python


Those days, I've wrote a little python application to fit my blogging
needs. I'm an occasional blogger, a vim lover, I like restructured text
and DVCSes, so I've made a little tool that makes good use of all that.

[Pelican](http://docs.getpelican.com) (for calepin) is just a simple
tool to generate your blog as static files, letting you using your
editor of choice (vim\!). It's easy to extend, and has a template
support (via jinja2).

I've made it to fit *my* needs. I hope it will fit yours, but maybe it
wont, and it have not be designed to feet everyone's needs.

Need an example ? You're looking at it \! This weblog is using pelican
to be generated, also for the atom feeds.

I've released it under AGPL, since I want all the modifications to be
profitable to all the users.

You can find a repository to fork at
<https://github.com/getpelican/pelican/>. feel free to hack it \!

If you just want to get started, use your installer of choice (pip,
easy\_install, …) And then have a look to the help (pelican --help)

```
$ pip install pelican
```

## Usage

Here's a sample usage of pelican

``` bash
$ pelican .
writing /home/alexis/projets/notmyidea.org/output/index.html
writing /home/alexis/projets/notmyidea.org/output/tags.html
writing /home/alexis/projets/notmyidea.org/output/categories.html
writing /home/alexis/projets/notmyidea.org/output/archives.html
writing /home/alexis/projets/notmyidea.org/output/category/python.html
writing
/home/alexis/projets/notmyidea.org/output/pelican-a-simple-static-blog-generator-in-python.html
Done !
```

You also can use the --help option for the command line to get more
informations

```bash

$pelican --help
usage: pelican [-h] [-t TEMPLATES] [-o OUTPUT] [-m MARKUP] [-s SETTINGS] [-b]
               path

A tool to generate a static blog, with restructured text input files.

positional arguments:
  path                  Path where to find the content files (default is
                        "content").

optional arguments:
  -h, --help            show this help message and exit
  -t TEMPLATES, --templates-path TEMPLATES
                        Path where to find the templates. If not specified,
                        will uses the ones included with pelican.
  -o OUTPUT, --output OUTPUT
                        Where to output the generated files. If not specified,
                        a directory will be created, named "output" in the
                        current path.
  -m MARKUP, --markup MARKUP
                        the markup language to use. Currently only
                        ReSTreucturedtext is available.
  -s SETTINGS, --settings SETTINGS
                        the settings of the application. Default to None.
  -b, --debug
```

Enjoy :)
