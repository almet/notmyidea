Service de nuages : Stocker et interroger les permissions avec Kinto
####################################################################

:lang: fr
:date: 2015-05-26
:summary: Comment faire pour stocker et interroger la base de données au sujet des permissions avec Kinto ?


*Cet article est repris depuis le blog « Service de Nuages » de mon équipe à Mozilla*


**tl;dr: On a maintenant un super système de permission mais comment faire pour stocker et interroger ces permissions de manière efficace ?**

La problématique
================

Maintenant que nous avons défini un modèle de gestion des permissions
sur les objets qui nous satisfait, le problème est de stocker ces
permissions de manière efficace afin de pouvoir autoriser ou interdire
l'accès à un objet pour la personne qui fait la requête.

Chaque requête sur notre API va générer une ou plusieurs demandes
d'accès, il faut donc que la réponse soit très rapide sous peine
d'impacter la vélocité du service.


Obtenir la liste des "principals" d'un utilisateur
==================================================

Les *principals* de l'utilisateur correspondent à son ``user_id``
ainsi qu'à la liste des identifiants des groupes dans lesquels il a
été ajouté.

Pour éviter de recalculer les *principals* de l'utilisateur à chaque
requête, le mieux reste de maintenir une liste des *principals* par
utilisateur.

Ainsi lorsqu'on ajoute un utilisateur à un groupe, il faut bien penser
à ajouter le groupe à la liste des *principals* de l'utilisateur.

Ça se complexifie lorsqu'on ajoute un groupe à un groupe.

Dans un premier temps interdire l'ajout d'un groupe à un groupe est
une limitation qu'on est prêts à accepter pour simplifier le
modèle.

L'avantage de maintenir la liste des *principals* d'un utilisateur
lors de la modification de cette liste c'est qu'elle est déjà
construite lors des lectures, qui sont dans notre cas plus fréquentes
que les écritures.

Cela nécessite de donner un identifiant unique aux groupes pour tous
les *buckets*.

Nous proposons de de les nommer avec leur URI:
``/buckets/blog/groups/moderators``


Obtenir la liste des "principals" d'un ACE
==========================================

    Rappel, un "ACE" est un *Access Control Entry*, un des éléments
    d'une ACL (e.g. *modifier un enregistrement*).

Avec le `système de permissions choisi
<{filename}/code/2015-05-01-cliquet-permissions.rst>`_, les permissions d'un
objet héritent de celle de l'objet parent.

Par exemple, avoir le droit d'écriture sur un *bucket* permet la
création des permissions et la modification de tous ses records.

Ce qui veut dire que pour obtenir la liste complète des *principals*
ayant une permission sur un objet, il faut regarder à plusieurs
endroits.

Rémy a `décrit dans un gist la liste d'héritage de chaque permission <https://gist.github.com/Natim/77c8f61c1d42e476cef8#file-permission-py-L9-L52>`_.

Prenons l'exemple de l'ajout d'un record dans une collection.

Le droit ``records:create`` est obtenu si l'on a l'un des droits suivants:

- ``bucket:write``
- ``collection:write``
- ``records:create``

Notre première idée était de stocker les permissions sur chaque objet
et de maintenir la liste exhaustive des permissions lors d'une
modification d'ACL. Cependant cela nécessitait de construire cette
liste lors de l'ajout d'un objet et de mettre à jour tout l'arbre lors
de sa suppression.  (*Je vous laisse imaginer le nombre d'opérations
nécessaires pour ajouter un administrateur sur un *bucket* contenant
1000 collections avec 100000 records chacune.*)

