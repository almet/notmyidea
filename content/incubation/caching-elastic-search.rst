How to cache Elastic Seach Queries?
###################################

:status: other

These days, I'm working on Marketplace, the Mozilla's Appstore. Internally,
we're doing Elastic Search to do search, and after some load tests, we
eventually found out that Elastic Search was our bottleneck.

So we want to reduce the number of requests we do to this server. Currently,
the requests are done trough HTTP.

The first thing to realize is what do we want to cache exactly? There is a fair
bit of things we might want to cache. Let's start by the most queried pages:
the home and the list of apps per category.

Different approaches
====================

You can put the cache in many different locations. The code powering
Marketplace is kinda fuzzy sometimes. The requests to Elastic Search are done
in a number of different parts of the code. They're done sometimes directly
with HTTP calls, sometimes using the ElasticUtils library, sometimes using some
other lib…

That's kind of hard to get where and how to add the caching layer here. What
did we do? We started to work on an HTTP caching proxy. This proxy could

Find a key
==========



Caching things
==============

Caching is easy, it's something like that, in term of python code::

    if key in cache:
        value = cache.get(key)
    else:
        value = do_the_request()
        cache.set(key, value)
    return value

Back to business logic: I want to cache the request that are done on the
homepage. The code currently looks like this::

    popular = Webapp.popular(region=region, gaia=request.GAIA)[:10]

Nothing fancy going on here, we're displaying the list of popular and latest
apps on the marketplace. I can cache the results for each region, and depending
if `request.GAIA` is `True` or not. The key will look like `popular-{region}`,
to which I will eventually append `-gaia` if it makes sense. More generally,
I will turn a number of criterias into a single key, like this::

    def cache(qs, *keys):
        """Cache the given querystring"""
        key = '-'.join(keys)
        if key in cache:
            result = cache.get(key)
        else:
            result = qs
            cache.set(key, result)
        return result

Which I can use like this::

    keys = [region.slug, ]
    if request.GAIA:
        keys.append('gaia')

    popular = cache(Webapp.popular(region=region, gaia=request.GAIA)[:10],
                    'popular', *keys)

Invalidation is hard?
=====================

Right, we got this cached, good. But what happens when the data we cached
changes? Currently, nothing, we return the same data over and over again.

We need to tell our application when this cache isn't good anymore; we need to
*invalidate* it.

We can use different strategies for this:

* Set a timeout for the cache.
* Invalidate manually the cache when something changes, for instance using
  signals.

I started by having a look at how I wanted to invalidate all of this, case by
case. The problem
