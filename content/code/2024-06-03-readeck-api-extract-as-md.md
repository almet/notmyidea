---
title: Generating my weeknotes quotes with jq and readeck
tags: readeck, jq, markdown
status: draft
---

I've installed [readeck](https://readeck.org/en/) to track the articles I read,
and I'm currently trying to make it a database for the quotes I do. Because
there is a nice Firefox addon I hope it will be convenient to use.

Readeck proposes an API to retrieve the data it stores, and I wanted to leverage
it to build [my weeknotes](/weeknotes) citations.

The API provided is very easy to query, and returns JSON:

```bash

curl -X GET "https://readeck.notmyidea.org/api/bookmarks/annotations" -H "accept: application/json" -H "authorization: Bearer <redacted>" | jq
```

Returns:
  
```json
[
  {
    "id": "RpgpsT2ZijHsbiwX9fL3He",
    "href": "http://readeck.notmyidea.org/api/bookmarks/fJ6SRgbUJXdNt3QGrvb2aP/annotations/RpgpsT2ZijHsbiwX9fL3He",
    "text": "Fourth, power matters. AI is a technology that fundamentally magnifies power of the humans who use it, but not equally across users or applications. Can we build systems that reduce power imbalances rather than increase them? Think of the privacy versus surveillance debate in the context of AI.",
    "created": "2024-06-02T22:16:46.80538957+02:00",
    "bookmark_id": "fJ6SRgbUJXdNt3QGrvb2aP",
    "bookmark_href": "http://readeck.notmyidea.org/api/bookmarks/fJ6SRgbUJXdNt3QGrvb2aP",
    "bookmark_url": "https://www.schneier.com/blog/archives/2024/05/how-ai-will-change-democracy.html",
    "bookmark_title": "How AI Will Change Democracy",
    "bookmark_site_name": "Schneier on Security"
  },
  ...
]
```

From there, turning this to markdown was this [jq](https://jqlang.github.io/jq/manual/) filter:

```json
.[] | "> \(.text) \n> \n> — [\(.bookmark_title)](\(.bookmark_url))\n"
```

Using `jq -r` to output as raw output, I get the quote I'm looking for:

```markdown

> Fourth, power matters. AI is a technology that fundamentally magnifies power of the humans who use it, but not equally across users or applications. Can we build systems that reduce power imbalances rather than increase them? Think of the privacy versus surveillance debate in the context of AI.
> 
> — [How AI Will Change Democracy](https://www.schneier.com/blog/archives/2024/05/how-ai-will-change-democracy.html)  
```

Because I write these notes every week, I'm only interested in the content of the last week.

Here is how to get "last-week-date" on MacOS:

```bash
date -v-7d +"%Y-%m-%d"
```

And I can filter with:

```bash
jq --arg date $(date -v-7d +"%Y-%m-%d") '.[] | select(.created > $date)'
```

Putting it all together, I have the following line:

```bash

curl -X GET "https://readeck.notmyidea.org/api/bookmarks/annotations" -H "accept: application/json" -H "authorization: Bearer <redacted>" \
| jq -r --arg date $(date -v-7d +"%Y-%m-%d") \
 '.[] | select(.created > $date) | "> \\(.text) \\n> \\n> — [\\(.bookmark_title)](\\(.bookmark_url))\\n"'  
```

I feel like a hairy monster, but an happy one.
