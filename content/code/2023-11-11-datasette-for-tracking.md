---
title: Using Datasette for tracking my professional activity
tags: Datasette, Graphs, SQL
---

I've been following Simon Willison since quite some time, but I've actually never played with his main project [Datasette](https://datasette.io) before.

As I'm going back into development, I'm trying to track where my time goes, to be able to find patterns, and just remember how much time I've worked on such and such project. A discussion with [Thomas](https://thom4.net/) made me realize it would be nice to track all this in a spreadsheet of some sort, which I was doing until today.

Spreadsheets are nice, but they don't play well with rich content, and doing graphs with them is kind of tricky. So I went ahead and setup everything in Datasette.

First of all, I've imported my `.csv` file into a sqlite database: 
```bash
sqlite3 -csv -header db.sqlite ".import journal.csv journal"
```

Then, I used [sqlite-utils](https://sqlite-utils.datasette.io/en/stable/) to do some tidying and changed the columns names:

```bash
# Rename a column
sqlite-utils transform journal --rename "quoi ?" content

# Make everything look similar
sqlite-utils update db.sqlite journal project 'value.replace("Umap", "uMap")'
```

Here is my database schema:

```bash
sqlite-utils schema db.sqlite
CREATE TABLE "journal" (
   [date] TEXT,
   [project] TEXT,
   [duration] TEXT,
   [where] TEXT,
   [content] TEXT,
   [paid_work] INTEGER
);
```

And then installed datasette, with a few plugins, and ran it:

```bash
pipx install datasette
datasette install datasette-render-markdown datasette-write-ui datasette-dashboards datasette-dateutil
```

I then came up with a few SQL queries which are useful:

How much I've worked per project:

```SQL
sqlite-utils db.sqlite "SELECT project, SUM(CAST(duration AS REAL)) as total_duration FROM journal GROUP BY project;"
[{"project": "Argos", "total_duration": XX},
 {"project": "IDLV", "total_duration": XX},
 {"project": "Notmyidea", "total_duration": XX},
 {"project": "Sam", "total_duration": XX},
 {"project": "uMap", "total_duration": XX}]
```

How much I've worked per week, in total (I've redacted the results for privacy):

```SQL
sqlite-utils db.sqlite "SELECT strftime('%Y-W%W', date) AS week, SUM(CAST(duration AS REAL)) AS hours FROM journal GROUP BY week ORDER BY week;"

[{"week": "2023-W21", "hours": XX},
 {"week": "2023-W22", "hours": XX},
 {"week": "2023-W23", "hours": XX},
 {"week": "2023-W25", "hours": XX},
 {"week": "2023-W29", "hours": XX},
 {"week": "2023-W37", "hours": XX},
 {"week": "2023-W39", "hours": XX},
 {"week": "2023-W40", "hours": XX},
 {"week": "2023-W41", "hours": XX},
 {"week": "2023-W42", "hours": XX},
 {"week": "2023-W44", "hours": XX},
 {"week": "2023-W45", "hours": XX}]
```

I then created a quick dashboard using [datasette-dashboard](https://github.com/rclement/datasette-dashboards), which looks like this:

![Capture d'écran du dashboard, heures par semaine](/images/datasette/hours-per-week.png)
![Capture d'écran du dashboard, heures par projet](/images/datasette/hours-per-project.png)

Using this configuration:

```yaml
plugins:
  datasette-render-markdown:
    columns:
      - "content"
  datasette-dashboards:
    my-dashboard:
      title: Notmyidea
      filters:
        project:
          name: Projet
          type: select
          db: db
          query: SELECT DISTINCT project FROM journal WHERE project IS NOT NULL ORDER BY project ASC
      layout:
        - [hours-per-project]
        - [entries]
        - [hours-per-week]
      charts:
        hours-per-project:
          title: Nombre d'heures par projet
          query: SELECT project, SUM(CAST(duration AS REAL)) as total FROM journal GROUP BY project;
          db: db
          library: vega-lite
          display:
            mark: { type: arc, tooltip: true }
            encoding:
              color: { field: project, type: nominal }
              theta: { field: total, type: quantitative }
        hours-per-week:
          title: Heures par semaine
          query: SELECT strftime('%Y-W%W', date) AS week, SUM(CAST(duration AS REAL)) AS hours FROM journal GROUP BY week ORDER BY week;
          db: db
          library: vega-lite
          display:
            mark: { type: bar, tooltip: true }
            encoding:
              x: { field: week, type: ordinal}
              y: { field: hours, type: quantitative }

        entries:
          title: Journal
          db: db
          query: SELECT * FROM journal WHERE TRUE [[ AND project = :project ]] ORDER BY date DESC
          library: table
          display:
```

And ran datasette with:

```bash
datasette db.sqlite --root --metadata metadata.yaml
```