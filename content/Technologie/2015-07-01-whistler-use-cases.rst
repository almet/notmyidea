Service de nuages : Perspectives pour l'été
###########################################

:lang: fr
:date: 2015-07-07
:summary: Le travail en cours et les fonctionnalités à venir pour les prochains mois.

*Cet article est repris depuis le blog « Service de Nuages » de mon équipe à Mozilla*

Mozilla a pour coutume d'organiser régulièrement des semaines de travail où tous les employés
sont réunis physiquement. Pour cette dernière édition, nous avons pu retrouver
nos collègues du monde entier à `Whistler, en Colombie Britannique au Canada
<http://www.openstreetmap.org/node/268148288#map=4/50.12/-122.95>`_ !

.. image:: {filename}/images/whistler-talks.jpg
    :alt: «All Hands» talk about Lego, by @davidcrob - CC0
    :align: center

Ce fût l'occasion pour notre équipe de se retrouver, et surtout de partager notre
vision et nos idées dans le domaine du stockage, afin de collecter des cas d'utilisation pour
notre solution `Kinto <https://kinto.readthedocs.org>`_.

Dans cet article, nous passons en revue les pistes que nous avons pour
les prochains mois.


Ateliers et promotion
=====================

Nicolas a présenté `Kinto.js <https://github.com/mozilla-services/kinto.js>`_ dans un atelier dédié, avec comme support de
présentation le `tutorial d'introduction <http://kintojs.readthedocs.org/en/latest/tutorial/>`_.

L'application résultante, pourtant toute simple, permet d'appréhender les
concepts de synchronisation de Kinto. Le tout sans installation prélable,
puisque Rémy a mis en place un `serveur de dev effacé tous les jours <https://kinto.dev.mozaws.net/v1/>`_.

Nous avions mis un point d'honneur à faire du Vanilla.JS, déjà pour éviter les
combats de clochers autour des frameworks, mais aussi pour mettre en évidence qu'avec
HTML5 et ES6, on n'était plus aussi démunis qu'il y a quelques années.

Ce petit atelier nous a permis de nous rendre compte qu'on avait encore de
grosses lacunes en terme de documentation, surtout en ce qui concerne
l'éco-système et la vision globale des projets (Kinto, Kinto.js, Cliquet, ...).
Nous allons donc faire de notre mieux pour combler ce manque.

.. image:: {filename}/images/whistler-workshop.jpg
    :alt: Kinto.js workshop - CC0
    :align: center


Mozilla Payments
================

Comme `décrit précédemment <http://www.servicedenuages.fr/la-gestion-des-permissions>`_, nous avons mis en place un système de permissions pour répondre aux besoins de suivi des paiements et abonnements.

Pour ce projet, Kinto sera utilisé depuis une application Django, via un client Python.

Maintenant que les développements ont été livrés, il faut transformer l'essai, réussir l'intégration, l'hébergement et la montée en puissance. La solution doit être livrée à la fin de l'année.

À venir
-------

Nous aimerions en profiter pour implémenter une fonctionnalité qui nous tient à coeur : la construction de la liste des enregistrements accessibles en lecture sur une collection partagée.

.. image:: {filename}/images/whistler-lake.jpg
    :alt: Whistler Alta Lake - CC0
    :align: center


Firefox OS et stockage
======================

Nous avons eu beaucoup d'échanges avec l'équipe de Firefox OS, avec qui nous avions
déjà eu l'occasion de collaborer, pour le `serveur d'identification BrowserID par SMS <https://github.com/mozilla-services/msisdn-gateway>`_ et pour `Firefox Hello <https://github.com/mozilla-services/loop-server>`_.

In-App sync
-----------

Kinto, la solution simple promue pour la synchronisation de données dans les applications
Firefox OS ? La classe ! C'est ce qu'on avait en tête depuis longtemps, déjà à
l'époque avec `Daybed <http://daybed.readthedocs.org/>`_. Voici donc une belle opportunité à saisir !

Il va falloir expliciter les limitations et hypothèses simplificatrices de notre
solution, surtout en termes de gestion de la concurrence. Nous sommes persuadés
que ça colle avec la plupart des besoins, mais il ne faudrait pas décevoir :)

Le fait que `Dale <https://github.com/daleharvey>`_, un des auteurs de `PouchDB <http://pouchdb.com/>`_ et `Michiel de Jong <https://github.com/michielbdejong>`_, un des auteurs de `Remote Storage <http://remotestorage.io/>`_, nous aient encouragés sur nos premiers pas nous a bien motivé !


Cut the Rope
------------

Kinto devrait être mis à profit pour synchroniser les paramètres et les scores
du `jeu <http://mozilla.cuttherope.net/>`_. Un premier exercice et une première vitrine sympas !

« SyncTo »
----------

`Firefox Sync <https://docs.services.mozilla.com/storage/apis-1.5.html>`_ est la solution qui permet de synchroniser les données de Firefox (favoris, extensions, historique, complétion des formulaires, mots de passe, ...) entre plusieurs périphériques, de manière chiffrée.

L'implémentation du client en JavaScript est relativement complexe et date un peu maintenant.
Le code existant n'est pas vraiment portable dans *Firefox OS* et les tentatives de réécriture
n'ont pas abouti.

Nous souhaitons implémenter un pont entre *Kinto* et *Firefox Sync*, de manière
à pouvoir utiliser le client *Kinto.js*, plus simple et plus moderne, pour récupérer
les contenus et les stocker dans IndexedDB. Le delta à implémenter côté serveur est faible car nous nous étions
inspirés du protocole déjà éprouvé de Sync. Côté client, il s'agira surtout de
câbler l'authentification BrowserId et la Crypto.

