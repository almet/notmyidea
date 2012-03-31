Carto-forms
###########

:slug: carto-forms
:date: 30-03-2012
:author: Alexis Métaireau, Mathieu Leplatre
:tags: GIS, forms
:lang: fr
:status: draft

On a un plan. Un "truc de ouf".

À plusieur reprises, des amis m'ont demandé de leur coder la même chose, à
quelques details près: une page web avec un formulaire qui permettrait de
soumettre des informations géographiques, lié à une carte et des manières de
filtrer l'information.

L'idée fait son bout de chemin, et je commence à penser qu'on peut même avoir
quelque chose de vraiment flexible et utile. J'ai nommé le projet "carto-forms"
pour l'instant (mais c'est uniquement un nom de code).

Pour résumer: et si on avait un moyen de construire des formulaires, un peu
comme google forms, mais avec des informations géographiques en plus?

Si vous ne connaissez pas google forms, il s'agit d'une interface simple
d'utilisation pour générer des formulaires et récupérer des informations depuis
ces derniers.

Google forms est un super outil mais à mon avis manque deux choses importantes:
premièrement, il s'agit d'un outil propriétaire (oui, on peut aussi dire
privateur) et il n'est donc pas possible de le hacker un peu pour le faire
devenir ce qu'on souhaite, ni l'installer sur notre propre serveur.
Deuxièmement, il ne sait pas vraiment fonctionner avec des informations
géographiques, et il n'y à pas d'autre moyen de filtrer les informations que
l'utilisation de leur système de feuilles de calcul.

Après avoir réfléchi un petit peu à ça, j'ai contacté `Mathieu`_ et les anciens
collègues de chez `Makina Corpus`_, puisque les projets libres à base de carto
sont à même de les intéresser. Et j'ai bien eu raison, j'ai récupéré pas mal de
feedback, et nous sommes en train, avec Mathieu, de définir plus clairement les
objectifs et autres détails.

Quelques cas d'utilisation
==========================

J'arrive à imaginer differents cas d'utilisation pour cet outil. Le premier est
celui que j'ai approximativement décrit plus haut: la génération de cartes de
manière collaborative, avec du "facet filtering". Voici un flux d'utilisation:

* Un "administrateur" se rends sur le site web et créé un nouveau formulaire
  pour l'ensemble des évènements alternatifs. Il crée les champs suivants:
  
  * Nom: le champ qui contiens le nom de l'évènement.

  * Categorie: la catégorie de l'évènement (marche, concert, manifestation…).
    Il peut s'agir d'un champ à multiples occurances.

  * Le lieu de l'évènement. Celui ci peut être donné soit par une adresse soit
    en selectionnant un point sur une carte.

  * Date: la date de l'évènement (un "date picker" peut permettre cela
    facilement)

  Chaque champ dans le formulaire à des informations sémentiques associées
  (oui/non, multiple selection, date, heure, champ géocodé, selection carto,
  etc.)

