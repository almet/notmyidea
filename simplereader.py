from pelican import signals
from pelican.readers import MarkdownReader, Category
from pelican.utils import get_date, slugify

import os.path


class SimpleReader(MarkdownReader):
    enabled = True

    file_extensions = ["md"]

    def __init__(self, *args, **kwargs):
        super(SimpleReader, self).__init__(*args, **kwargs)
        self.settings["MARKDOWN"]["extensions"].append("markdown.extensions.toc")

    def read(self, filename):
        content, metadata = super(SimpleReader, self).read(filename)
        # Get the title from the first h1
        if "title" not in metadata and len(self._md.toc_tokens):
            first_title = self._md.toc_tokens[0]
            metadata["title"] = first_title["name"]
            content = content.replace(
                '<h1 id="{id}">{name}</h1>'.format(**first_title), ""
            )

        # Get the date from the filename.
        parts = os.path.splitext(os.path.basename(filename))[0].split("-")
        if len(parts) >= 3:
            metadata["date"] = get_date("-".join(parts[:3]))

        if "slug" not in metadata:
            metadata["slug"] = slugify(
                metadata["title"], self.settings.get("SLUG_REGEX_SUBSTITUTIONS", [])
            )

        category = os.path.basename(os.path.abspath(os.path.join(filename, os.pardir)))
        metadata["category"] = self.process_metadata("category", category)
        return content, metadata


def add_reader(readers):
    readers.reader_classes["md"] = SimpleReader


# This is how pelican works.
def register():
    signals.readers_init.connect(add_reader)
