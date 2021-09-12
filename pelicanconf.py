# -*- coding: utf-8 -*-

PATH = "content"
AUTHOR = u""
SITENAME = u"Alexis Métaireau"
THEME = "mnmlist"
DISQUS_SITENAME = "notmyidea"
DEFAULT_PAGINATION = 10
STATIC_PATHS = ["images", "docs"]

SITEURL = ""
RELATIVE_URLS = True

TIMEZONE = "Europe/Paris"
LOCALE = "fr_FR.utf8"

DEFAULT_DATE_FORMAT = "%d %B %Y"
LINKS = []

PLUGIN_PATHS = ["."]
PLUGINS = [
    "simplereader",
]

CACHE_OUTPUT_DIRECTORY = "cache"
CACHE_DOMAIN = "/cache/"
TYPOGRIFY = True
