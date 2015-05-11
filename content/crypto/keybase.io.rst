Simplifier les preuves d'identités
##################################

:date: 2015-05-11
:headline: Qu'est-ce que Keybase.io et comment essayent-ils de simplifier la
           création de preuves d'identité.

L'un des problèmes non réellement résolu actuellement quant au chiffrement des
échanges est lié à l'authenticité des clés. Si quelqu'un décide de publier une
clé en mon nom, et en utilisant mon adresse email, cela lui est assez facile.

Il est donc nécessaire d'avoir des moyens de prouver que la clé publique que
j'utilise est réellement la mienne.

Traditionnellement, il est nécessaire de faire signer ma clé publique par
d'autres personnes, via une rencontre en personne ou des échanges hors du
réseau. C'est par exemple ce qui est réalisé lors des `Key Signing parties
<https://fr.wikipedia.org/wiki/Key_signing_party>`_.

Une manière simple d'effectuer ces vérifications serait, en plus de donner son
adresse email, sa signature de clé, ou a minima de donner un mot clé pour
valider que les échanges proviennent bien de la bonne personne.

PGP propose un mécanisme de signature des clés d'autrui, une fois celles ci
validées, ce qui permet de placer sa confiance dans les signataires de la clé.

`Keybase.io <https://keybase.io>`_ est un service qui vise à rendre la création
de ces preuves plus facile, en partant du principe qu'il est possible
d'utiliser différents moyens afin de prouver l'identité des personnes. Par
exemple, leurs comptes Twitter, GitHub ou leurs noms de domaines. De la même
manière qu'il est possible de signer (valider) les clés de nos amis, il est
possible de les "tracker" selon le jargon de keybase.

Donc, en somme, *Keybase.io* est un annuaire, qui tente de rendre plus facile la
création de preuves. Bien.

Quelques points d'ombre
=======================

Il s'agit d'une *startup* américaine, domiciliée dans le Delaware, qui se trouve être
un des paradis fiscaux qui `est connu pour être un paradis fiscal au coeur
même des États-Unis <https://fr.wikipedia.org/wiki/Delaware>`_. Je ne veux pas
faire de raccourcis trop rapides, bien évidemment, alors `j'ai ouvert un ticket
sur GitHub pour en savoir plus
<https://github.com/keybase/keybase-issues/issues/1569>`_ (après tout, le fait
d'être un paradis fiscal permet peut-être d'échapper à certaines lois sur la
requêtes de données). D'autant plus étonnant, la startup n'a pour l'instant `pas
de *business model* <https://github.com/keybase/keybase-issues/issues/788>`_
(ce qui en un sens est assez rassurant, même si on peut se poser la question de
pourquoi faire une startup dans ces cas là).

Le service (bien qu'en Alpha), n'est pas mis à disposition sous licence libre,
ce qui pour l'instant empêche quiconque de créer son propre serveur Keybase.
`Une partie des composants, cependant, le sont (open source)
<https://github.com/keybase/>`_.

J'ai du mal à croire en des initiatives qui veulent sauver le monde, mais dans
leur coin, je ne comprends pas pourquoi il n'y à pas de documentation sur
comment monter son propre serveur, ou comment les aider à travailler sur la
fédération. Mais bon, c'est pour l'instant une initiative encore fraîche, et je
lui laisse le bénéfice du doute.

Sur le long terme, une infrastructure comme *Keybase.io*, devra évidemment être
`distribuée <https://github.com/keybase/keybase-issues/issues/162>`_.

.. epigraph::

    We've been talking about a total decentralization, but we have to solve
    a couple things, synchronization in particular. Right now someone can
    mirror us and a client can trust a mirror just as easily as the server at
    keybase.io, but there needs to be a way of announcing proofs to any server
    and having them cooperate with each other. We'd be so happy to get this
    right.

    -- `Chris Coyne, co-founder of Keybase
    <http://chris.beams.io/posts/keybase/>`_

Afin de se "passer" de leur service centralisé, les preuves générées (qui sont
la force du système qu'ils mettent en place) pourraient être exportées sur des
serveurs de clés existants. C'est quelque chose `qu'ils souhaitent réaliser .
<https://github.com/keybase/keybase-issues/issues/890>`_.

Bref, une initiative quand même importante et utile, même si elle soulève des
questions qui méritent qu'on s'y attarde un brin.

Par ailleurs, `d'autres projets qui visent des objectifs similaires
<https://leap.se/nicknym>`_ existent, via le projet LEAP, mais je n'ai pas
encore creusé.
