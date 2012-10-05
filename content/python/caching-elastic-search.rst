How to cache Elastic Seach Queries?
###################################

:status: other

The first thing to realize is what do we want to cache exactly? There is a fair
bit of things we might want to cache. Let's start by the most queried pages:
the home and the list of apps per category.

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
    latest = Webapp.latest(region=region, gaia=request.GAIA)[:10]

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

Caching is easy, invalidation is hard
=====================================

Right, we got this cached, good. But what happens when the data we cached
changes? Currently, nothing, we return the same data over and over again.

We need to tell our application when this cache isn't good anymore; we need to
*invalidate* it.

We can use different strategies for this:

* Set a timeout for the cache.
* Invalidate manually the cache when something changes, for instance using
  signals.

Here, obviously, we don't want to invalidate the cache each time we're adding
a new rating; what we'll do is to invalidate the cache manually, when we
compute the new popularity of the addons.

In this case, this is done by a command.
