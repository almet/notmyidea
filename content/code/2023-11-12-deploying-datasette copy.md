---
title: Deploying and customizing datasette
headline: Step by step follow-up on how I've deployed it and added custom templates on top.
tags: Datasette, Deployment
---

First, create the venv and install everything

```bash
# Create and activate venv
python3 -m venv venv
source venv/bin/activate

# Install datasette…
pip install datasette

# … and the plugins
datasette install datasette-render-markdown datasette-dashboards datasette-dateutil
```

I was curious how much all of this was weighting. 30MB seems pretty reasonable to me.

```bash
# All of this weights 30Mb
du -sh venv
30M	venv
```

## Adding authentication

Datasette doesn't provide authentication by default, so [you have to use a plugin for this](https://docs.datasette.io/en/stable/authentication.html). I'll be using [Github authentication](https://github.com/simonw/datasette-auth-github) for now as it seems simple to add:

```
pip install datasette-auth-github
```

I've had to create a new github application and export the variables to my server, and add some configuration to my `metadata.yaml` file:

```yaml
allow:
  gh_login: almet

plugins:
  datasette-auth-github:
    client_id:
      "$env": GITHUB_CLIENT_ID
    client_secret:
      "$env": GITHUB_CLIENT_SECRET
```

If that's useful to you, here is [the git repository](https://gitlab.com/almet/timetracker-datasette-deploy
) I'm deploying to my server.

## Using templates

Okay, I now want to be able to send an URL to the people I'm working with, on which they can see what I've been doing, and what I've been using my time on.

It was pretty simple to do, and kind of weird to basically do what I've been doing back in the days for my first PHP applications : put SQL statements in the templates ! heh.

I've added a template with what I want to do. It has the side-effect of being able to propose a read-only view to a private database.

```html
<h1>{{project}}
    {% for row in sql("SELECT SUM(CAST(duration AS REAL)) as total_hours FROM journal WHERE project = '" + project + "';", database="db") %}
({{ row["total_hours"] }} heures)
{% endfor %}
</h1>
<dl>
    {% for row in sql("select date, CAST(duration AS REAL) as duration, content from journal where project = '" + project + "' order by date DESC", database="db") %}
        <dt>{{ row["date"] }} ({{ row["duration"] }} heures)</dt>
        <dd>{{ render_markdown(row["content"]) }}</dd>
    {% endfor %}
</dl>
```

Which looks like this :

![Alt text](/images/datasette/custom-template.png)