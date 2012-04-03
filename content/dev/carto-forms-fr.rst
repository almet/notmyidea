Carto-forms
###########

:slug: carto-forms
:date: 02-04-2012
:author: Alexis Métaireau, Mathieu Leplatre
:tags: GIS, forms
:lang: fr

On a un plan. Un "truc de ouf".

À plusieurs reprises, des amis m'ont demandé de leur coder la même chose, à
quelques détails près: une page web avec un formulaire qui permettrait de
soumettre des informations géographiques, lié à une carte et des manières de
filtrer l'information.

L'idée fait son bout de chemin, et je commence à penser qu'on peut même avoir
quelque chose de vraiment flexible et utile. J'ai nommé le projet *carto-forms*
pour l'instant (mais c'est uniquement un nom de code).

Pour résumer: et si on avait un moyen de construire des formulaires, un peu
comme Google forms, mais avec des informations géographiques en plus?

Si vous ne connaissez pas Google forms, il s'agit d'une interface simple
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
sont à même de les intéresser.

Imaginez le cas suivant:

1. Dans une "mapping party", on choisit un sujet particulier à cartographier et
   on design un formulaire (liste des champs (tags) a remplir + description +
   le type d'information) ;
2. Sur place, les utilisateurs remplissent les champs du formulaire avec ce
   qu'ils voient. Les champs géolocalisés peuvent être remplis automatiquement
   avec la géolocalisation du téléphone ;
3. À la fin de la journée, il est possible de voir une carte des contributions,
   avec le formulaire choisi ;
4. Un script peut importer les résultats et les publier vers OpenStreetMap.

Quelques cas d'utilisation
==========================

J'arrive à imaginer différents cas d'utilisation pour cet outil. Le premier est
celui que j'ai approximativement décrit plus haut: la génération de cartes de
manière collaborative, avec des filtres à facettes. Voici un flux d'utilisation
général:

* Un "administrateur" se rend sur le site web et crée un nouveau formulaire
  pour l'ensemble des évènements alternatifs. Il crée les champs suivants:
  
  * Nom: le champ qui contient le nom de l'évènement.

  * Catégorie: la catégorie de l'évènement (marche, concert, manifestation…).
    Il peut s'agir d'un champ à multiples occurrences.

  * Le lieu de l'évènement. Celui-ci peut être donné soit par une adresse soit
    en sélectionnant un point sur une carte.

  * Date: la date de l'évènement (un "date picker" peut permettre cela
    facilement)

  Chaque champ dans le formulaire a des informations sémantiques associées
  (oui/non, multiple sélection, date, heure, champ géocodé, sélection carto,
  etc.)

