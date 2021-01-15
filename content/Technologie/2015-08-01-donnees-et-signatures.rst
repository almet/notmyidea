Service de nuages : Garantir l'intégrité des données via des signatures
#######################################################################

:summary: Comment garantir l'intégrité des données en utilisant les signatures.
:lang: fr
:date: 2016-03-01

*Cet article est repris depuis le blog « Service de Nuages » de mon équipe à Mozilla*

Dans le cadre du projet `Go Faster
<https://wiki.mozilla.org/Firefox/Go_Faster>`_, nous souhaitons distribuer des
mises à jour de parties de *Firefox* de manière séparée des mises à jour majeures
(qui ont lieu toutes les 6 semaines).

Les données que nous souhaitons mettre à jour sur les clients sont multiples.
Entre autres, nous souhaitons gérer `la mise à jour des listes de révocation
(CRL) de certificats SSL
<https://blog.mozilla.org/security/2015/03/03/revoking-intermediate-certificates-introducing-onecrl/>`_.

Il est évidemment nécessaire de s'assurer que les données qui sont téléchargées
sur les client sont légitimes : que personne ne tente d'invalider des
certificats alors qu'ils sont valides, et que l'ensemble des mises à jour sont
bel et bien récupérées sur le client.

La signature garantit qu'une mise à jour contient tous les enregistrements, mais il
est toujours possible de bloquer l'accès au service (par exemple avec le *china
great firewall*).

Ce mécanisme fonctionne pour les listes de certificats à révoquer, mais pas
uniquement. Nous comptons réutiliser ce même fonctionnement dans le futur pour
la mise à jour d'autres parties de Firefox, et vous pouvez également en tirer
parti pour d'autres cas d'utilisation.

Nous souhaitons utiliser `Kinto <https://kinto.readthedocs.org>`_ afin
de distribuer ces jeux de données. Un des avantages est que l'on peut
facilement *cacher* les collections derrière un CDN.

Par contre, nous ne souhaitons pas que les clients fassent
confiance aveuglément, ni au serveur Kinto, ni au CDN.

Effectivement, un attaquant, contrôlant l'un ou l'autre, pourrait
alors envoyer les mises à jour qu'il souhaite à l'ensemble des clients
ou supprimer des certificats révoqués. Imaginez le carnage !

Afin de résoudre ce problème, considérons les conditions suivantes:

- La personne qui a le pouvoir de mettre à jour les CRL (*l'updater*)
  a accès à une cle de signature (ou mieux, `un HSM
  <https://fr.wikipedia.org/wiki/Hardware_Security_Module>`_) qui lui permet de
  signer la collection;
- Le pendant public de ce certificat est stocké et distribué dans Firefox;
- Le *hashing* et la *signature* sont faits côté client pour éviter certains
  vecteurs d'attaque (si un attaquant a la main sur le serveur Kinto par
  exemple).

Le chiffrement à sens unique, aussi appellé *hashing* est un moyen de toujours
obtenir le même résultat à partir de la même entrée.


Premier envoi de données sur Kinto
==================================

L'ensemble des données est récupéré depuis une source *sécurisée* puis mis dans
une collection JSON. Chaque élément contient un identifiant unique généré sur
le client.
  
Par exemple, un enregistrement peut ressembler à :

.. code-block:: javascript

   {"id": "b7dded96-8df0-8af8-449a-8bc47f71b4c4",
    "fingerprint": "11:D5:D2:0A:9A:F8:D9:FC:23:6E:5C:5C:30:EC:AF:68:F5:68:FB:A3"}

Le *hash* de la collection est ensuite calculé, signé puis envoyé au serveur
(voir plus bas pour les détails).

La signature est déportée sur un service qui ne s'occupe que de ça, puisque la
sécurité du certificat qui s'occupe des signatures est extrêmement importante.


Comment vérifier l'intégrité des données ?
==========================================

Premièrement, il faut récupérer l'ensemble des enregistrements présents sur
le serveur, ainsi que le *hash* et la signature associée.

Ensuite, vérifier la signature du *hash*, pour s'assurer que celui-ci provient
bien d'un tiers de confiance.

Finalement, recalculer le *hash* localement et valider qu'il correspond bien à
celui qui a été signé.


Ajouter de nouvelles données
============================

Pour l'ajout de nouvelles données, il est nécessaire de s'assurer que les
données que l'on a localement sont valides avant de faire quoi que ce soit
d'autre.

Une fois ces données validées, il suffit de procéder comme la première fois, et
d'envoyer à nouveau le *hash* de la collection au serveur.


Comment calculer ce hash ?
==========================

Pour calculer le *hash* de la collection, il est nécessaire :

1. D'ordonner l'ensemble des éléments de la collection (par leur id) ;
2. Pour chaque élément, sérialiser les champs qui nous intéressent (les
   concaténer clé + valeur)
3. Calculer le *hash* depuis la sérialisation.

Nous sommes encore incertains de la manière dont le hash va être calculé. Les `JSON Web Signature
<https://tools.ietf.org/html/draft-ietf-jose-json-web-signature-41>`_ semblent
une piste intéressante. En attendant, une implementation naïve en python
pourrait ressembler à ceci :

.. code-block:: python

  import json
  import hashlib

  data = [
     {"id": "b7dded96-8df0-8af8-449a-8bc47f71b4c4",
      "fingerprint": "11:D5:D2:0A:9A:F8:D9:FC:23:6E:5C:5C:30:EC:AF:68:F5:68:FB:A3"},
     {"id": "dded96b7-8f0d-8f8a-49a4-7f771b4c4bc4",
      "fingerprint": "33:6E:5C:5C:30:EC:AF:68:F5:68:FB:A3:11:D5:D2:0A:9A:F8:D9:FC"}]

  m = hashlib.sha256()
  m.update(json.dumps(data, sort_keys=True))
  collection_hash = m.hexdigest()

Enfin, un schéma pour résumer !

.. image:: {filename}/images/kinto-signing.jpg
    :align: center
    :alt: Schema résumant le processus de signature de la collection.
