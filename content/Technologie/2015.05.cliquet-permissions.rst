Service de nuages : La gestion des permissions
##############################################

:lang: fr
:summary: Démystification du vocabulaire des permissions et proposition d'implémentation pour Kinto

*Cet article est repris depuis le blog « Service de Nuages » de mon équipe à Mozilla*

Dans le cadre de la création d'un service de stockage de données personnelles
(Kinto), la gestion des permissions est un des gros challenges : qui doit avoir
accès à quoi, et comment le définir ?

**tl;dr: Quelques retours sur le vocabulaire des systèmes de permission et sur nos idées pour l'implementation des permissions dans un stockage générique.**

La problématique
================

La problématique est simple : des données sont stockées en ligne, et il
faut un moyen de pouvoir les partager avec d'autres personnes.

En regardant les cas d'utilisations, on se rend compte qu'on a plusieurs types
d'utilisateurs :

- les utilisateurs "finaux" (vous) ;
- les applications qui interagissent en leurs noms.

Tous les intervenants n'ont donc pas les mêmes droits : certains doivent
pouvoir lire, d'autres écrire, d'autres encore créer de nouveaux
enregistrements, et le contrôle doit pouvoir s'effectuer de manière fine : il
doit être possible de lire un enregistrement mais pas un autre, par exemple.

Nous sommes partis du constat que les solutions disponibles n'apportaient pas
une réponse satisfaisante à ces besoins.


Un problème de vocabulaire
==========================

Le principal problème rencontré lors des réflexions fût le vocabulaire.

Voici ci-dessous une explication des différents termes.


Le concept de « principal »
---------------------------