* Une fois terminé, le formulaire est généré et une URL permet d'y acceder. 
  (par exemple http://forms.notmyidea.org/alternatives).

* Une API REST permet d'autres applications d'accéder aux informations et d'en
  ajouter / modifier de nouvelles.

* Il est maintenant possible de donner l'URL à qui voudra en faire bon usage.
  Nimporte qui peut ajouter des informations. On peut également imaginer une
  manière de modérer les modifications si besoin est.

* Bien sur, la dernière phase est la plus interessante: il est possible de
  filtrer les informations par lieu, catégorie ou date, le tout soit via une
  API REST, soit via une jolie carte et quelques controles bien placés, dans le
  navigateur.

Vous avez du remarquer que le processus de création d'un formulaire est
volontairement très simple. L'idée est que n'importe qui puisse créer des
cartes facilement, en quelques clics. Si une API bien pensée suit, on peut
imaginer faire de la validation coté serveur et même faire des applications
pour téléphone assez simplement.

Pour aller un peu plus loin, si on arrive à penser un format de description
pour le formulaire, il sera possible de construire les formulaires de manière
automatisée sur différentes plateformes et également sur des clients
génériques.

Voici quelques autres exemples d'ou ce projet pourrait être utile:

Designer des formulaires spécialisés pour les applications mobiles OSM
----------------------------------------------------------------------

1. Dans une "mapping party", on choisit un sujet particulier à cartographier et
   on design un formulaire (liste des champs (tags) a remplir + description +
   le type d'information)
2. Sur place, les utilisateurs remplissent les champs du formulaire avec ce
   qu'ils voient. Les champs géolocalisé peuvent être remplis automatiquement
   avec la geolocalisation du téléphone.
3. À la fin de la journée, il est possible de voir une carte des contributions,
   avec le formulaire choisi.
4. Un script peut importer les resultats et les publier vers Open Street Map.

Quelques exemples incluent le recensement des points de recyclage, des endroits
accessibles (pour les fauteuils roulants par exemple), des points ou il y à de
la publicité (la plupart des villes ne les recensent pas!) etc.

Un backend SIG simple à utiliser
--------------------------------

Disons que vous êtes developeur mobile. vous ne voulez pas vous encombrer avec
PostGIS ou écrire du code specifique pour récupérer et insérer des données SIG!
Vous avez besoin de *Carto-Forms*! Une API simple vous aide à penser vos
modèles et vos formulaires, et cette même API vous permet d'insérer et de
récupérer des données. Vous pouvez vous concentrer sur votre application et non
pas surla manière dont les données géographiques sont stockées et gérées.

En d'autres termes, vous faites une distinciton entre le stockage des
informations et leur affichage.

Si vous êtes un developeur django, plomino, drupal etc. vous pouvez developer
un module pour "plugger" votre interface utilisateur avec celle de
*Carto-Forms*. De cette manière, il est possibnle d'exposer les formulaires aux
utilisateurs de vos backoffices. De la même manière, il est possible d'écrire
des widgets qui consomment des données et les affichent (en utilisant par
exemple une bibliothèque javascript de webmapping).

Un outil de visualisation
-------------------------

Il est possible d'explorer mon jeu de données en utilisant des filtres sur
chacun de mes champs. Le faceting peut etre une idée pour faciliter ce
filtrage. Une carte affiche le resultat et il est possible de télécharger les
données brutes (geojson, xml). Idéalement, le mieux serait d'obtenir ces
données filtrées directement depuis une API Web.

Ça n'existe pas déjà tout ça ?
===============================

Bien sur, il y à google forms, wui vous permet de faire ce genre de choses,
mais comme je l'ai précisé plus haut, il ne s'agit pas exactement de la même
chose.

Nous avons découvert https://webform.com qui permet de créer des formulaires
avec un système de drag'n'drop. J'adorerais reproduire quelque chose de
similaire pour l'interface utilisateur. Par contre ce projet ne gère pas les
appels via API et les informations de géolocalisation …

http://mapbox.com fait également un superbe travail autour de la cartographie,
mais ne prends pas en compte le coté autogénération de formulaires…

On est parti ?!
===============

Comme vous avez pu vous en rendre compte, il ne s'agit pas d'un problème
outrageusement complexe. On à pas mal disucté avec Mathieu, à propos de ce
qu'on souhaite faire et du comment. Il se trouve qu'on peut surement s'en
sortir avec une solution élégante sans trop de problèmes. Mathieu est habitué à
travailler autour des projets de SIG (ce qui est parfait parce que ce n'est pas
mon cas) et connaît son sujet. Une bonne opportunité d'apprendre!

On sera tous les deux à `Djangocong`_ le 14 et 15 Avril, et on prévoit une
session de *tempête de cerveau* et un sprint sur ce projet. Si vous êtes dans
le coin et que vous souhaitez discuter ou nous filer un coup de pate, n'hésitez
pas!

On ne sait pas encore si on utiliser django ou quelque chose d'autre. On à
pensé un peu à CouchDB, son système de couchapps et geocouch, mais rien n'est
encore gravé dans le roc! N'hésitez pas à proposer vos solutions ou
suggestions.

Voici le document etherpad sur lequel on à travaillé jusqu'à maintenant:
http://framapad.org/carto-forms. N'hésitez pas à l'éditer et à ajouter vos
commentaires, c'est son objectif!

.. _Djangocong:  http://rencontres.django-fr.org
.. _Mathieu: http://blog.mathieu-leplatre.info/
.. _Makina Corpus: http://makina-corpus.com
