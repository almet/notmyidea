PyconFR 2015 — Geoalchemy
#########################

:date: 2015.10.17
:category: pyconfr2015
:unlisted: true

.. note::

  Voici quelques notes prises durant la PyconFR 2015, à Pau. N'hésitez pas
  à les completer si besoin.

Speaker: Eric Lemoine, Camp to camp. (@elemoine)

Bibliothèque python basée sur SQL alchemy, pour interagir avec des bases de
données geographiques / spatiales.

Une base de donnée optimisée pour representer et rechercher des données qui
representent des objets dans un espace géométrique.

- Il est possible d estocker des ligne,s de polygones, des points. Il y a une
  colonne géometrie pour stocker ces données.

- Il y a aussi des fonctions qui permettent de travailler sur ces données
  (transfomrations, projections, etc).
- Indexs géographiques qui permettent de faire des recherches de manière
  performante.

POSTGIS
-------

POSTGIS s'appuie sur postres pour offrir des types géographiques, des fonctions
et des indexes (R-Tree), qui permettent de ranger les géométries dans des
"boites englobantes".

Pour créer une base de données postgis, il faut faire un "create extension
postgis", ce qui installe tout ce dont on a besoin.

il est possible d'apeller `GEOMETRY(POINT)` par exemple.

`ST_GeomFromText('POINT(lat long)')` permet de convertir un point dans un objet
geometrie interne à postgres.

`ST_DWithin` permet de trouver les personnes qui sont autour d'un rayon donné.

L'ensemble des fonctions proposées par postgres commencent par `ST_*`

SQLAlchemy
----------

Il s'agit d'une bote à outil qui permet de faire des requetes de manière
simple. Il y a une philosophie forte.

- Il ne sohaite pas cacher la base de données
- C'est un language pour faire du SQL en python
- Rien n'est caché.
- Fourni un vocabulaire riche pour générer le SQL
- L'objectif est de changer la manière dont on pense à SQL, redonner le gout du
  SQL aux developeurs.

Deux parties:
- ORM
- CORE

Il est possible d'utiliser simplement le core si l'on sohaite (sans utiliser
l'ORM)

Core
~~~~

Il est possible d'utiliser SQL Alchemy pour générer les tables à l'origine.
Core permet d'utiliser des tables, et d'executer une insertion, depuis python.
Il est possible de representer les requetes avec des methodes chainées
`select().where()` etc.

Le "core" ne fait pas de mapping du tout, il manipule des Tables SQLA
directement.

ORM
~~~

L'ORM fait, lui, du mapping. C'est cette couche que l'on va utiliser dans une
application Web complexe par exemple.

- il est possible de travailler avec une session `Session()` puis on effectue
  des opérations et on `commit()`.

GeoAlchemy
==========

- Créé en 2009, pour supporter uniquement postgis.
- Depuis, d'autres bases de données (MySQL, Spatialite, MySQL server) etc.
- Réécriture depuis grace à la nouvelle API de SQLAlechemy, mais perte du
  support d'autres backends.
- Finalement, retour sur POSTGIS uniquement, pour évite d'avoir à supporter les
  différences de tous les backends.

Features
--------

Très simple de s'intégrer avec les features de POSTGIS, par exemple en
déclarant une colonne en tant que "Géometrie".

Exemple: session.query(Lake).filter(Lake.geom.ST_Buffer(2).ST_Area) permet de
lister l'ensemble des lacs avec une aire de 2 au moins.

S'intègre bien avec des services existants (shapely, pyramid, etc).

Utilisation de geojsondumps pour representer des features en geojson.

Status
------

Le projet est completement documenté sur read the docs. La documentation est
assez complete et solide. Il est intégralement testé, sur differentes versions
de python, sqlalchemy et postgres.

3 ou 4 developeurs actifs sur le projet, ça fonctionne plutôt bien. Pour
  contribuer, il est possible de faire cela sur github.

  Slides de la presentation sur http://erliem.net/talks/pyconfr2015

Resources:

- https://pypi.python.org/pypi/Shapely - Manipulation and analysis of geometric
  objects in the Cartesian plane.

Question:

- Dans les exemples geoalchemy, les données geométriques sont passées sous
  forme de chaine. Est-ce normal ? Oui.
- Les rasters sont également supportés.
