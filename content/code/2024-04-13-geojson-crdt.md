---
title: A GeoJSON distributed Key/Value store
status: draft
---

Our requirements for uMap made it clear we don't really need
a complex CRDT library. We need a way to have peers agree on who is the last
writer, or to state it differently, to order the operations.

The rest of the picture is rather simple: just replace the value at a given location.

## The context

In our case, we have a server, and for the foreseable future we will continue to
have one. We don't want to rely on the server to assign timestamps on each write
operation because that would add too much delay, but we can use it to make sure
the messages are transmitted to the right peers.

So:

- The server has a GeoJSON document, and want to sync it with other peers.
- The server has a way to reach all the peers, using a WebSocket connection.
- Peers can go online and offline, and sync their changes with other peers when
they have connection.

## A Hybrid Logical Clock (HLC)

The different peers will send the server operations when something is changed on
their end. We need to have a way for peers to agree on the ordering of the
operations, without having to concert with each other.

One way to solve this is by using an hybrid logical clock. On each peer, an
hybrid physical+ logical clock is kept, composed of:

- The **physical time**: the current clock time.
- A **logical counter**: an incrementing counter, to differentiate between events that happened at the same clock tick.
- A **peer identifier**: A unique identifier for the peer

This makes it possible to order between different "times": first compare
physical times, then logical times, and finally any additional disambiguating
information such as peer identifiers if the other components are equal.

```python
def hlc_compare(hlc1, hlc2):
    physical_time1, logical_time1, peer_id1 = hlc1
    physical_time2, logical_time2, peer_id2 = hlc2

    if physical_time1 != physical_time2:
        return (physical_time1 > physical_time2) - (physical_time1 < physical_time2)
    elif logical_time1 != logical_time2:
        return (logical_time1 > logical_time2) - (logical_time1 < logical_time2)
    else:
        return (peer_id1 > peer_id2) - (peer_id1 < peer_id2)
```

## Operations

For now, let's reprensent the operations like this:

```python

# Set foobar to peerA
(1712938520, 500, "Peer A", "foobar=peerA")
```

Peers will send operations to the server, which will assign an incremental ID to each, so it's possible to keep track of which operations have been already received by the peers.

| ID  | Clock                     | Payload           |
| --  | -----                     | -------           |
| 90  | 1712938501, 500, "Peer A" | title=super       |
| 99  | 1712938520, 501, "Peer A" | layertype=cluster |
| 100 | 1712938502, 300, "Peer B" | color=blue        |
| 101 | 1712938510, 301, "Peer B" | markertype=drop   |
| 102 | 1712938520, 502, "Peer A" | foobar=peerA      |
| 103 | 1712938510, 302, "Peer B" | foobar=peerB      |

As we can see, incremental IDs might not match the clock order.

They are mainly here as a way for the server to know which operations should be
returned to the peers, based on their last known ID.

For instance, if peer A knows up to id 99, when it gets back online it can ask the
server for operations that happened since then, and then apply them locally
before rendering its interface.

## Compacting the data

We need to distinguish between these use cases:

- A new peer enters, and needs to get the freshest view from the server
- An existing peer reconnects, it might have local data to send, and need to reconciliate it with the freshest state.

### A new peer enters

When a new peer enters and needs to get fresh data, we can do it in multiple
ways. The simplest one is to make it redo the exact same things that happened on
other peers: get the same GeoJSON and apply the same operations on it.

It will work, but will require the server to serve all the operations that
happened over time to all clients, which is suboptimal. We can avoid this by
compacting the data on the server prior to serving it.

This view of the document needs to have an HLC associated with each key.

### An existing peer reconnects

```
T0   = Peer A retrieves data. It goes offline with it.
T1   = Peer A updates the data locally
T100 = Peer B updates the data and syncs
T101 = Peer A goes back online.
```

At T101, Peer A will tell the server: "hey, let me know what data you have since T0".
The server will return the operations since then, and Peer A will apply it locally.
It will then send the missing data that happened at T1.

Because peers know the time at which each change has been made, receiving old
data will be applied only if it's fresher than the current one.

## The data

Because we're using GeoJSON, the data is well defined. It looks like this:

```json
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [125.6, 10.1]
  },
  "properties": {
    "name": "Dinagat Islands"
  }
}
```

On uMap, a simple `.geojson` map looks like this (it's long, but I already removed a lot of data in there)

```json
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [
      -1.426849365234375,
      48.182112019648514
    ]
  },
  "properties": {
    "name": "Title",
    "zoom": 10,
    "miniMap": false,
    "overlay": {},
    "slideshow": {},
    "tilelayer": {
      "tms": false,
      "name": "OSM Positron (Carto)",
      "maxZoom": 20,
      "minZoom": 0,
      "attribution": "Map tiles by [[http://cartodb.com/attributions#basemaps|CartoDB]], under [[https://creativecommons.org/licenses/by/3.0/|CC BY 3.0]]. map data © [[http://osm.org/copyright|OpenStreetMap contributors]] under ODbL ",
      "url_template": "https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png"
    },
    "longCredit": "https://www.data.gouv.fr/fr/datasets/repertoire-national-des-associations/",
    "defaultView": "data",
    "description": "",
    "limitBounds": {},
    "onLoadPanel": "caption",
    // redacted. Tons of properties
    "permissions": {
      "edit_status": 3,
      "share_status": 1,
      "owner": {
        "id": 2712,
        "name": "ametaireau",
        "url": "/fr/user/ametaireau/"
      },
      "editors": []
    },
    "umap_id": 1053526,
    "umap_version": "2.1.3",
    "featuresHaveOwner": false,
    "datalayers": [
      {
        "id": "badb1518-9ff1-40a2-b8a8-4d6976904469",
        "fill": true,
        "name": "Concentration d'associations",
        "type": "Choropleth",
        "opacity": 0.1,
        "editMode": "disabled",
        "labelKey": "{nom}: {orgCount} ",
        "browsable": true,
        "inCaption": true,
        "showLabel": null,
        "choropleth": {
          "mode": "kmeans",
          "breaks": "0,11,25,51,149,420,708,2746,2746",
          "classes": 8,
          "property": "orgCount"
        },
        "remoteData": {},
        "description": "Le nombre d'associations par commune",
        "fillOpacity": 0.8,
        "permissions": {
          "edit_status": 0
        },
        "displayOnLoad": true,
        "labelInteractive": false
      }
    ]
  }
}

```


And a layer looks like this:

```json

{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [125.6, 10.1]
      },
      "properties": {
        "nom": "Dinagat Islands",
        "orgCount": 10,
      }
    }
  ],
  "_umap_options": {
    "displayOnLoad": true,
    "inCaption": true,
    "browsable": true,
    "editMode": "advanced",
    "name": "Photographies de 2019",
    "color": "Crimson",
    "iconUrl": "/uploads/pictogram/embassy-24.png",
    "iconClass": "Ball",
    "remoteData": {},
    "description": ""
  }
}
```

It's interesting to note that the data here has mixed purpose. It's at the same
time useful data for uMap, and for the geographical objects.

Now, what we want to do is to propagate the changes from one peer to another,
going trough the server.

Because uMap doesn't internally use the `GeoJSON` keys to handle its changes, we
will need to match between changes in the geoJSON and changes in uMap. It
actually goes both ways, when detecting the modified data, and when applying the
received changes.
