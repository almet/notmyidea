PyconFR 2015 — SQL Alchemy
##########################

:date: 2015.10.17
:category: pyconfr2015
:unlisted: true

.. note::

  Voici quelques notes prises durant la PyconFR 2015, à Pau. N'hésitez pas
  à les completer si besoin.

Speaker: David Allouche

SQL Alchemy vous permet de produire le SQL que vous voulez. Il faut que vous
souhaitiez comprendre ce que va etre produit.

Déclaratif:

- On créé des classes qui representent nos tables, et les liaisons entre les
  tables, en utilisant `relationship` (qui à énormement d'attributs).
- On définit quelles osnt les clés étrangères entre les tables.
- Puis on va définir les attributs qui sont liés entre les tables
  (relationship).
- Pour définir des relations entre les Tables, il est possible d'utiliser des
  chaines de caractère `relationship('OtherTable')`.

- La session es tun concept important.
- Lire efficacement. Attention à ne pas faire énormement de requetes avec
  L'ORM.

**Performance SQL**

- Générer le SQL (python)
- Ne pas faire énormement de petites requetes.

Il est possible de demander à la session de charger les données qui sont
associées. (avec un joinedload). Par defaut, cela risque de charger
l'ensemble des colonnes.

Pour la générer avec SQLAlchemy, il est possible de faire un
`.query(Table).join(Table).join(Table2).filter_by(field=value)`

En pratique, le mieux est de lister clairemnet le nom des tables

2ème partie:

Pour de l'import de données, 

- first() fait une requete SQL. A éviter dans les boucles
- session.flush() c'est quand la session écrit en base tout ce qui est en cours
  dans la transaction. Par default, la session fait un flush avant chaque
  requete.
- une option backçpopulates mets à jour la liste des documents associés à une
  table qui à une foreign key.
  backref modifie implicitement la classe associée. Il est recommandé
  d'utiliser `back_populates` et non pas `backref`.
- `subqueryload` permet de générer une requete séparée plutôt qu'une jointure.
