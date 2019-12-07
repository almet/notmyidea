# -*- coding: utf-8 -*-

PATH = "content"
AUTHOR = u"Alexis Métaireau"
SITENAME = u"Alexis - Carnets en ligne"
THEME = "theme"
DISQUS_SITENAME = "notmyidea"
STATIC_PATHS = ["static", "images"]

SITEURL = ""
RELATIVE_URLS = True

TIMEZONE = "Europe/Paris"
LOCALE = "fr_FR.utf8"

DEFAULT_DATE_FORMAT = "%d %B %Y"
LINKS = [
    ("Code", "https://github.com/almet"),
]

PLUGIN_PATHS = ["."]
PLUGINS = [
    "simplereader",
]

CACHE_OUTPUT_DIRECTORY = "cache"
CACHE_DOMAIN = "/cache/"
