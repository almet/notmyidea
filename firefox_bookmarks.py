from pelican import signals

"""
Author 	: Jay Rambhia
email 	: jayrambhia777@gmail.com
Git 	: https://github.com/jayrambhia
gist 	: https://gist.github.com/jayrambhia
=============================================
Name	: bookmarkFirefox
Repo    : Bookmark-Manager
Git     : https://github.com/jayrambhia/Bookmark-Manager
version	: 0.2
"""

import os
import json
import lz4


def fetch_bookmarks(path):
    '''
    Decodes browser bookmark backup files using json
    Returns a dictionary with bookmark url as key and (title, tag, add_date) tuple as value
    '''
    files = os.listdir(path)
    files.sort()
    filename = os.path.join(path, files[-1])

    with open(filename) as f:
        if f.read(8) != b"mozLz40\0":
            print("unable to uncompress bookmarks")
        database = json.loads(lz4.block.decompress(f.read()))
    # Get Bookmarks Menu / Bookmarks toolbar / Tags / Unsorted Bookmarks
    for category in database['children']:
        if 'root' in category and category['root'] == 'unfiledBookmarksFolder':
            bookmarks = category['children']
            return bookmarks


def fetch_firefox_bookmarks(generators):
    gen = generators[0]
    if 'FIREFOX_BOOKMARKS_PATH' in gen.settings:
        gen.context['bookmarks'] = fetch_bookmarks(gen.settings['FIREFOX_BOOKMARKS_PATH'])


def register():
    signals.all_generators_finalized.connect(fetch_firefox_bookmarks)
