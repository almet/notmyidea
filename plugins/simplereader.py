import locale
import os.path
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from markdown.preprocessors import Preprocessor

from pelican import signals
from pelican.readers import Markdown, MarkdownReader, pelican_open
from pelican.utils import get_date, slugify

try:
    locale.setlocale(locale.LC_TIME, "fr_FR.UTF8")
except Exception:
    locale.setlocale(locale.LC_TIME, "fr_FR")


class WorklogPreprocessor(Preprocessor):
    pattern = re.compile(
        r"""
        (?:(\w+)\s+)?                   # Day name
        (\d{1,2})\s+                    # Day number
        ([\wéû]+)\s+                    # Month name
        (\d{4})\s+                      # Year
        \(
        (\d{1,2})h                      # Hours (mandatory)
        (?:\s+facturées)?               # Optionally 'facturées', if not present, assume hours are 'facturées'
        (?:,\s*(\d{1,2})h\s*bénévoles)? # Optionally 'volunteer hours 'bénévoles'
        ,?                              # An optional comma
        \s*                             # Optional whitespace
        (?:fun\s+)?                     # Optionally 'fun' (text) followed by whitespace
        (\d)/5                          # Happiness rating (mandatory, always present)
        \)                              # Closing parenthesis
        """,
        re.VERBOSE | re.UNICODE,
    )

    def __init__(self, *args, **kwargs):
        self.data = {}
        self.monthly_hours = defaultdict(lambda: defaultdict(int))
        super().__init__(*args, **kwargs)

    def run(self, lines):
        new_lines = []
        for line in lines:
            if line.startswith("##"):
                match = re.search(self.pattern, line)
                if not match:
                    raise ValueError("Unable to parse worklog title", line)
                (
                    day_of_week,
                    day,
                    month,
                    year,
                    payed_hours,
                    volunteer_hours,
                    happiness,
                ) = match.groups()

                volunteer_hours = int(
                    volunteer_hours) if volunteer_hours else 0
                payed_hours = int(payed_hours)
                happiness = int(happiness)
                date = datetime.strptime(f"{day} {month} {year}", "%d %B %Y")
                self.data[date.strftime("%Y-%m-%d")] = {
                    "payed_hours": payed_hours,
                    "volunteer_hours": volunteer_hours,
                    "happiness": happiness,
                }
                current_date = date.strftime("%Y/%m")
                self.monthly_hours[current_date]['payed'] += payed_hours
                self.monthly_hours[current_date]['volunteered'] += volunteer_hours
                displayed_date = date.strftime("%A %d %B %Y")

                # Replace the line with just the date
                new_lines.append(f"## 🗓️ {displayed_date}")
            else:
                new_lines.append(line)
        return new_lines

    def compute_data(self, metadata):
        """Do the operations on the data.

        This is run once, after everything has been parsed
        """
        payed_hours = sum([item["payed_hours"] for item in self.data.values()])
        volunteer_hours = sum([item["volunteer_hours"]
                              for item in self.data.values()])

        data = dict(
            data=self.data,
            payed_hours=payed_hours,
            volunteer_hours=volunteer_hours,
            monthly_hours=self.monthly_hours,
            template="worklog",
        )
        if "total_days" in metadata:
            total_hours = int(metadata["total_days"]) * 7
            data.update(
                dict(
                    total_hours=total_hours,
                    percentage=round(payed_hours / total_hours * 100),
                )
            )

        return data


class SimpleReader(MarkdownReader):
    enabled = True

    file_extensions = ["md"]

    def __init__(self, *args, **kwargs):
        super(SimpleReader, self).__init__(*args, **kwargs)
        self.settings["MARKDOWN"]["extensions"].append(
            "markdown.extensions.toc")
        self.settings["MARKDOWN"]["extension_configs"].update(
            {'markdown.extensions.toc': {'toc_depth': 3}})

    def read(self, source_path):
        self._source_path = source_path
        self._md = Markdown(**self.settings["MARKDOWN"])

        is_worklog = Path(source_path).parent.match("pages/worklog")

        if is_worklog:
            worklog = WorklogPreprocessor(self._md)
            self._md.preprocessors.register(worklog, "worklog", 20)

        with pelican_open(source_path) as text:
            content = self._md.convert(text)

        if hasattr(self._md, "Meta"):
            metadata = self._parse_metadata(self._md.Meta)
        else:
            metadata = {}

        # Add the worklog info to the metadata
        if is_worklog:
            metadata["worklog"] = worklog.compute_data(metadata)

        # Add the TOC to the metadata.
        if len(self._md.toc) > 300:
            metadata["table_of_contents"] = self._md.toc

        # Get the title from the first title
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
                metadata["title"], self.settings.get(
                    "SLUG_REGEX_SUBSTITUTIONS", [])
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
