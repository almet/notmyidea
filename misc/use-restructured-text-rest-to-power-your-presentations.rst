Use Restructured Text (ReST) to power your presentations
#########################################################

:date: 2010-06-25

Wednesday, we give a presentation, with some friends, about the
CouchDB Database, to
`the Toulouse local LUG <http://www.toulibre.org>`_. Thanks a lot
to all the presents for being there, it was a pleasure to talk
about this topic with you. Too bad the season is over now an I quit
Toulouse next year. 

During our brainstorming about the topic, we
used some paper, and we wanted to make a presentation the simpler
way. First thing that come to my mind was using
`restructured text <http://docutils.sourceforge.net/rst.html>`_, so
I've wrote a simple file containing our different bullet points. In
fact, there is quite nothing to do then, to have a working
presentation. 

So far, I've used
`the rst2pdf program <http://code.google.com/p/rst2pdf/>`_, and a
simple template, to generate output. It's probably simple to have
similar results using latex + beamer, I'll try this next time, but
as I'm not familiar with latex syntax, restructured text was a
great option. 

Here are
`the final PDF output <http://files.lolnet.org/alexis/rst-presentations/couchdb/couchdb.pdf>`_,
`Rhe ReST source <http://files.lolnet.org/alexis/rst-presentations/couchdb/couchdb.rst>`_,
`the theme used <http://files.lolnet.org/alexis/rst-presentations/slides.style>`_,
and the command line to generate the PDF::

    rst2pdf couchdb.rst -b1 -s ../slides.style

