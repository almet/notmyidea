Using dbpedia to get languages influences
#########################################

:date: 2011/08/16
:tags: dbpedia, sparql, python

While browsing the Python's wikipedia page, I found information about the languages 
influenced by python, and the languages that influenced python itself.

Well, that's kind of interesting to know which languages influenced others,
it could even be more interesting to have an overview of the connexion between
them, keeping python as the main focus.

This information is available on the wikipedia page, but not in a really
exploitable format. Hopefully, this information is provided into the
information box present on the majority of wikipedia pages. And… guess what?
there is project with the goal to scrap and index all this information in
a more queriable way, using the semantic web technologies.

Well, you may have guessed it, the project in question in dbpedia, and exposes
information in the form of RDF triples, which are way more easy to work with
than simple HTML.

For instance, let's take the page about python:
http://dbpedia.org/page/Python_%28programming_language%29

The interesting properties here are "Influenced" and "InfluencedBy", which
allows us to get a list of languages. Unfortunately, they are not really using
all the power of the Semantic Web here, and the list is actually a string with
coma separated values in it.

Anyway, we can use a simple rule: All wikipedia pages of programming languages
are either named after the name of the language itself, or suffixed with "(
programming language)", which is the case for python.

So I've built `a tiny script to extract the information from dbpedia <https://github.com/ametaireau/experiments/blob/master/influences/get_influences.py>`_ and transform them into a shiny graph using graphviz. 

After a nice::

    $ python get_influences.py python dot | dot -Tpng > influences.png

The result is the following graph (`see it directly here
<http://files.lolnet.org/alexis/influences.png>`_)

.. image:: http://files.lolnet.org/alexis/influences.png
    :width: 800px

Interestingly enough, it's stated that Java was an influence for Python (!!)

You can find the script `on my github account
<https://github.com/ametaireau/experiments>`_. Feel free to adapt it for
whatever you want if you feel hackish.