Un *principal*, en sécurité informatique, est une entité qui peut être
authentifiée par un système informatique. [#]_ En Français il s'agit
du « commettant », l'acteur qui commet l'action (oui, le terme est conceptuel !)

Il peut s'agir aussi bien d'un individu, d'un ordinateur, d'un
service ou d'un groupe regroupant l'une de ces entités, ce qui
est plus large que le classique « *user id* ».

Les permissions sont alors associées à ces *principals*.

Par exemple, un utilisateur est identifié de manière unique lors de la
connexion par le système d'authentification dont le rôle est de
définir une liste de *principals* pour l'utilisateur se connectant.

.. [#] Pour en savoir plus sur les *principals* :
       https://en.wikipedia.org/wiki/Principal_%28computer_security%29


La différence entre rôle et groupe
----------------------------------

De but en blanc, il n'est pas évident de définir précisément la
différence entre ces deux concepts qui permettent d'associer
des permissions à un groupe de *principals*. [#]_

La différence est principalement sémantique. Mais on peut y voir une
différence dans la « direction » de la relation entre les deux concepts.

- Un rôle est une liste de permissions que l'on associe à un *principal*.
- Un groupe est une liste de *principals* que l'on peut associer à une permission.

.. [#] Plus d'informations :
       http://stackoverflow.com/questions/7770728/group-vs-role-any-real-difference


La différence entre permission, ACL, ACE
----------------------------------------

.. epigraph::

  Une ACL est une liste d’Access Control Entry (ACE) ou entrée de contrôle d'accès
  donnant ou supprimant des droits d'accès à une personne ou un groupe.

  -- https://fr.wikipedia.org/wiki/Access_Control_List

Je dirais même plus, dans notre cas, « à un *principal* ». Par exemple:

.. code-block:: text

    create_record: alexis,remy,tarek

Cet ACE donne la permission ``create`` sur l'objet ``record`` aux
utilisateurs Tarek, Rémy et Alexis.


La délégation de permissions
============================

Imaginez l'exemple suivant, où un utilisateur stocke deux types de données en
ligne :

- des contacts ;
- une liste de tâches à faire qu'il peut associer à ses contacts.

L'utilisateur a tous les droits sur ses données.

Cependant il utilise deux applications qui doivent elles avoir un accès restreint :

- une application de gestion des contacts à qui il souhaite déléguer
  la gestion intégrale de ses contacts : ``contacts:write`` ;
- une application de gestion des tâches à qui il souhaite déléguer la
  gestion des tâches : ``contacts:read tasks:write``

Il souhaite que son application de contacts ne puisse pas accéder à
ses tâches et que son application de tâches ne puisse pas modifier ses
contacts existants, juste éventuellement en créer de nouveaux.

Il lui faut donc un moyen de déléguer certains de ses droits à un tiers
(l'application).

C'est précisément le rôle des `scopes OAuth2
<http://tools.ietf.org/html/rfc6749#page-23>`_.

Lors de la connexion d'un utilisateur, une fenêtre lui demande quels
accès il veut donner à l'application qui va agir en son nom.

Le service aura ensuite accès à ces *scopes* en regardant le jeton
d'authentification utilisé. Cette information doit être
considérée comme une entrée utilisateur (c'est à dire qu'on ne peut
pas lui faire confiance). Il s'agit de ce que l'utilisateur souhaite.

Or, il est également possible que l'utilisateur n'ait pas accès aux données
qu'il demande. Le service doit donc utiliser deux niveaux de permissions :
celles de l'utilisateur, et celles qui ont été déléguées à l'application.


Espace de noms
==============

Dans notre implémentation initiale de *Kinto* (notre service de stockage en
construction), l'espace de nom était implicite : les données stockées étaient
nécessairement celles de l'utilisateur connecté.

Les données d'un utilisateur étaient donc cloisonnées et impossible à partager.

L'utilisation d'espaces de noms est une manière simple de gérer le partage des données.

Nous avons choisi de reprendre le modèle de GitHub et de Bitbucket, qui
utilisent les « organisations » comme espaces de noms.

Dans notre cas, il est possible de créer des "buckets", qui correspondent à ces
espaces de noms. Un bucket est un conteneur de collections et de groupes
utilisateurs.

Les ACLs sur ces collections peuvent être attribuées à certains groupes du
*bucket* ainsi qu'à d'autres *principals* directement.


Notre proposition d'API
=======================

Les objets manipulés
--------------------

Pour mettre en place la gestion des permissions, nous avons identifié les
objets suivants :

+-----------------+---------------------------------------------------------+
| Objet           | Description                                             |
+=================+=========================================================+
| **bucket**      | On peut les voir comme des espaces de noms. Ils         |
|                 | permettent d'avoir différentes collections portant      |
|                 | le même nom mais stockées dans différents *buckets* de  |
|                 | manière à ce que les données soient distinctes.         |
+-----------------+---------------------------------------------------------+
| **collection**  | Une liste d'enregistrements.                            |
+-----------------+---------------------------------------------------------+
| **record**      | Un enregistrement d'une collection.                     |
+-----------------+---------------------------------------------------------+
| **group**       | Un groupe de commetants (« *principals* »).             |
+-----------------+---------------------------------------------------------+

Pour la définition des ACLs, il y a une hiérarchie et les objets « héritent » des
ACLs de leur parents :

.. code-block:: text

               +---------------+
               | Bucket        |
               +---------------+
        +----->+ - id          +<---+
        |      | - permissions |    |
        |      +---------------+    |
        |                           |
        |                           |
        |                           |
        |                           |
        |                           |
    +---+-----------+        +------+---------+
    | Collection    |        | Group          |
    +---------------+        +----------------+
    | - id          |        |  - id          |
    | - permissions |        |  - members     |
    +------+--------+        |  - permissions |
           ^                 +----------------+
           |
           |
    +------+---------+
    | Record         |
    +----------------+
    |  - id          |
    |  - data        |
    |  - permissions |
    +----------------+


Les permissions
---------------

Pour chacun de ces objets nous avons identifié les permissions suivantes :

+------------+-----------------------------------------+
| Permission | Description                             |
+============+=========================================+
| **read**   | La permission de lire le contenu de     |
|            | l'objet et de ses sous-objets.          |
+------------+-----------------------------------------+
| **write**  | La permission de modifier et            |
|            | d'administrer un objet et ses sous-     |
|            | objets. La permission *write* permet la |
|            | lecture, modification et suppression    |
|            | d'un objet ainsi que la gestion de ses  |
|            | permissions.                            |
+------------+-----------------------------------------+
| **create** | La permission de créer le sous-objet    |
|            | spécifié. Par exemple:                  |
|            | ``collections:create``                  |
+------------+-----------------------------------------+

À chaque permission spécifiée sur un objet est associée une liste de
*principals*.

Dans le cas de la permission ``create`` on est obligé de spécifier
l'objet enfant en question car un objet peut avoir plusieurs types
d'enfants. Par exemple : ``collections:create``, ``groups:create``.

Nous n'avons pour l'instant pas de permission pour `delete` et `update`,
puisque nous n'avons pas trouvé de cas d'utilisation qui les nécessitent.
Quiconque avec le droit d'écriture peut donc supprimer un enregistrement.

Les permissions d'un objet sont héritées de son parent. Par exemple,
un enregistrement créé dans une collection accessible à tout le monde
en lecture sera lui aussi accessible à tout le monde.

Par conséquent, les permissions sont cumulées. Autrement dit, il n'est pas
possible qu'un objet ait des permissions plus restrictives que son parent.


Voici la liste exhaustive des permissions :

+----------------+------------------------+-----------------------------------+
| Objet          | Permissions associées  | Commentaire                       |
+================+========================+===================================+
| Configuration  | `buckets:create`       | Les *principals* ayant le droit   |
| (.ini)         |                        | de créer un bucket sont définis   |
|                |                        | dans la configuration du serveur. |
|                |                        | (*ex. utilisateurs authentifiés*) |
+----------------+------------------------+-----------------------------------+
| ``bucket``     | `write`                | C'est en quelque sorte le droit   |
|                |                        | d'administration du *bucket*.     |
|                +------------------------+-----------------------------------+
|                | `read`                 | C'est le droit de lire le contenu |
|                |                        | de tous les objets du *bucket*.   |
|                +------------------------+-----------------------------------+
|                | `collections:create`   | Permission de créer des           |
|                |                        | collections dans le *bucket*.     |
|                +------------------------+-----------------------------------+
|                | `groups:create`        | Permission de créer des groupes   |
|                |                        | dans le *bucket*.                 |
+----------------+------------------------+-----------------------------------+
| ``collection`` | `write`                | Permission d'administrer tous les |
|                |                        | objets de la collection.          |
|                +------------------------+-----------------------------------+
|                | `read`                 | Permission de consulter tous les  |
|                |                        | objets de la collection.          |
|                +------------------------+-----------------------------------+
|                | `records:create`       | Permission de créer des nouveaux  |
|                |                        | enregistrement dans la collection.|
+----------------+------------------------+-----------------------------------+
| ``record``     | `write`                | Permission de modifier ou de      |
|                |                        | partager l'enregistrement.        |
|                +------------------------+-----------------------------------+
|                | `read`                 | Permission de consulter           |
|                |                        | l'enregistrement.                 |
+----------------+------------------------+-----------------------------------+
| ``group``      | `write`                | Permission d'administrer le       |
|                |                        | groupe                            |
|                +------------------------+-----------------------------------+
|                | `read`                 | Permission de consulter les       |
|                |                        | membres du groupe.                |
+----------------+------------------------+-----------------------------------+


Les « *principals* »
--------------------

Les acteurs se connectant au service de stockage peuvent s'authentifier.

Ils reçoivent alors une liste de *principals* :

- ``Everyone``: le *principal* donné à tous les acteurs (authentifiés ou pas) ;
- ``Authenticated``: le *principal* donné à tous les acteurs authentifiés ;
- un *principal* identifiant l'acteur, par exemple ``fxa:32aa95a474c984d41d395e2d0b614aa2``

Afin d'éviter les collisions d'identifiants, le *principal* de l'acteur dépend
de son type d'authentification (``system``, ``basic``, ``ipaddr``, ``hawk``,
``fxa``) et de son identifiant (unique par acteur).

En fonction du *bucket* sur lequel se passe l'action, les groupes dont
fait partie l'utilisateur sont également ajoutés à sa liste de
``principals``. ``group:moderators`` par exemple.

Ainsi, si Bob se connecte avec *Firefox Accounts* sur le *bucket*
``servicedenuages_blog`` dans lequel il fait partie du groupe
``moderators``, il aura la liste de *principals* suivante :
``Everyone, Authenticated, fxa:32aa95a474c984d41d395e2d0b614aa2, group:moderators``

Il est donc possible d'assigner une permission à Bob en utilisant l'un de
ces quatre *principals*.

.. note::

    Le *principal* ``<userid>`` dépend du *back-end* d'authentification (e.g.
    ``github:leplatrem``).


Quelques exemples
-----------------

**Blog**

+-------------------------+-------------+---------------------------------+
| Objet                   | Permissions | Principals                      |
+=========================+=============+=================================+
| ``bucket:blog``         | ``write``   | ``fxa:<blog owner id>``         |
+-------------------------+-------------+---------------------------------+
| ``collection:articles`` | ``write``   | ``group:moderators``            |
|                         +-------------+---------------------------------+
|                         | ``read``    | ``Everyone``                    |
+-------------------------+-------------+---------------------------------+
| ``record:569e28r98889`` | ``write``   | ``fxa:<co-author id>``          |
+-------------------------+-------------+---------------------------------+

**Wiki**

+-------------------------+-------------+---------------------------------+
| Object                  | Permissions | Principals                      |
+=========================+=============+=================================+
| ``bucket:wiki``         | ``write``   | ``fxa:<wiki administrator id>`` |
+-------------------------+-------------+---------------------------------+
| ``collection:articles`` | ``write``   | ``Authenticated``               |
|                         +-------------+---------------------------------+
|                         | ``read``    | ``Everyone``                    |
+-------------------------+-------------+---------------------------------+

**Sondages**

+-------------------------+-----------------------+--------------------------+
| Objet                   | Permissions           | Principals               |
+=========================+=======================+==========================+
| ``bucket:poll``         | ``write``             | ``fxa:<admin id>``       |
|                         +-----------------------+--------------------------+
|                         | ``collection:create`` | ``Authenticated``        |
+-------------------------+-----------------------+--------------------------+
| ``collection:<poll id>``| ``write``             | ``fxa:<poll author id>`` |
|                         +-----------------------+--------------------------+
|                         | ``record:create``     | ``Everyone``             |
+-------------------------+-----------------------+--------------------------+

**Cartes colaboratives**

+-------------------------+-----------------------+--------------------------+
| Objet                   | Permissions           | Principals               |
+=========================+=======================+==========================+
| ``bucket:maps``         | ``write``             | ``fxa:<admin id>``       |
|                         +-----------------------+--------------------------+
|                         | ``collection:create`` | ``Authenticated``        |
+-------------------------+-----------------------+--------------------------+
| ``collection:<map id>`` | ``write``             | ``fxa:<map author id>``  |
|                         +-----------------------+--------------------------+
|                         | ``read``              | ``Everyone``             |
+-------------------------+-----------------------+--------------------------+
| ``record:<record id>``  | ``write``             | ``fxa:<maintainer id>``  |
|                         |                       | (*ex. event staff member |
|                         |                       | maintaining venues*)     |
+-------------------------+-----------------------+--------------------------+

**Plateformes**

Bien sûr, il y a plusieurs façons de modéliser les cas d'utilisation typiques.
Par exemple, on peut imaginer une plateforme de wikis (à la wikia.com), où les
wikis sont privés par défaut et certaines pages peuvent être rendues publiques :

+-------------------------+-----------------------+-----------------------------+
| Objet                   | Permissions           | Principals                  |
+=========================+=======================+=============================+
| ``bucket:freewiki``     | ``write``             |``fxa:<administrator id>``   |
|                         +-----------------------+-----------------------------+
|                         | ``collection:create`` | ``Authenticated``           |
|                         +-----------------------+-----------------------------+
|                         | ``group:create``      | ``Authenticated``           |
+-------------------------+-----------------------+-----------------------------+
| ``collection:<wiki id>``| ``write``             | ``fxa:<wiki owner id>``,    |
|                         |                       | ``group:<editors id>``      |
|                         +-----------------------+-----------------------------+
|                         | ``read``              | ``group:<readers id>``      |
+-------------------------+-----------------------+-----------------------------+
| ``record:<page id>``    | ``read``              | ``Everyone``                |
+-------------------------+-----------------------+-----------------------------+



L'API HTTP
----------

Lors de la création d'un objet, l'utilisateur se voit
attribué la permission ``write`` sur l'objet :

.. code-block:: http

    PUT /v1/buckets/servicedenuages_blog HTTP/1.1
    Authorization: Bearer 0b9c2625dc21ef05f6ad4ddf47c5f203837aa32ca42fced54c2625dc21efac32
    Accept: application/json

    HTTP/1.1 201 Created
    Content-Type: application/json; charset=utf-8

    {
        "id": "servicedenuages_blog",
        "permissions": {
            "write": ["fxa:49d02d55ad10973b7b9d0dc9eba7fdf0"]
        }
    }

Il est possible d'ajouter des permissions à l'aide de ``PATCH`` :

.. code-block:: http

    PATCH /v1/buckets/servicedenuages_blog/collections/articles HTTP/1.1
    Authorization: Bearer 0b9c2625dc21ef05f6ad4ddf47c5f203837aa32ca42fced54c2625dc21efac32
    Accept: application/json

    {
        "permissions": {
            "read": ["+system.Everyone"]
        }
    }

    HTTP/1.1 201 Created
    Content-Type: application/json; charset=utf-8

    {
        "id": "servicedenuages_blog",
        "permissions": {
            "write": ["fxa:49d02d55ad10973b7b9d0dc9eba7fdf0"],
            "read": ["system.Everyone"]
        }
    }

Pour le ``PATCH`` nous utilisons la syntaxe préfixée par un ``+`` ou
par un ``-`` pour ajouter ou enlever des *principals* sur un ACL.

Il est également possible de faire un ``PUT`` pour réinitialiser les ACLs,
sachant que le ``PUT`` va ajouter l'utilisateur courant à la
liste automatiquement mais qu'il pourra se retirer avec un ``PATCH``.
Ajouter l'utilisateur courant permet d'éviter les situations où plus
personne n'a accès aux données.


.. note::

    La permission ``create`` est valable pour ``POST`` mais aussi pour ``PUT``
    lorsque l'enregistrement n'existe pas.


Le cas spécifique des données utilisateurs
------------------------------------------

Une des fonctionnalités actuelles de *Kinto* est de pouvoir gérer des
collections d'enregistrements par utilisateur.

Sous *\*nix* il est possible, pour une
application, de sauvegarder la configuration de l'utilisateur courant
dans son dossier personnel sans se soucier de l'emplacement sur
le disque en utilisant ``~/``.

Dans notre cas si une application souhaite sauvegarder les contacts d'un
utilisateur, elle peut utiliser le raccourci ``~`` pour faire référence au
*bucket* **personnel** de l'utilisateur : ``/buckets/~/collections/contacts``

Cette URL retournera le code ``HTTP 307`` vers le *bucket* de l'utilisateur courant :

.. code-block:: http

    POST /v1/buckets/~/collections/contacts/records HTTP/1.1

    {
       "name": "Rémy",
       "emails": ["remy@example.com"],
       "phones": ["+330820800800"]
    }

    HTTP/1.1 307 Temporary Redirect
    Location: /v1/buckets/fxa:49d02d55ad10973b7b9d0dc9eba7fdf0/collections/contacts/records

Ainsi il est tout à fait possible à Alice de partager ses contacts
avec Bob. Il lui suffit pour cela de donner la permission ``read`` à
Bob sur sa collection et de donner l'URL complète
``/v1/buckets/fxa:49d02d55ad10973b7b9d0dc9eba7fdf0/collections/contacts/records``
à Bob.


La délégation des permissions
-----------------------------

Dans le cas de *Kinto*, nous avons défini un format pour restreindre les
permissions via les scopes OAuth2:
``storage:<bucket_id>:<collection_id>:<permissions_list>``.

Ainsi, si on reprend l'exemple précédent de la liste de tâches, il est possible pour
Bob de créer un token OAuth spécifique avec les *scopes* suivants :
``profile storage:todolist:tasks:write storage:~:contacts:read+records:create``

Donc, bien que Bob a la permission ``write`` sur ses contacts,
l'application utilisant ce token pourra uniquement lire les contacts
existants et en ajouter de nouveaux.

Une partie de la complexité est donc de réussir à présenter ces *scopes* de
manière lisible à l'utilisateur, afin qu'il choisisse quelles permissions
donner aux applications qui agissent en son nom.

Voilà où nous en sommes de notre réflexion !

Si vous avez des choses à ajouter, des points de désaccord ou autres
réflexions, n'hésitez pas à nous interrompre pendant qu'il est encore temps !
