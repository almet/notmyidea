import json
import os
import sqlite3
import subprocess

import click

DATABASE = "quotes.db"


def recreate_database(db_path):
    if os.path.exists(db_path):
        os.remove(db_path)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("CREATE TABLE quotes (id INTEGER PRIMARY KEY, content TEXT)")
    conn.commit()
    return conn


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


def insert_quotes_to_db(conn, quotes):
    cur = conn.cursor()
    for quote in quotes:
        cur.execute("INSERT INTO quotes (content) VALUES (?)", (quote,))
    conn.commit()


@click.command()
@click.argument("input_markdown_file", type=click.Path(exists=True))
@click.argument("clusters", type=int)
def main(input_markdown_file, clusters):
    """Process Markdown files and generate output with clustered quotes."""
    conn = recreate_database(DATABASE)
    quotes = extract_quotes(input_markdown_file)
    insert_quotes_to_db(conn, quotes)

    subprocess.run(
        [
            "llm",
            "embed-multi",
            "quotes",
            "-d",
            DATABASE,
            "--sql",
            "SELECT id, content FROM quotes WHERE content <> ''",
            "--store",
        ],
        capture_output=True,
        text=True,
    )

    cluster_result = subprocess.run(
        [
            "llm",
            "cluster",
            "quotes",
            str(clusters),
            "-d",
            DATABASE,
            "--summary",
            "--prompt",
            "Titre pour l'ensemble de ces citations (court)",
        ],
        capture_output=True,
        text=True,
    )

    if cluster_result.returncode == 0:
        cluster_data = json.loads(cluster_result.stdout)
    else:
        click.echo("Clustering failed:", err=True)
        click.echo(cluster_result.stderr, err=True)
        conn.close()
        return

    for group in cluster_data:
        summary = group["summary"]
        item_ids = [item["id"] for item in group["items"]]

        print(f"## {summary}\n\n")

        for item_id in item_ids:
            try:
                cur = conn.cursor()
                cur.execute("SELECT content FROM quotes WHERE id=?", (item_id,))
                quote = cur.fetchone()
                if quote:
                    print(f"{quote[0]}\n\n")
                else:
                    click.echo(f"> Quote with ID {item_id} not found.\n\n", err=True)
            except sqlite3.Error as e:
                click.echo(
                    f"> Error fetching quote with ID {item_id}: {e}\n\n", err=True
                )

    conn.close()


if __name__ == "__main__":
    main()
