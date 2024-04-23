---
tags: umap, datasette, opendata
---
# Mapping the concentration of not-for-profit organizations

Following a discussion with a friend, I realized the number of not-for-profit
organizations could be a good indicator of activities in a city, potentially
corellating it to well-being.

I wanted to create a [choropleth](https://en.wikipedia.org/wiki/Choropleth_map) map,
so that different cities appear in different colors on the map,
depending on their respective number of organisations.

## Getting the data

The first thing to do was to retrieve the data. I needed two distincts datasets:

- the cities and their shapes, to display them.
- the number of organisations per city.

The first one was easy, thanks to [France GeoJSON](https://france-geojson.gregoiredavid.fr/), I was able to download [the geometries of the cities of my department](https://france-geojson.gregoiredavid.fr/repo/departements/35-ille-et-vilaine/communes-35-ille-et-vilaine.geojson).

For the number of organisations, I found some [data on data.gouv.fr](https://www.data.gouv.fr/fr/datasets/repertoire-national-des-associations/?reuses_page=3#/community-resources),  but the comments made me explore [the official journal dataset](https://journal-officiel-datadila.opendatasoft.com/explore/dataset/jo_associations/table/?sort=dateparution).

Turns out it's possible to issue requests on an API, without having to download everything, so I went with this pseudo SQL statement:

```SQL
SELECT count(*) as nb_asso
WHERE departement_libelle=="Ille-et-Vilaine"
GROUP BY "codepostal_actuel"
ORDER BY -nb_asso
```

Which translates [to this URL](https://journal-officiel-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/jo_associations/records?select=count(*)%20as%20nb_asso&where=departement_libelle%3D%22Ille-et-Vilaine%22&group_by=codepostal_actuel&order_by=-nb_asso&offset=0)

## Merging the data with jq

I had all the interesting bits, but in two unrelated `json` files.

[jq](https://jqlang.github.io/jq/manual/), a tool to manipulate JSON data allowed me
to merge these files together, using the `--slurpfile` argument:

```bash

jq --slurpfile orgs organizations.json '.features |= map(
   .properties |= (. as $props |
     ($orgs[0].results[] | select(.codepostal_actuel == $props.code) | . + $props)
   )
 )' cities.geojson > enriched-cities.geojson
```

I still find it a bit hard to read, but basically what this does is:

- use the `cities.geojson` file as an input
- references `organizations.json` as a second input, naming it `orgs`.
- for each of the geojson properties, merge them with the data coming from orgs, matching on the postal code.

It's using `map()` and the `|=` syntax from jq to do this.

So, it works, and produces an enhanced version of the `.geojson`.

But it turns out that the data I got wasn't good enough.

## Second take

It turns out this simple version is returning no results for the biggest city around (Rennes). There is something fishy.

Let's see the kind of data that's inside this `.geojson` file in more details:

```bash

jq '.features[].properties | select(.nom == "Rennes")' cities.geojson
{
  "code": "35238",
  "nom": "Rennes"
}```

It turns out this code is not the postal code, but the INSEE code, and these aren't used in the other dataset:

```bash
jq '.results[] | select(.codepostal_actuel == "35238")' organizations.json
# Returns nothing
```

The other dataset I had access to is exposing these codes, so I downloaded all the files, imported them in [datasette](https://datasette.io) and issued an SQL query on it:

```SQL
SELECT COUNT(*) AS count, adrs_codeinsee, libcom
FROM base_rna
WHERE adrs_codepostal LIKE '35%'
GROUP BY adrs_codepostal, libcom;
```

The produced data looked like a typical datasette JSON result:

```javascript
{
  // …
  "rows": [
    [
      2746,
      "35238",
      "RENNES"
    ],
    [
      14,
      "35116",
      "FRESNAIS"
    ],
    // other records here…
  ],
  // …
}
```

Here is the updated jq query, defaulting to 0 for the org count when nothing
is found:

```bash

jq --slurpfile orgs organizations.json '
 .features |= map(
   .properties |= (
     . as $props |
     ((($orgs[0].rows[] | select(.[1] == $props.code))[0]) // 0) as $orgCount |
     . + { "orgCount": $orgCount }
   )
 )
' cities.geojson > enriched-cities.geojson
```

## Visualisation

I've imported this as a choropleth layer in uMap, it looks like this:

<iframe width="100%" height="300px" frameborder="0" allowfullscreen allow="geolocation" src="//umap.openstreetmap.fr/fr/map/concentration-des-associations-en-ille-et-vilaine_1053526?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&editMode=disabled&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=none&captionBar=false&captionMenus=true"></iframe><p><a href="//umap.openstreetmap.fr/fr/map/concentration-des-associations-en-ille-et-vilaine_1053526?scaleControl=false&miniMap=false&scrollWheelZoom=true&zoomControl=true&editMode=disabled&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=none&captionBar=false&captionMenus=true">Voir en plein écran</a></p>
