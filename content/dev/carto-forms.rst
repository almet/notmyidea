Carto-forms
###########

:date: 30-03-2012
:author: Alexis Métaireau, Mathieur Leplatre
:tags: GIS, forms

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

The use case
============

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

* Once finished, he gets an url (says http://forms.notmyidea.org/bearhugging)
* He can communicate the adress by the means he wants to his community and they
  can go to the page and fill it.

So, as youmay have notice, It would allow us to create interactive maps realy
easily, just a matter of some clicks for the users. and if we also think about
a nice Web API for this, we could do server-side validation and built even
phone applications easily. To push the cursor a bit further, if we can come
with a cool description format for the data, we could even build the forms
dynamically on different platforms, with a generic client.

Well, right, this is me dreaming.

Let's get it real
=================

As you may have understood, this isn't a really complicated problem. I've
started an etherpad document and we've been chatting about that with `Mathieu`_
some times. I think we can come with an elegant solution without too much
pain. Mathieu is used to work with GIS systems (which is really cool because
I'm not at all) and knows his subject, so that's an opportunity to learn ;-)

We will be at `Djangocong`_ on april 14 and 15 and we will probably have
a brainstorming session and a sprint on this, so if you want to help us, or
just to discuss, feel free to join!

We don't know yet if we will be using django for this or something else. We
have been thinking about couchdb, couchapps and geocouch but nothing is written
in stone yet. Comments and propositions are welcome!

.. _Djangocong:  http://rencontres.django-fr.org
.. _Mathieu: http://blog.mathieu-leplatre.info/