La solution que nous avons désormais adoptée consiste à stocker les
*principals* de chaque *ACE* (*qui* a le droit de faire telle action
sur l'objet), et de faire l'union des *ACE* hérités, afin de les
croiser avec les *principals* de l'utilisateur :


    (ACE(object, permission) ∪ inherited_ACE) ∩ PRINCIPALS(user)

Par exemple l'ACE: ``/buckets/blog/collections/article:records:create`` hérite de
l'ACE ``/buckets/blog/collections/article:write`` et de ``/buckets/blog:write`` :

    (ACE(/buckets/blog/collections/article:records:create) ∪ ACE(/buckets/blog/collections/article:write) ∪ ACE(/buckets/blog:write)) ∩ PRINCIPALS('fxa:alexis')


Récupérer les données de l'utilisateur
======================================

La situation se corse lorsqu'on souhaite limiter la liste des
*records* d'une collection à ceux accessibles pour l'utilisateur, car
on doit faire cette intersection pour tous les *records*.

Une première solution est de regarder si l'utilisateur est mentionné
dans les *ACL*s du *bucket* ou de la *collection*:

Ensuite, si ce n'est pas le cas, alors on filtre les *records* pour
lesquels les *principals* correspondent à ceux de l'utilisateur.


.. code-block:: python

    principals = get_user_principals(user_id)
    can_read_all = has_read_perms(bucket_id, collection_id,
                                  principals)
    if can_read_all:
        records = get_all_records(bucket_id, collection_id,
                                  filters=[...])
    else:
        records = filter_read_records(bucket_id, collection_id,
                                      principals=principals,
                                      filters=[...])


Il faudra faire quelque chose de similaire pour la suppression
multiple, lorsqu'un utilisateur souhaitera supprimer des
enregistrements sur lesquels il a les droits de lecture mais pas
d'écriture.


Le modèle de données
====================

Pour avoir une idée des requêtes dans un backend SQL, voyons un peu ce
que donnerait le modèle de données.


Le format des ID
----------------

Utiliser des URI comme identifiant des objets présente de nombreux
avantages (lisibilité, unicité, cohérence avec les URLs)

* bucket: ``/buckets/blog``
* groupe: ``/buckets/blog/group/moderators``
* collection: ``/buckets/blog/collections/articles``
* record: ``/buckets/blog/collections/articles/records/02f3f76f-7059-4ae4-888f-2ac9824e9200``


Les tables
----------

Pour le stockage des principals et des permissions:

.. code-block:: sql

    CREATE TABLE user(id TEXT, principals TEXT[]);
    CREATE TABLE perms(ace TEXT, principals TEXT[]);

La table *perms* va associer des *principals* à chaque *ACE*
(e.g.``/buckets/blog:write``).

Pour le stockage des données:

.. code-block:: sql

    CREATE TABLE object(id TEXT, type TEXT, parent_id TEXT, data JSONB,
                        write_principals TEXT[], read_principals TEXT[]);

La colonne *parent_id* permet de savoir à qui appartient l'objet
(e.g. groupe d'un *bucket*, collection d'un *bucket*, *record* d'une
collection, ...).


Exemple d'utilisateur
---------------------

.. code-block:: sql

    INSERT INTO user (id, principals)
         VALUES ('fxa:alexis', '{}');

    INSERT INTO user (id, principals)
         VALUES ('fxa:natim',
                 '{"/buckets/blog/groups/moderators"}');


Exemple d'objets
----------------

Bucket
::::::

.. code-block:: sql

    INSERT INTO object (id, type, parent_id, data,
                        read_principals, write_principals)
    VALUES (
        '/buckets/blog',
        'bucket',
        NULL,
        '{"name": "blog"}'::JSONB,
        '{}', '{"fxa:alexis"}');


Group
:::::

.. code-block:: sql

    INSERT INTO object (id, type, parent_id, data,
                        read_principals, write_principals)
    VALUES (
        '/buckets/blog/groups/moderators',
        'group',
        '/buckets/blog',
        '{"name": "moderators", "members": ['fxa:natim']}'::JSONB,
        '{}', '{}');


Ce groupe peut être gére par ``fxa:alexis`` puisqu'il a la permission
``write`` dans le *bucket* parent.


Collection
::::::::::

.. code-block:: sql

    INSERT INTO object (id, type, parent_id, data,
                        read_principals, write_principals)
    VALUES (
        '/buckets/blog/collections/articles',
        'collection',
        '/buckets/blog',
        '{"name": "article"}'::JSONB,
        '{"system.Everyone"}',
        '{"/buckets/blog/groups/moderators"}');

Cette collection d'articles peut être lue par tout le monde,
et gérée par les membres du groupe ``moderators``, ainsi que
``fxa:alexis``, via le *bucket*.


Records
:::::::

.. code-block:: sql

    INSERT INTO object (id, type, parent_id, data,
                        read_principals, write_principals)
    VALUES (
        '/buckets/blog/collections/articles/records/02f3f76f-7059-4ae4-888f-2ac9824e9200',
        'record',
        '/buckets/blog/collections/articles',
        '{"name": "02f3f76f-7059-4ae4-888f-2ac9824e9200",
          "title": "Stocker les permissions", ...}'::JSONB,
        '{}', '{}');


