---
title: Using pelican to track my worked and volunteer hours
headline: Graphs, progress-bars and python-markdown extensions
tags: Pelican, Work, Vega, Markdown
---

I was tracking my hours in Datasette ([article](https://blog.notmyidea.org/using-datasette-for-tracking-my-professional-activity.html) and [follow-up](https://blog.notmyidea.org/deploying-and-customizing-datasette.html)), but I wasn't really happy with the editing process.

I've seen [David](https://larlet.fr/david) notes, which made me want to do something similar.

I'm consigning everything in markdown files and as such, was already keeping track of everything this way already. Tracking my hours should be simple otherwise I might just oversee it. So I hacked something together with [pelican](https://github.com/getpelican/pelican) (the software I wrote for this blog).

![A graph showing the worked hours and volunteer hours](/images/pelican/worklog.png)

It's doing the following:

1. Defines a specific format for my worklog entries
2. Parses them (using a regexp), does some computation and ;
3. Uses a specific template to display a graph and progress bar.

## Reading information from the titles

I actually took the format I've been already using in my log, and enhanced it a bit.
Basically, the files look likes this (I'm writing in french):

```markdown
---
title: My project
total_days: 25
---

## Mardi 23 Novembre 2023 (9h, 5/5)

What I did this day.
I can include [links](https://domain.tld) and whatever I want.
It won't be processed.

## Lundi 22 Novembre 2023 (8h rémunérées, 2h bénévoles, 4/5)

Something else.
```

Basically, the second titles (h2) are parsed, and should have the following structure:
`{day_of_week} {day} {month} {year} ({worked_hours}(, optional {volunteer_hours}), {fun_rank})`

The goal here is to retrieve all of this, so I asked ChatGPT for a regexp and iterated on the result which got me:

```python
pattern = re.compile(
        r"""
        (\w+)\s+                      # Day name
        (\d{1,2})\s+                  # Day number
        ([\wéû]+)\s+                  # Month name
        (\d{4})\s+                    # Year
        \(
        (\d{1,2})h                    # Hours (mandatory)
        (?:\s+facturées)?             # Optionally 'facturées', if not present, assume hours are 'facturées'
        (?:,\s*(\d{1,2})h\s*bénévoles)? # Optionally 'volunteer hours 'bénévoles'
        ,?                            # An optional comma
        \s*                           # Optional whitespace
        (?:fun\s+)?                   # Optionally 'fun' (text) followed by whitespace
        (\d)/5                        # Happiness rating (mandatory, always present)
        \)                            # Closing parenthesis
        """,
        re.VERBOSE | re.UNICODE,
    )
```

## The markdown preprocessor

I'm already using a custom pelican plugin, which makes it possible to have pelican behave exactly the way I want. For instance, it's getting the date from the filesystem.

I just had to add some features to it. The way I'm doing this is by [using a custom Markdown reader](https://docs.getpelican.com/en/3.6.2/plugins.html#how-to-create-a-new-reader), on which I add extensions and custom processors.

In my case, I added a preprocessor which will only run when we are handling the worklog. It makes it possible to change what's being read, before the markdown lib actually transforms it to HTML.

Here is the code for it:

```python
class WorklogPreprocessor(Preprocessor):
    pattern = "the regexp we've seen earlier"

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

                volunteer_hours = int(volunteer_hours) if volunteer_hours else 0
                payed_hours = int(payed_hours)
                happiness = int(happiness)

                date = datetime.strptime(f"{day} {month} {year}", "%d %B %Y")
                self.data[date.strftime("%Y-%m-%d")] = {
                    "payed_hours": payed_hours,
                    "volunteer_hours": volunteer_hours,
                    "happyness": happiness,
                }

                # Replace the line with just the date
                new_lines.append(f"## 🗓️ {day_of_week} {day} {month} {year}")
            else:
                new_lines.append(line)
        return new_lines

```
It does the following when it encounters a h2 line:

- try to parse it
- store the data locally
- replace the line with a simpler version
- If if doesn't work, error out.

I've also added some computations on top of it, which makes it possible to display a percentage of completion for the project, if "payed_hours" was present in the metadata, and makes it use a specific template (see later).

```python
def compute_data(self, metadata):
    done_hours = sum([item["payed_hours"] for item in self.data.values()])

    data = dict(
        data=self.data,
        done_hours=done_hours,
        template="worklog",
    )

    if "total_days" in metadata:
        total_hours = int(metadata["total_days"]) * 7
        data.update(
            dict(
                total_hours=total_hours,
                percentage=round(done_hours / total_hours * 100),
            )
        )

    return data
```

## Plugging this with pelican

Here's the code for extending a custom reader, basically adding a pre-processor and adding back its data in the document metadata:

```python

is_worklog = Path(source_path).parent.match("pages/worklog")

if is_worklog:
    worklog = WorklogPreprocessor(self._md)
    self._md.preprocessors.register(worklog, "worklog", 20)

# process the markdown, and then

if is_worklog:
    metadata["worklog"] = worklog.compute_data(metadata)
```

## Adding a graph

Okay, everything is parsed, but it's not yet displayed on the pages. I'm using [vega-lite](https://vega.github.io/vega-lite/docs/) to display a graph.

Here is my template for this (stored in `template/worklog.html`), it's doing a stacked bar chart with my data.

```js
const spec = {
      "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
      "width": 500,
      "height": 200,
      "data": 
        {
          "name": "table",
          "values": [
          {% for date, item in page.metadata.worklog.data.items() %}
            {"date": "{{ date }}", "series": "Rémunéré", "count": {{ item['payed_hours'] }}},
            {"date": "{{ date }}", "series": "Bénévole", "count": {{ item['volunteer_hours'] }}},
          {% endfor %}
          ]
        }
      ,
      "mark": "bar",
      "encoding": {
        "x": {
          "timeUnit": {"unit": "dayofyear", "step": 1},
          "field": "date",
          "axis": {"format": "%d/%m"},
          "title": "Date",
          "step": 1,
        },
        "y": {
          "aggregate": "sum",
          "field": "count",
          "title": "Heures",
        },
        "color": {
          "field": "series",
          "scale": {
            "domain": ["Bénévole", "Rémunéré"],
            "range": ["#e7ba52", "#1f77b4"]
          },
          "title": "Type d'heures"
        }
      }
    };

  	vegaEmbed("#vis", spec)
    	// result.view provides access to the Vega View API
      .then(result => console.log(result))
      .catch(console.warn);
```

I've also added a small progress bar, made with unicode, which looks like this.

```
▓▓░░░░░░░░ 29% (51h / 175 prévues) 
```

Here is the code for it:
```jinja2
{% if "total_days" in page.metadata.keys() %}
      {% set percentage = page.metadata.worklog['percentage'] %}
      {% set total_blocks = 10 %}
      {% set percentage_value = (percentage / 100.0) %}
      {% set full_blocks = ((percentage_value * total_blocks) | round(0, 'floor') ) | int %}
      {% set empty_blocks = total_blocks - full_blocks %}
      <div class="progressbar">
        {# Display full blocks #}
        {% for i in range(full_blocks) %}▓{% endfor %}
        {# Display empty blocks #}
        {% for i in range(empty_blocks) %}░{% endfor %}
        {{ percentage }}% ({{ page.metadata.worklog['done_hours'] }}h / {{ page.metadata.worklog['total_hours'] }} prévues)
      </div>
```