* Une fois terminé, le formulaire est généré et une URL permet d'y accéder. 
  (par exemple http://forms.notmyidea.org/alternatives).

* Une API REST permet à d'autres applications d'accéder aux informations et d'en
  ajouter / modifier de nouvelles.

* Il est maintenant possible de donner l'URL à qui voudra en faire bon usage.
  N'importe qui peut ajouter des informations. On peut également imaginer une
  manière de modérer les modifications si besoin est.

* Bien sur, la dernière phase est la plus intéressante: il est possible de
  filtrer les informations par lieu, catégorie ou date, le tout soit via une
  API REST, soit via une jolie carte et quelques contrôles bien placés, dans le
  navigateur.

Vous avez dû remarquer que le processus de création d'un formulaire est
volontairement très simple. L'idée est que n'importe qui puisse créer des
cartes facilement, en quelques clics. Si une API bien pensée suit, on peut
imaginer faire de la validation coté serveur et même faire des applications
pour téléphone assez simplement.

Pour aller un peu plus loin, si on arrive à penser un format de description
pour le formulaire, il sera possible de construire les formulaires de manière
automatisée sur différentes plateformes et également sur des clients
génériques.

On imagine pas mal d'exemples pour ce projet: des points de recyclage, les
endroits accessibles (pour fauteuils roulants etc.), identification des arbres,
bons coins à champignons, recensement des espèces en voie de disparition
(l'aigle de Bonelli est actuellement suivi en utilisant une feuille de calcul
partagée !), suivi des espèces dangereuses (le frelon asiatique par exemple),
cartographier les points d'affichage publicitaires, participation citoyenne 
(graffitis, nids de poule, voir http://fixmystreet.ca), geocaching,
trajectoires (randonnées, coureurs, cyclistes)…

Voici quelques exemples où ce projet pourrait être utile (la liste n'est pas
exhaustive):

Un backend SIG simple à utiliser
--------------------------------

Disons que vous êtes développeur mobile. Vous ne voulez pas vous encombrer avec
PostGIS ou écrire du code spécifique pour récupérer et insérer des données SIG!
Vous avez besoin de *Carto-Forms*! Une API simple vous aide à penser vos
modèles et vos formulaires, et cette même API vous permet d'insérer et de
récupérer des données. Vous pouvez vous concentrer sur votre application et non
pas sur la manière dont les données géographiques sont stockées et gérées.

En d'autres termes, vous faites une distinction entre le stockage des
informations et leur affichage.

Si vous êtes un développeur django, plomino, drupal etc. vous pouvez développer
un module pour "plugger" vos modèles et votre  interface utilisateur avec celle
de *Carto-Forms*. De cette manière, il est possible d'exposer les formulaires
aux utilisateurs de vos backoffices. De la même manière, il est possible
d'écrire des widgets qui consomment des données et les affichent (en utilisant
par exemple une bibliothèque javascript de webmapping).

Un outil de visualisation
-------------------------

Puisque les données peuvent être proposées de manière automatisée en utilisant
l'API, vous pouvez utiliser la page de résultat de Carto-forms comme un outil
de visualisation.

Il est possible d'explorer mon jeu de données en utilisant des filtres sur
chacun des champs. La recherche à facettes peut être une idée pour faciliter ce
filtrage. Une carte affiche le résultat. Vous avez l'impressoin d'être en face
d'un système d'aide à la décision !

Évidemment, il est possible de télécharger les données brutes (geojson, xml).
Idéalement, le mieux serait d'obtenir ces données filtrées directement depuis
une API Web, et un lien permet de partager la page avec l'état des filtres et
le niveau de zoom / la localisation de la carte.

Un service générique pour gérer les formulaires
-----------------------------------------------

Si vous souhaitez générer un fichier de configuration (ou ce que vous voulez,
messages emails, …) vous aurez besoin d'un formulaire et d'un template pour
injecter les données proposées par les utilisateurs et récupérer un résultat.

Un service de gestion des formulaires pourrait être utile pour créer des
formulaires de manière automatique et récupérer les données "nettoyées" et
"validées".

On peut imaginer par exemple l'utilisation d'un système de templates externe
reposant sur *carto-forms*. Celui-ci "parserait" le contenu des templates et 
pourrait le lier aux informations ajoutées par les utilisateurs via un formulaire.

Pour ce cas particulier, il n'y a pas besoin d'informations géographiques
(SIG). Il s'agit quasiment du service proposé actuellement par Google forms.

Ça n'existe pas déjà tout ça ?
===============================

Bien sur, il y a Google forms, qui vous permet de faire ce genre de choses,
mais comme je l'ai précisé plus haut, il ne s'agit pas exactement de la même
chose.

Nous avons découvert https://webform.com qui permet de créer des formulaires
avec un système de drag'n'drop. J'adorerais reproduire quelque chose de
similaire pour l'interface utilisateur. Par contre ce projet ne gère pas les
appels via API et les informations de géolocalisation …

L'idée de http://thoth.io est également assez sympathique: une api très 
simple pour stocker et récupérer des données. En plus de ça, *carto-forms*
proposerait de la validation de données et proposerait un support des points
SIG (point, ligne, polygone).

http://mapbox.com fait également un superbe travail autour de la cartographie,
mais ne prends pas en compte le coté auto-génération de formulaires…

On est parti ?!
===============

Comme vous avez pu vous en rendre compte, il ne s'agit pas d'un problème
outrageusement complexe. On a pas mal discuté avec Mathieu, à propos de ce
qu'on souhaite faire et du comment. Il se trouve qu'on peut sûrement s'en
sortir avec une solution élégante sans trop de problèmes. Mathieu est habitué à
travailler autour des projets de SIG (ce qui est parfait parce que ce n'est pas
mon cas) et connaît son sujet. Une bonne opportunité d'apprendre!

On sera tous les deux à `Djangocong`_ le 14 et 15 Avril, et on prévoit une
session de *tempête de cerveau* et un sprint sur ce projet. Si vous êtes dans
le coin et que vous souhaitez discuter ou nous filer un coup de patte,
n'hésitez pas!

On ne sait pas encore si on utilisera django ou quelque chose d'autre. On a
pensé un peu à CouchDB, son système de couchapps et geocouch, mais rien n'est
encore gravé dans le marbre ! N'hésitez pas à proposer vos solutions ou
suggestions.

Voici le document etherpad sur lequel on a travaillé jusqu'à maintenant:
http://framapad.org/carto-forms. N'hésitez pas à l'éditer et à ajouter vos
commentaires, c'est son objectif!

Merci à `Arnaud`_ pour la relecture et la correction de quelques typos dans le
texte :)

.. _Djangocong:  http://rencontres.django-fr.org
.. _Mathieu: http://blog.mathieu-leplatre.info/
.. _Arnaud: http://sneakernet.fr/
.. _Makina Corpus: http://makina-corpus.com
