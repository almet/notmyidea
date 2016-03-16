Carto Forms - First steps
#########################

:date: 17-11-2012
:status: draft

For an introduction on carto forms, please see this blog post:
https://blog.notmyidea.org/carto-forms.html (and its variant in french if you
prefer: https://blog.notmyidea.org/carto-forms-fr.html)

So, let's not talk too much about what we want to do, and rather explain how we
will do it instead ;)

Writing this article turned out to dump my thinking while bootstraping the
project, so I'm really explaining how I'm getting from here to there ;)

First step: defining a way to describe forms
============================================

What we want is a generic way to describe forms. I'm not sure if such a thing
exist. And, because I'm on a train atm, let's suppose there isn't anything like
this already (which is probably a wrong assumption, but, let's stick with that
for now).

What do we want? A way to associate titles, descriptions to a field. We also
want to be able to describe what's *in* the field (the type of content), and if
it is a repeatable field or not. In the case of a selection, we might also want
to have a list of possibilities somewhere. Let's take a simple example:

Title: Ads spots
Description: Describe all the ads spots in Paris
Fields:

- location (geoloc/address/lat-long)
- size *the size of the ad* (choice list: small/medium/big/huge)
- light *is there light on it?* (boolean)

Okay, so what we have here is in the form: name *description* (type of field).
In some way, we need to separate the widget that will be displayed to the user
from the type of data. What we need here is the type of data, the widget thing
should be decided at a different layer. So, let's refine the "location" field
to "location (SIG point)".

Okay, we now know what we want to save. Yet, we need to define the format.
At this point, I'm wondering if I should use XML, YAML or JSON to describe this
data. To be able to choose, listing the potential consumers / providers of data
can help. The first consumer of this data will be a REST API, and the first
producer will be, probably javascript (or whatever techno is used on the
client). Of course, we can provide lots of format on the REST API and depend
on the "Content-Types" header to know how to talk to it, but well, do we really
want or need to do that? Let's assume no for now and stick with JSON, because
it's now easily validable and I can't think of a language without a lib for it
(apart COBOL, of course).

Hey-hi, JSON. How does our data look with you? Let's dump a python structure
and dump it with `json.dumps`::

    data = {
    'title': 'Ads spots',
    'description': 'All the ads spots in paris',
    'fields': (
     {'name': 'location', 'type': 'SIG point'},
     {'name': 'size', 'type': 'choice', 'description': 'the size of the ad',
      'choices': ('small', 'medium', 'big', 'huge')},
     {'name': 'light', 'desciption': 'is there light on it?', 'type': 'bool'},
    )}
    import json
    json.dumps(data)

… and the result is (ran with `python data.py | python -m json.tool`) …::

    {
        "title": "Ads spots"
        "description": "All the ads spots in paris",
        "fields": [
            {
                "name": "location",
                "type": "SIG point"
            },
            {
                "choices": [
                    "small",
                    "medium",
                    "big",
                    "huge"
                ],
                "description": "the size of the ad",
                "name": "size",
                "type": "choice"
            },
            {
                "desciption": "is there light on it?",
                "name": "light",
                "type": "bool"
            }
        ],
    }

Validating the form definition
==============================

JSON is nice to us, JSON schema now exists and there are tools to work with it.
Quickly, it's the same kind of things than what's provided by XML Schema: you
create a schema, pass it some data and it's able to tell you if the data
complies with the schema. If not, it gives you a nice list of wrong fields.

The second option, in python, is a tool named colander, which approximately
does the same thing, but with its own syntax.

FIXME need to dig on json schema here and do an approx schema for this.

Creating the forms
==================

The next step is to actually create a form from this. Python, and django in
particular, have nice APIs to do that in python.  However, I don't know how
they internally work, but you can pass to it some data provided by an HTTP POST
request and it will tell you if it validate or no.

The problem with django is that you're tied to it, and it's not possible (well,
as far as I know) to get only the validation bits out of it. On the other hand,
the form framework already comes with nice geolocation facilities. It could be
nice to have a tool able to parse the format we defined and to generate django
models out of it.

We need to be careful here: what I'm talking about is to generate code… Well,
there are two approches to do that: either we generate a python file and parse
it, or either we can read the json data and programatically create a form out
of it, at runtime. We might want to cache this at some point to avoid doing it
each time, but let's consider it's another problem we will tackle later.

So, django internals!

Let's loop on the fields provided by our format and generate the form. We will
care about how to store this / retrieve it later :)

Oh, but wait. I'm talking about forms but I should be talking about models!
Validation is one thing, but what we want to do is to describe the data we will
be handling. Forms will just be the user facing thing and what will to the
validation!

Django, no django? Let's think about this one more time. There is another
competitor on this field, because we are talking about storing information that
are changing all the time and to base validation on them: CouchDB! And there
also is GeoCouch, which brings interesting SIG features to Couch. And it's
talking JSON!

Creating a new form should be as easy as this::

    $ curl -X POST localhost:5984/cartoforms/ -d "`python test.py`" -H "Content-Type: application/json"
    {"ok":true,"id":"2d58ef2b02eae639b3f94e357a000d26","rev":"1-0462d0827e7cdad20b5703a923249220"}

Hmm, wait, this is cool but we got this hideous hash. Let's change this to a
PUT instead::

    $  curl -X PUT localhost:5984/cartoforms/paris-ads -d "`python test.py`" -H "Content-Type: application/json"
    {"ok":true,"id":"paris-ads","rev":"1-0462d0827e7cdad20b5703a923249220"}

Of course, we can already retrieve this with a GET::

     curl -X GET localhost:5984/cartoforms/paris-ads -d "`python test.py`"
     {"_id":"paris-ads","_rev":"1-0462d0827e7cdad20b5703a923249220","fields":[{"type":"SIG
     point","name":"location"},{"choices":["small","medium","big","huge"],"type":"choice","name":"size","description":"the
     size of the ad"},{"type":"bool","desciption":"is there light on
     it?","name":"light"}],"description":"All the ads spots in
     paris","title":"Ads spots"}

Validation? Yes, you're completely right: we need validation for this. Because
in this current state, anyone can just insert whatever data they want into this
system, which could become a problem at some point.

Let's say we don't care who is able to publish to the DB, until we know that
what's being posted complies with a certain format. And, guess what's cool?
CouchDB provides validators. Yeah, I agree, it's somewhat exhausting to realize
that we have all this for free, but, heh, that's open source, dude!

Adding validation!
==================

So, we described our format already, what we need to do is to create a couchdb
validator which is able to filter this.

Hmm, I don't remember how they are named (will find out in the couch
documentation), but if I remember correctly, you can hook up some javascript
functions to each POST / PUT, to check that the data inserted is correct, and
output appropriate error messages when it's not what you expected.

Yeah, this means writing javascript, which is cool because I wanted to re-learn
how to do javascript!

… train arrives to station, see you next :)
