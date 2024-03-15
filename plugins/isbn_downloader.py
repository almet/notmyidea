import logging
import os
from pathlib import Path

import requests
from pelican import log, signals

log = logging.getLogger(__name__)


def check_or_download_image(isbn, output_dir):
    log.info(f"Downloading cover for {isbn=}")

    output_dir = Path(output_dir)
    # remote_url = f"https://images.isbndb.com/covers/41/83/{isbn}.jpg"
    image_relative_path = f"images/isbn-covers/{isbn}.jpg"
    image_path = output_dir / image_relative_path

    if image_path.exists():
        return image_relative_path
    else:
        try:
            remote_url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
            api_resp = requests.get(remote_url)
            api_resp.raise_for_status()

            returned = api_resp.json()
            if returned["totalItems"] > 0:
                thumbnail_url = returned["items"][0]["volumeInfo"]["imageLinks"][
                    "thumbnail"
                ]
                response = requests.get(thumbnail_url, stream=True)

                os.makedirs(os.path.dirname(image_path), exist_ok=True)

                with open(image_path, "wb") as fp:
                    for chunk in response.iter_content(chunk_size=8192):
                        fp.write(chunk)

                return image_relative_path
        except:
            log.error(
                f"No ISBN cover found for {isbn=}. Look at https://isbnsearch.org/isbn/{isbn}"
            )
            return


def run_for_each_article(generator):
    for article in generator.articles:
        isbn = getattr(article, "isbn", None)
        if isbn:
            isbn = isbn.replace("-", "")
            article.isbn_cover = check_or_download_image(isbn, generator.path)


def register():
    signals.article_generator_finalized.connect(run_for_each_article)
