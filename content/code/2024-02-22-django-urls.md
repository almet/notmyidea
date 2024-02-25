---
title: Using uuids in URLs in a Django app
tags: django, urls, uuid
---

After adding a regexp for uuids (which are quite hard to regexp for), I
discovered that Django [offers path converters](https://docs.djangoproject.com/
en/5.0/topics/http/urls/#path-converters), making this a piece of cake.

I was using old school `re_path` paths in my `urls.py`, but it's possible to
replace them with `path`, like this:

```python
url_patterns = (
    path(
        "datalayer/<int:map_id>/<uuid:pk>/",
        views.DataLayerView.as_view(),
        name="datalayer_view",
    ),
)
```

A few default path converters are defined (str, int, slug, uuid, path), but it's
also possible to define your own, as specified in the docs.
