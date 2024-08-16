---
title: Categorizing book quotes in clusters
tags: llm, markdown, clusters, sqlite
---

When I'm reading a theory book, oftentimes I'm taking notes: it helps me remember the contents, make it easier to get back to it later on, and overall it helps me organize my thoughts.

I was looking for an excuse to use LLM embeddings, to better understand what they are and how they work, so I took a stab at categorizing the quotes I have in different groups (named clusters).

Here is what I did:

1. Extract the quotes from the markdown files, and put them in a sqlite database ;
2. Create an embedding for each of the quotes. Embeddings are a binary representation of the content, and can be used to compare with other contents.
3. Run a [K-nearest neighbors (k-NN)](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) algorithm on it, to find the groups.
4. Organize these quotes in a new markdown document

I went with the [llm](https://llm.datasette.io/) command line tool with the `embed-multi` feature and the [`llm cluster` plugin](https://github.com/simonw/llm-cluster) to group the notes together, and I wrote a python script to glue everything together.

In the end, I'm happy to have learnt how to make this work, but… the end results aren't as good as I expected it to be, unfortunately. Maybe that's because creating these clusters is where I actually learn, and automating it doesn't bring much value to me.

Grouping the quotes manually, removing the ones repeating themselves seems to lead to a more precise and "to the point" document.

That being said, here's how I did it. The main reason was to understand how it works!:

## Extracting quotes from markdown files

First, I extracted the quotes and put them in a local sqlite database. Here is a python script I used:

```python
def extract_quotes(input_file):
    with open(input_file, "r") as file:
        quote_lines = []
        quotes = []
        for line in file:
            if line.startswith(">"):
                quote_lines.append(line)
            else:
                if quote_lines:
                    quote = "\n".join(quote_lines).strip()
                    quotes.append(quote)
                    quote_lines = []
    return quotes
```

This is reading lines and grouping together the ones starting with a `>`. I'm not even using a Markdown parser here. I went with python because it seemed easier to get multi-line quotes.

Then, I insert all the quotes in a local database:

```python
def recreate_database(db_path):
    if os.path.exists(db_path):
        os.remove(db_path)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("CREATE TABLE quotes (id INTEGER PRIMARY KEY, content TEXT)")
    conn.commit()
    return conn
```

Once the sqlite database created, insert each quote in it:

```python
def insert_quotes_to_db(conn, quotes):
    cur = conn.cursor()
    for quote in quotes:
        cur.execute("INSERT INTO quotes (content) VALUES (?)", (quote,))
    conn.commit()
```

Bringing everything together like this:

```python
@click.command()
@click.argument("input_markdown_file", type=click.Path(exists=True))
def main(input_markdown_file):
    """Process Markdown files and generate output with clustered quotes."""
    conn = recreate_database("quotes.db")
    quotes = extract_quotes(input_markdown_file)
    insert_quotes_to_db(conn, quotes)
```

Alternatively, you can create the database with `sqlite-utils` and populate it with a loop (but multi-lines quotes aren't taken into account. Python wins.):

```bash
sqlite-utils create-table quotes.db quotes id integer content text --pk=id --replace

grep '^>' "$INPUT_MARKDOWN_FILE" | while IFS= read -r line; do
  echo "$line" | jq -R '{"content": . }' -j | sqlite-utils insert quotes.db quotes -
done
```

---

## Getting the clusters

That's really where the "magic" happens. Now that we have our local database, we can use `llm` to create the embeddings, and then the clusters:

```bash
llm embed-multi quotes -d quotes.db --sql "SELECT id, content FROM quotes WHERE content <> ''" --store
```

Avoiding the empty lines is mandatory, otherwise the OpenAI API is failing without much explanation (unless I missed it, at the moment `llm` doesn't generate embeddings with local models). It actually took me some time to figure out why the API calls were failing.

Then, we generate the clusters and the summaries:

```bash
llm cluster quotes 5 -d quotes.db --summary --prompt "Titre court pour l'ensemble de ces citations"
```

Which outputs us something like this:

```json
[
  {
    "id": "0",
    "items": [
      {
        "id": "1",
        "content": "> En se contentant de leur coller l'\u00e9tiquette d'oppresseurs et de les rejeter, nous \u00e9vitions de mont"
      },
      {
        "id": "10",
        "content": "> Toute personne qui essaie de vivre l'amour avec un partenaire d\u00e9pourvu de conscience affective sou"
      },
      // <snip>
    ],
    "summary": "Dynamiques émotionelles dans les relations genrées"
  },
  // etc.
]
```

## Output as markdown

The last part is to put back everything together in a the `STDOUT`. It's a simple loop which does a lookup in the database for each item, prints the summary of each group and then the quotes.

You can find [the full script here](/extra/scripts/group-quotes.py), included below:

```python
{!extra/scripts/group-quotes.py!}
```