Alexis a sauté sur l'occasion pour commencer l'écriture d'`un client python pour Firefox Sync <https://github.com/mozilla-services/syncclient>`_, qui servira de brique de base pour l'écriture du service.

Cloud Storage
-------------

Eden Chuang et Sean Lee ont présenté les avancées sur l'intégration de services de stockages
distants (*DropBox, Baidu Yun*) dans *Firefox OS*. Actuellement, leur preuve de
concept repose sur `FUSE <https://fr.wikipedia.org/wiki/Filesystem_in_Userspace>`_.

Nous avons évidemment en tête d'introduire la notion de fichiers attachés dans
*Kinto*, en implémentant la specification
`*Remote Storage* <https://tools.ietf.org/html/draft-dejong-remotestorage-05>`_,
mais pour l'instant les cas d'utilisations ne se sont pas encore présentés officiellement.


À venir
-------

Nous serons probablement amenés à introduire la gestion de la concurrence dans
le client JS, en complément de ce qui a été fait sur le serveur, pour permettre
les écritures simultanées et synchronisation en tâche de fond.

Nous sommes par ailleurs perpétuellement preneurs de vos retours — et bien
entendu de vos contributions — tant sur le code `serveur <https://github.com/mozilla-services/kinto/>`_
que `client <https://github.com/mozilla-services/kinto.js/>`_  !

.. image:: {filename}/images/whistler-cloud-storage.jpg
    :alt: Firefox OS Cloud Storage Presentation - CC0
    :align: center


Contenus applicatifs de Firefox
===============================

Aujourd'hui Firefox a un cycle de release de six semaines. Un des objectifs
consiste à désolidariser certains contenus applicatifs de ces cycles
relativement longs (ex. *règles de securité, dictionnaires, traductions, ...*) [#]_.

Il s'agit de données JSON et binaire qui doivent être versionnées et synchronisées par
les navigateurs (*lecture seule*).

Il y a plusieurs outils officiels qui existent pour gérer ça (*Balrog*, *Shavar*, ...),
et pour l'instant, aucun choix n'a été fait. Mais lors des conversations avec
l'équipe en charge du projet, ce fût vraiment motivant de voir que même pour
ce genre de besoins internes, *Kinto* est tout aussi pertinent !

.. [#]

    La bonne nouvelle c'est que toutes les fonctionnalités *third-party* qui ont
    été intégrées récemment vont redevenir des *add-ons* \\o/.

.. image:: {filename}/images/whistler-landscape.jpg
    :alt: Landscape - CC0
    :align: center


Awesome bar
===========

L'équipe *Firefox Labs*, le laboratoire qui élève des pandas roux en éprouvette,
serait vraiment intéressé par notre solution, notamment pour abreuver en données
un prototype pour améliorer *Awesome bar*, qui fusionnerait URL, historique et recherche.

Nous ne pouvons pas en dire beaucoup plus pour l'instant, mais les fonctionnalités
de collections d'enregistrements partagées entre utilisateurs de *Kinto*
correspondent parfaitement à ce qui est envisagé pour le futur du navigateur :)


À venir
-------

Nous serons donc probablement amenés, avant de la fin de l'année, à introduire des
fonctionnalités d'indexation et de recherche *full-text* (comprendre *ElasticSearch*).
Cela rejoint nos plans précédents, puisque c'est quelque chose que nous avions dans
*Daybed*, et qui figurait sur notre feuille de route !

.. image:: {filename}/images/whistler-labs.jpg
    :alt: Firefox Labs Meeting - CC0
    :align: center


Browser.html
============

L'équipe *Recherche* explore les notions de plateforme, et travaille notamment
sur l'implémentation d'un navigateur en JS/HTML avec *React*:
`browser.html <https://github.com/mozilla/browser.html>`_

*Kinto* correspond parfaitement aux attentes
de l'équipe pour synchroniser les données associées à un utilisateur.

Il pourrait s'agir de données de navigation (comme Sync), mais aussi de collections
d'enregistrements diverses, comme par exemple les préférences du navigateur
ou un équivalent à *Alexa.com Top 500* pour fournir la complétion d'URL sans
interroger le moteur de recherche.

L'exercice pourrait être poussé jusqu'à la synchronisation d'états *React*
entre périphériques (par exemple pour les onglets).

À venir
-------

Si *browser.html* doit stocker des données de navigation, il faudra ajouter
des fonctionnalités de chiffrement sur le client JS. Ça tombe bien, c'est un
sujet passionant, et `il y a plusieurs standards <http://www.w3.org/TR/WebCryptoAPI/>`_ !

Pour éviter d'interroger le serveur à intervalle régulier afin de synchroniser les
changements, l'introduction des `*push notifications* <https://w3c.github.io/push-api/>`_ semble assez naturelle.
Il s'agirait alors de la dernière pierre qui manque à l'édifice pour obtenir
un «*Mobile/Web backend as a service*» complet.

.. image:: {filename}/images/whistler-roadmap.jpg
    :alt: Roadmap - CC0
    :align: center


Conclusion
==========

Nous sommes dans une situation idéale, puisque ce que nous avions imaginé
sur `notre feuille de route <https://github.com/mozilla-services/kinto/wiki/Roadmap>`_ correspond à ce qui nous est demandé par les
différentes équipes.

L'enjeu consiste maintenant à se coordonner avec tout le monde, ne pas décevoir,
tenir la charge, continuer à améliorer et à faire la promotion du produit, se concentrer
sur les prochaines étapes et embarquer quelques contributeurs à nos cotés pour
construire une solution libre, générique, simple et auto-hébergeable pour le stockage
de données sur le Web :)

.. image:: {filename}/images/whistler-top-roof.jpg
    :alt: Friday Night Party - CC0
    :align: center