Interroger les permissions
--------------------------

Obtenir la liste des "principals" d'un ACE
::::::::::::::::::::::::::::::::::::::::::

Comme vu plus haut, pour vérifier une permission, on fait l'union des
*principals* requis par les objets hérités, et on teste leur
intersection avec ceux de l'utilisateur:

.. code-block:: sql

   WITH required_principals AS (
        SELECT unnest(principals) AS p
          FROM perms
         WHERE ace IN (
            '/buckets/blog:write',
            '/buckets/blog:read',
            '/buckets/blog/collections/article:write',
            '/buckets/blog/collections/article:read')
    ),
    user_principals AS (
        SELECT unnest(principals)
          FROM user
         WHERE id = 'fxa:natim'
    )
    SELECT COUNT(*)
      FROM user_principals a
     INNER JOIN required_principals b
        ON a.p = b.p;


Filtrer les objets en fonction des permissions
::::::::::::::::::::::::::::::::::::::::::::::

Pour filtrer les objets, on fait une simple intersection de liste
(*merci PostgreSQL*):

.. code-block:: sql


    SELECT data
      FROM object o, user u
     WHERE o.type = 'record'
       AND o.parent_id = '/buckets/blog/collections/article'
       AND (o.read_principals && u.principals OR
            o.write_principals && u.principals)
       AND u.id = 'fxa:natim';

Les listes s'indexent bien, notamment grâce aux `index GIN
<http://www.postgresql.org/docs/current/static/indexes-types.html>`_.


Avec Redis
----------

*Redis* présente plusieurs avantages pour ce genre de
problématiques. Notamment, il gère les *set* nativement (listes de
valeurs uniques), ainsi que les opérations d'intersection et d'union.

Avec *Redis* on peut écrire l'obtention des *principals* pour un *ACE*
comme cela :

.. code-block:: redis

    SUNIONSTORE temp_perm:/buckets/blog/collections/articles:write  permission:/buckets/blog:write  permission:/buckets/blog/collections/articles:write
    SINTER temp_perm:/buckets/blog/collections/articles:write principals:fxa:alexis

- ``SUNIONSTORE`` permet de créer un set contenant les éléments de
  l'union de tous les set suivants. Dans notre cas on le nomme
  ``temp_perm:/buckets/blog/collections/articles:write`` et il contient
  l'union des sets d'ACLs suivants:
  - ``permission:/buckets/blog:write``
  - ``permission:/buckets/blog/collections/articles:write``
- ``SINTER`` retourne l'intersection de tous les sets passés en paramètres dans notre cas :
  - ``temp_perm:/buckets/blog/collections/articles:write``
  - ``principals:fxa:alexis``

Plus d'informations sur :
- http://redis.io/commands/sinter
- http://redis.io/commands/sunionstore

Si le set résultant de la commande ``SINTER`` n'est pas vide, alors
l'utilisateur possède la permission.

On peut ensuite supprimer la clé temporaire ``temp_perm``.

En utilisant ``MULTI`` on peut `même faire tout cela au sein d'une
transaction <https://gist.github.com/Natim/77c8f61c1d42e476cef8#file-permission-py-L117-L124>`_
et garantir ainsi l'intégrité de la requête.


Conclusion
==========

La solution a l'air simple mais nous a demandé beaucoup de réflexion
en passant par plusieurs propositions.

L'idée finale est d'avoir :

- Un backend spécifique permettant de stocker les *principals* des
  utilisateurs et des *ACE* (e.g. avec les sets Redis) ;
- La liste des principals read et write sur la table des objets.

C'est dommage d'avoir le concept de permissions à deux endroits, mais
cela permet de connaître rapidement la permission d'un utilisateur sur
un objet et également de pouvoir récupérer tous les objets d'une
collection pour un utilisateur si celui-ci n'a pas accès à tous les
records de la collection, ou toutes les collections du bucket.
