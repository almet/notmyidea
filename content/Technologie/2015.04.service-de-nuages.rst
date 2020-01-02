Service de nuages !
===================

:lang: fr
:summary: Retour sur le premier trimestre 2015: Readinglist, Kinto, Cliquet.

*Cet article est repris depuis le blog « Service de Nuages » de mon équipe à Mozilla*


Pas mal de changements depuis le début de l'année pour l'équipe
«cloud-services» francophone!

Tout d'abord, nouvelle importante, l'équipe s'étoffe avec des profils assez
complémentaires: `n1k0 <https://nicolas.perriault.net/>`_ et `Mathieu
<http://mathieu-leplatre.info>`_ sont venus prêter main forte à `Tarek
<http://ziade.org/>`_, `Rémy <http://natim.ionyse.com>`_ et `Alexis
<http://notmyidea.org>`_.

Le début de l'année a vu le lancement de `Firefox Hello
<https://www.mozilla.org/en-US/firefox/hello/>`_ ce qui nous a permis de passer
à l'échelle `le serveur <https://github.com/mozilla-services/loop-server>`_,
écrit en Node.js®, pour l'occasion.


Un serveur de listes de lecture
-------------------------------

En parallèle, un projet de `synchronisation de liste de lecture
<https://readinglist.readthedocs.org>`_ (*Reading List*) a vu le jour.  L'idée
étant de pouvoir marquer des pages "à lire pour plus tard" et de continuer la
lecture sur n'importe quel périphérique synchronisé (Firefox pour Android ou
Firefox Desktop). Un équivalent libre à `Pocket`_ en quelque sorte, qu'il est
possible d'héberger soit-même.

.. _Pocket: http://getpocket.com

.. image:: {filename}/images/readinglist-screenshot.png
    :alt: Capture d'écran de Firefox nightly avec readinglist.

Pour le construire, nous aurions pu réutiliser `Firefox Sync`_, après tout
c'est un service de synchronisation de données très robuste, construit avec `Cornice`_.
Mais seulement, *Sync* n'a pas été pensé pour garantir la pérennité des données,
et la marche était trop haute pour changer ça en profondeur.

.. _Firefox Sync: https://github.com/mozilla-services/server-syncstorage
.. _Cornice: http://cornice.readthedocs.org/

Nous aurions pu aussi nous contenter de faire une énième application qui expose
une API et persiste des données dans une base de données.

Mais cette nouvelle petite équipe n'est pas là par hasard :)


La «Daybed Team»
----------------

On partage une vision: un service générique de stockage de données ! Peut-être
que ça vous rappelle `un certain projet nommé Daybed <https://daybed.io>`_ ?
Pour les applications clientes, JavaScript, mobiles ou autres, l'utilisation de
ce service doit être un jeu d'enfant ! L'application gère ses données
localement (aka offline-first), et synchronise à la demande.

Ici, le cœur du serveur *Reading List* est justement une API "CRUD" (Create,
Retrieve, Update, Delete), qui gère de la synchronisation et de
l'authentification. Nous avons donc pris le parti de faire une API "simple",
avec le moins de spécificités possible, qui poserait les bases d'un service
générique. Notamment parce qu'il y a d'autres projets dans la même trempe qui vont suivre.

Pas mal d'expérience ayant été accumulée au sein de l'équipe, avec d'une part la
création de *Firefox Sync*, et d'autre part avec *Daybed*, notre side-project, nous
tentons de ne pas reproduire les mêmes erreurs, tout en gardant les concepts
qui ont fait leurs preuves.

Par exemple, nous avons conservé le mécanisme de collections d'enregistrements
et de *timestamp* de *Sync*. Comme ces problématiques sont récurrentes, voire
incontournables, nous avons décidé de reprendre le protocole de synchronisation,
de l'étendre légèrement et surtout de le dissocier du projet de listes de lecture.


Le mécanisme qui force à aller de l'avant
-----------------------------------------

Comme première pierre à l'édifice, nous avons donné naissance au projet
`Cliquet <https://cliquet.readthedocs.org>`_, dont l'idée principale est de
fournir une implémentation de ce protocole en python, tout en factorisant
l'ensemble de nos bonnes pratiques (pour la prod notamment).

.. image:: {filename}/images/cliquet-logo.png
    :align: right
    :alt: Logo du projet Cliquet

L'avantage d'avoir un protocole plutôt qu'un monolithe, c'est que si vous
préférez Asyncio, io.js ou Go, on vous encouragera à publier votre
implémentation alternative !

Avec *Cliquet*, le code du serveur liste de lecture consiste principalement
à définir un schéma pour les enregistrements, puis à forcer des valeurs de
champs sur certains appels. Cela réduit ce projet à quelques dizaines de lignes
de code.

Quant au futur service de stockage générique, `le projet
<http://kinto.readthedocs.org>`_ en est encore à ses balbutiements mais c'est
bel et bien en route ! Il permet déjà d'être branché comme backend de stockage
dans une application *Cliquet*, et ça `implémenté en 20 lignes de code
<https://github.com/mozilla-services/kinto/blob/0.2.1/kinto/views/collection.py>`_!

Ah, et cette fois, nous ne construirons les fonctionnalités qu'à partir des
besoins concrets qui surviennent. Ça paraît tout bête, mais sur *Daybed* on
l'a pas vu venir :)

Dans les prochains articles, nous avons prévu de décrire les bonnes pratiques
rassemblées dans le protocole (ou *Cliquet*), certains points techniques précis
et de vous présenter notre vision via des exemples et tutoriaux.

À bientôt, donc !
