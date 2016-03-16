Thoughts about a form generation service, GIS enabled
#####################################################

:slug: carto-forms
:date: 02-04-2012
:author: Alexis Métaireau, Mathieu Leplatre
:tags: GIS, forms
:lang: en

We have a plan. A "fucking good" one.

A bunch of friends asked me twice for quite the same thing: a webpage with a
form, tied to a map generation with some information filtering. They didn't
explicitly ask that but that's the gist of it.

This idea has been stuck in my head since then and I even think that we can
come out with something a little bit more flexible and useful. I've named it
*carto-forms* for now, but that's only the "codename".

To put it shortly: what if we had a way to build forms, ala Google forms, but
with geographic information in them?

If you don't know Google forms, it means having an user-friendly way to build
forms and to use them to gather information from different users.

In my opinion, Google forms is missing two important things: first, it's not
open-source, so it's not possible to hack it or even to run it on your own
server.  Second, it doesn't really know how to deal with geographic data, and
there is no way to filter the information more than in a spreadsheet.

I knew that `Mathieu`_ and some folks at `Makina Corpus`_  would be interested
in this, so I started a discussion with him on IRC and we refined the details
of the project and its objectives.

Imagine the following:

1. For a mapping party, we choose a specific topic to map and design the form
   (list of fields (i.e. tags) to be filled + description + type of the
   information) ;
2. In situ, users fill the form fields with what they see. Geo fields can be
   pre-populated using device geolocation ;
3. At the end of the day, we can see a map with all user contributions seized
   through this particular form ;
4. If relevant, a script could eventually import the resulting dataset and 
   publish/merge with OpenStreetMap.


Some use cases
==============

I can see some use cases for this. The first one is a collaborative map, with
facet filtering. Let's draw a potential user flow:

* An "administrator" goes to the website and creates a form to list all the
  alternative-related events. He creates the following fields:
  
  * Name: a plain text field containing the name of the event.

  * Category: the category of the event. Can be a finite list.

  * Location: The location of the event. It could be provided by selecting a
    point on a map or by typing an address.

  * Date: the date of the event (a datepicker could do the trick)

  Each field in the form has semantic information associated with it (yes/no,
  multiple selection, date-time, geocoding carto, carto selection etc)

* Once finished, the form is generated and the user gets an url (say
  http://forms.notmyidea.org/alternatives) for it.

* REST APIs allow third parties to get the form description and to
  push/edit/get information from there.

* He can communicate the address in any way he wants to his community so they
  can go to the page and add information to it.

* Then, it is possible to filter the results per location / date or category.
  This can be done via API calls (useful for third parties) or via a nice
  interface in the browser.

So, as you may have noticed, this would allow us to create interactive maps really
easily. It's almost just a matter of some clicks to the users. If we also come
up with a nice Web API for this, we could do server-side validation and build
even phone applications easily.

To push the cursor a bit further, if we can come with a cool description format
for the forms, we could even build the forms dynamically on different platforms,
with generic clients.

As mentioned before, the idea of a simple tool to support collaborative mapping 
fullfils a recurring necessity ! 

We envision a lot of example uses for this : recycling spots, accessible spots (wheelchairs,
etc.), trees identification, mushrooms picking areas, tracking of endangered species 
(e.g. Bonelli's Eagle is currently tracked by sharing a spreadsheet), spotting of dangerous
species (e.g. asian predatory wasps), map advertisement boards (most cities do not track them!),
citizen reporting (e.g. graffiti, potholes, garbage, lightning like http://fixmystreet.ca),
geocaching, trajectories (e.g hiking, runners, cyclists)...

Here are some other examples of where *carto-forms* could be useful:

Simple GIS storage backend
--------------------------

Let's say you are a mobile developer, you don't want to bother with PostGIS
nor write a custom and insecure code to insert and retrieve your GIS data! You
need carto-forms! A simple API helps you design your models/forms and the
same API allows you to CRUD and query your data. Thus, you only need to focus
on your application, not on how GIS data will be handled. 

We make a distinction between storage and widgets.

Besides, if you are a django / drupal / plomino... maintainer : you
can develop a module to "plug" your models (content types) and UI to carto-forms! 
Carto forms are then exposed to your backoffice users (ex: drupal admin UI, django
adminsite), and likewise you can write your own HTML widgets that consume datasets
in frontend views (facets in JSON/XML, and map data in GeoJSON).


Visualization tool
------------------

Since data submission can be done programmatically using the API, you could use Carto-forms
results page as a visualization tool. 

You can explore your dataset content using filters related to each form field. Facets filtering
is a great advantage, and a map shows the resulting features set. You feel like you're in 
front of a decision support system! 

Of course, filtered raw data can be downloaded (GeoJSON, XML) and a permalink allows to
share the page with the state of the filters and the zoom/location of the map.


Generic forms service
---------------------

If you want to generate a configuration file (or whatever, email messages, ...),
you will need a form and a template to inlay user submitted values and get the result.

A form service would be really useful to create forms programmatically and retrieve 
cleaned and validated input values. 

You could run a dedicated template service based on *carto-forms*! Parsing a template
content, this external service could create a form dynamically and bind them together.
The output of the form service (fields => values) would be bound to the input of a template 
engine (variables => final result).

Note that for this use-case, there is no specific need of GIS data nor storage of records 
for further retrieval.


What's out in the wild already?
===============================

Of course, there is Google forms, which allows you to do these kind of things,
but it's closed and not exactly what we are describing here.

We've discovered the interesting https://webform.com/ which allows one to create
forms with a nice drag-n-drop flow. I would love to reproduce something similar
for the user experience. However, the project doesn't handle APIs and
geolocation information.

The idea of http://thoth.io is very attractive : an extremely simple web API to store
and retrieve data. In addition, *carto-forms* would do datatype validation and have
basic GIS fields (point, line, polygon).

http://mapbox.com also did an awesome work on cartography, but didn't take into
account the form aspect we're leveraging here.

So… Let's get it real!
======================

As you may have understood, this isn't a really complicated problem. We have
been sometimes chatting about that with Mathieu about what we would need and
how we could achieve this.

We can probably come with an elegant solution without too much pain. Mathieu is
used to work with GIS systems (which is really cool because I'm not at all) and
knows his subject, so that's an opportunity to learn ;-)

We will be at `Djangocong`_ on April 14 and 15 and will probably have
a brainstorming session and a sprint on this, so if you are around and want to
help us, or just to discuss, feel free to join!

We don't know yet if we will be using django for this or something else. We
have been thinking about couchdb, couchapps and geocouch but nothing is written
in stone yet. Comments and proposals are welcome!

Here is the etherpad document we worked on so far:
http://framapad.org/carto-forms. Don't hesitate to add your thoughts and edit
it, that's what it's made for!

Thanks to `Arnaud`_ and `Fuzzmz`_ for proof-reading and typo fixing.

.. _Djangocong:  http://rencontres.django-fr.org
.. _Mathieu: http://blog.mathieu-leplatre.info/
.. _Arnaud: http://sneakernet.fr/
.. _Fuzzmz: http://qwerty.fuzz.me.uk/
.. _Makina Corpus: http://makina-corpus.com
