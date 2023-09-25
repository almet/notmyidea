# -*- coding: utf-8 -*-

PATH = "content"
AUTHOR = ""
SITENAME = "Alexis Métaireau"
THEME = "mnmlist"
DISQUS_SITENAME = "notmyidea"
DEFAULT_PAGINATION = 3
STATIC_PATHS = ["images", "docs"]

SITEURL = ""
RELATIVE_URLS = True

TIMEZONE = "Europe/Paris"
LOCALE = "fr_FR"

DEFAULT_DATE_FORMAT = "%d %B %Y"
LINKS = []

PLUGIN_PATHS = ["."]
PLUGINS = [
    "simplereader",
]

CACHE_OUTPUT_DIRECTORY = "cache"
CACHE_DOMAIN = "/cache/"
TYPOGRIFY = True
INDEX_SAVE_AS = "articles.html"

CATEGORY_SAVE_AS = "{slug}/index.html"
CATEGORY_URL = "{slug}/"

MENU = [
    ("Alexis Métaireau", "/", "index"),
    ("Journal", "/journal/index.html", "journal"),
    ("Code, etc.", "/code/", "code"),
    ("Notes hebdo", "/weeknotes/", "weeknotes"),
    ("Lectures", "/lectures/", "lectures"),
]

CATEGORIES_DESCRIPTION = {
    "weeknotes": (
        "Notes hebdo",
        "Chaque semaine, je fais un petit résumé de ce qui s'est passé. Cela m'aide à garder le fil de mes idées et de mes différents projets. Un bon moyen de faire un pause et d'observer la semaine sous un autre angle.",
    ),
    "lectures": (
        "Notes de lecture",
        "Quelques notes prises au détour d'une lecture, plutôt pour ne pas les oublier, et me remémorer le livre quand j'en ai besoin.",
    ),
    "code": (
        "Code, etc.",
        "Des bouts de trucs liés au code, que je trouve utiles de stocker quelque part (en anglais)",
    ),
    "journal": (
        "Journal",
        "Quelques pensées partagées, bien souvent sur le monde du travail ou de la technologie.",
    ),
}
