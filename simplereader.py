import os.path
from datetime import datetime

from datefinder import find_dates
from markdown.preprocessors import Preprocessor
from pelican import signals
from pelican.readers import Category, Markdown, MarkdownReader, pelican_open
from pelican.utils import get_date, slugify


class BlockquotesPreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        for line in lines:
            if line.startswith(">"):
                # new_lines.append("&nbsp;")
                new_lines.append(line)
            else:
                new_lines.append(line)
        return new_lines


class SimpleReader(MarkdownReader):
    enabled = True

    file_extensions = ["md"]

    def __init__(self, *args, **kwargs):
        super(SimpleReader, self).__init__(*args, **kwargs)
        self.settings["MARKDOWN"]["extensions"].append("markdown.extensions.toc")

    def read(self, source_path):
        self._source_path = source_path
        self._md = Markdown(**self.settings["MARKDOWN"])
        if "Lectures" in source_path:
            self._md.preprocessors.register(
                BlockquotesPreprocessor(self._md), "blockquotes", 10
            )

        with pelican_open(source_path) as text:
            content = self._md.convert(text)

        if hasattr(self._md, "Meta"):
            metadata = self._parse_metadata(self._md.Meta)
        else:
            metadata = {}

        # Add the TOC to the metadata.
        if len(self._md.toc) > 300:
            metadata["table_of_contents"] = self._md.toc

        # Get the title from the first h1
        if "title" not in metadata and len(self._md.toc_tokens):
            first_title = self._md.toc_tokens[0]
            metadata["title"] = first_title["name"]
            content = content.replace(
                '<h1 id="{id}">{name}</h1>'.format(**first_title), ""
            )

        # Get the date from the filename, if possible.
        parts = os.path.splitext(os.path.basename(source_path))[0].split("-")
        if len(parts) > 3:
            metadata["date"] = get_date("-".join(parts[:3]))

        if "slug" not in metadata:
            metadata["slug"] = slugify(
                metadata["title"], self.settings.get("SLUG_REGEX_SUBSTITUTIONS", [])
            )

        category = os.path.basename(
            os.path.abspath(os.path.join(source_path, os.pardir))
        )
        metadata["category"] = self.process_metadata("category", category)
        return content, metadata


def add_reader(readers):
    readers.reader_classes["md"] = SimpleReader


# This is how pelican works.
def register():
    signals.readers_init.connect(add_reader)
