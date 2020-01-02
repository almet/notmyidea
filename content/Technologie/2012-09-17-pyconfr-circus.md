# Circus sprint at PyconFR

Last Thursday to Sunday, [Pycon France](http://pycon.fr) took place, in
Paris. It was the opportunity to meet a lot of people and to talk about
python awesomness in general.

We had three tracks this year, plus sprints the two first days. We
sprinted on [Circus](http://circus.io), the process and socket manager
we're using at Mozilla for some of our setups.

The project gathered some interest, and we ended up with 5 persons
working on it. Of course, we spent some time explaining what is Circus,
how it had been built, a lot of time talking about use-cases and
possible improvements, but we also managed to add new features.

Having people wanting to sprint on our projects is exciting because
that's when making things in the open unleashes its full potential. You
can't imagine how happy I was to have some friends come and work on this
with us :)

Here is a wrap-up of the sprint:

## Autocompletion on the command-line

[Remy Hubscher](http://natim.ionyse.com) worked on the command-line
autocompletion. Now we have a fancy command-line interface which is able
to aucomplete if you're using bash. It seems that not that much work is
needed to make it happen on zsh as well :)

[Have a look at the
feature](https://github.com/mozilla-services/circus/blob/master/extras/circusctl_bash_completion)

On the same topic, we now have a cool shell for Circus. If you start the
circusctl command without any option, you'll end-up with a cool shell.
Thanks [Jonathan Dorival](https://github.com/jojax) for the work on
this\! You can have a look at [the pull
request](https://github.com/mozilla-services/circus/pull/268).

## Future changes to the web ui

[Rachid Belaid](https://twitter.com/rachbelaid) had a deep look at the
source code and is much more familiarized to it now than before. We
discussed the possibility to change the implementation of the web ui,
and I'm glad of this. Currently, it's done with bottle.py and we want to
switch to pyramid.

He fixed some issues that were in the tracker, so we now can have the
age of watchers in the webui, for instance.

## Bug and doc fixing

While reading the source code, we found some inconsistencies and fixed
them, with [Mathieu Agopian](http://mathieu.agopian.info/). We also
tried to improve the documentation at different levels.

Documentation still needs a lot of love, and I'm planning to spend some
time on this shortly. I've gathered a bunch of feedback on this

## Circus clustering capabilities

One feature I wanted to work on during this sprint was the clustering
abilities of Circus. Nick Pellegrino made an internship on this topic at
Mozilla so we spent some time to review his pull requests.

A lot of code was written for this so we discussed a bunch of things
regarding all of this. It took us more time than expected (and I still
need to spend more time on this to provide appropriate feedback), but it
allowed us to have a starting-point about what this clustering thing
could be.

Remy wrote [a good summary about our
brainstorming](http://tech.novapost.fr/circus-clustering-management-en.html)
so I'll not do it again here, but feel free to contact us if you have
ideas on this, they're very welcome\!

## Project management

We've had some inquiries telling us that's not as easy as it should to
get started with the Circus project. Some of the reasons are that we
don't have any release schedule, and that the documentation is hairy
enough to lost people, at some point :)

That's something we'll try to fix soon :)

PyconFR was a very enjoyable event. I'm looking forward to meet the
community again and discuss how Circus can evolve in ways that are
interesting to everyone.

Tarek and me are going to [Pycon ireland](http://python.ie/pycon/2012/),
feel free to reach us if you're going there, we'll be happy to meet and
enjoy beers\!
