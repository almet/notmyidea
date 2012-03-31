Carto-forms
###########

:date: 30-03-2012
:author: Alexis Métaireau, Mathieu Leplatre
:tags: GIS, forms
:status: draft

The idea
========

This idea is walking in my head since some time and I've been talking with a
bunch of people about it in the last few months. to put it shortly: what if we
had a way to build forms, ala google forms, but with geographic informations in
them?

If you don't know google forms, it means having an user-friendly way to build
forms, for the users. The form can then be used to submit data to a server,
which will do something with it.

Google forms is missing two important things: first, it's not open-source, so
it's not possible to hack it, or even to run it on your server. Second, it
doesn't *really* know how to deal with geographic data.

The use cases
=============

I can see many use cases for this. The first one is a collaborative map, with
facet filtering. Let's draw the user flow here:

* An "administrator" goes to the website and create a form to list all the bear
  hugging events in the world. He creates the following fields:
  
  * Name: a plain text field containing the name of the event.

  * Category: the category of the event. Can be a finite list (only brown
    bears, polar bears, female bears)

  * Location: The location of the event. It could be provided by selecting a
    point on a map or by typing an address.

  * Date: the date of the event (a datepicker could do the trick)

  Each field in the form has semantic information associated with it (yes/no,
  multiple selection, date-time, geocoding carto, carto selection etc)

* Once finished, the form is generated and the user gets an url (says
  http://forms.notmyidea.org/bearhugging) for it.

* REST APIs allow thrid parties to get the form description and to
  push/edit/get information from there.

* He can communicate the address by the means he wants to his community and
  they can go to the page and fill it.

So, as you may have notice, It would allow us to create interactive maps really
easily, just a matter of some clicks for the users. and if we also think about
a nice Web API for this, we could do server-side validation and built even
phone applications easily. To push the cursor a bit further, if we can come
with a cool description format for the data, we could even build the forms
dynamically on different platforms, with generic clients.

Designing dedicated forms for OSM mobile apps
---------------------------------------------

1. For a mapping party, we choose a specific topic to map and design the form
   (list of fields (i.e. tags) to be filled + description + type of the
   information)
2. In situ, users fill the form fields with what they see. Geo fields can be
   prepopulated using device geolocation
3. At the end of the day, we can see a map with all users contributions using
   this particular form. 
4. A script can import the resulting dataset and publish/merge with OSM

Examples:
~~~~~~~~~

recycling spots, accessible spots (wheelchairs, etc.), map advertisement
boards (most cities do not track them!)…

Simple GIS storage backend
--------------------------

For example, you are a mobile developper, you don't want to bother with PostGIS
nor writing custom and unsecure code to insert and retrieve your GIS data! You
need carto-forms! A simple API helps you to design your models/forms. A simple
API allows you to CRUD and query your data. Thus, you only need to focus on
your application, not on how GIS data will be handled.  Distinguish storage
from widgets

Besides, if you are a django/plomino/drupal/... maintainer : you
can develop a module to "plug" your UI to carto-forms! That's how you will
expose carto forms to your backoffice users (ex: drupal admin UI, django
adminsite). Likewise, you can write widgets that consume datasets in frontend
views (using any webmapping js library)

Examples:
~~~~~~~~~

- communities of users, consumers, ...
- directory of places

Integration with a template service
-----------------------------------

You could connect the output of a form service (fields => values) to the input
of a template service (variables => values).  A "template service" could be
some API where you post a dictionnary (keys and values) and obtain some
generated content.  As examples, template services could be used to generate
configuration files, email messages, HTML pages...  To build a web interface of
a template service, you need to display a form where the user can assign values
to variables.  Variable list, type, options, validation... a form service would
be really useful.

Visualization tool
------------------

I can explore my dataset content using filters related to each form field.
Faceting can be an idea in order to ease filtering.  A map shows the resulting
features set, and raw data can be downloaded (geojson, xml) Ideally, I would
like to obtain a filtered dataset using a Web API.

What's out in the wild already?
===============================

Of course, there is google forms, which allows you to do this kind of things,
but it's closed and not exactly what we are describing here.

We've discovered the interesting https://webform.com/ which allows to create
forms with a nice drag-n-drop flow. I would love to reproduce something similar
for the user experience. However, the project doesn't handles APIs and
geolocation information.

So… Let's get it real!
======================

As you may have understood, this isn't a really complicated problem. I've
started `an etherpad document <http://framapad.org/carto-forms>`_ and we've
been chatting about that with `Mathieu`_ some times. I think we can come with
an elegant solution without too much pain. Mathieu is used to work with GIS
systems (which is really cool because I'm not at all) and knows his subject, so
that's an opportunity to learn ;-)

We will be at `Djangocong`_ on april 14 and 15 and we will probably have
a brainstorming session and a sprint on this, so if you want to help us, or
just to discuss, feel free to join!

We don't know yet if we will be using django for this or something else. We
have been thinking about couchdb, couchapps and geocouch but nothing is written
in stone yet. Comments and propositions are welcome!

.. _Djangocong:  http://rencontres.django-fr.org
.. _Mathieu: http://blog.mathieu-leplatre.info/
