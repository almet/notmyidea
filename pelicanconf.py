# -*- coding: utf-8 -*-

PATH = "content"
SITENAME = "(not my) ideas"
AUTHOR = ""
THEME = "mnmlist"
STATIC_PATHS = ["images", "audio", "extra", "docs"]
STYLESHEET_URL = "/theme/css/main.css"
EXTRA_PATH_METADATA = {
    "extra/keybase.txt": {"path": "keybase.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/android-chrome-192x192.png": {"path": "android-chrome-192x192.png"},
    "extra/android-chrome-512x512.png": {"path": "android-chrome-512x512.png"},
    "extra/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
    "extra/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "extra/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "extra/robots.txt": {"path": "robots.txt"},
}

FORMATTED_FIELDS = "contraintes"

SITEURL = ""
RELATIVE_URLS = True

TIMEZONE = "Europe/Paris"
LOCALE = "fr_FR"

TAG_FEED_ATOM = "feeds/tags/{slug}.atom.xml"

DEFAULT_DATE_FORMAT = "%d %B %Y"
LINKS = []

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["simplereader", "isbn_downloader", "neighbors"]

CACHE_OUTPUT_DIRECTORY = "cache"
CACHE_DOMAIN = "/cache/"
TYPOGRIFY = True
INDEX_SAVE_AS = "index.html"

CATEGORY_SAVE_AS = "{slug}/index.html"
CATEGORY_URL = "{slug}/"

MENU = [
    # ("Journal", "/journal/index.html", "journal"),
    # ("Code", "/code/", "code"),
    # ("Notes hebdo", "/weeknotes/", "weeknotes"),
    # ("Lectures", "/lectures/", "lectures"),
    # ("Projets", "/projets.html", "projets"),
    # ("Écriture", "/ecriture", "ecriture"),
]

FOOTERITEMS = [
    ("Pro", "/projets/"),
]

CATEGORIES_DESCRIPTION = {
    "weeknotes": (
        "Notes hebdo",
        "Chaque semaine, je fais un petit résumé de ce qui s'est passé. Cela m'aide à garder le fil de mes idées et de mes différents projets. Un bon moyen de faire une pause et d'observer la semaine sous un autre angle.",
    ),
    "lectures": (
        "Notes de lecture",
        "Quelques notes prises au détour d'une lecture, plutôt pour ne pas les oublier et me remémorer le livre quand j'en ai besoin.",
    ),
    "code": (
        "Code",
        "Des bouts de trucs liés au code, que je trouve utiles de stocker quelque part (en anglais)",
    ),
    "journal": (
        "Journal",
        "Quelques réfléxions, bien souvent autour du monde du travail ou de la technologie.",
    ),
    "notes": (
        "Notes",
        "Prises bien souvent en regardant une vidéo ou un article en ligne. Je les mets ici pour pouvoir les retrouver quand le besoin se fait sentir.",
    ),
    "ecriture": (
        "Écriture",
        "Textes rédigés lors d'ateliers d'écriture",
    ),
}
