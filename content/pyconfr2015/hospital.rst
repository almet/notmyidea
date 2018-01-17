PyconFR 2015 — Hospital - des tests en prod
###########################################

:date: 2015.10.18
:category: pyconfr2015
:unlisted: true

.. note::

  Voici quelques notes prises durant la PyconFR 2015, à Pau. N'hésitez pas
  à les completer si besoin.

Speaker: Benoit Bryon, Peopledoc.

Pour une procédure de déploiement, comment est-ce qu'on valide que tout va bien
une fois que tout est dépoyé ? Si on a une application très simple (upload et
envoi de fichiers).

Pour des applications plus complexes, il y a beaucoup de choses à tester (base
de données, cache, email, etc). Beaucoup de parties sont utiles: reverse
proxy, django, base de données etc.

Lors d'un déploiement, comment faire pour vérifier que tout tourne lorsque tout
est déployé ?

Comment faire ?
---------------

- Les tests permettent de tester hors sol.
- Le provisionning permet de valider que tout tourne correctement, mais
- simplement au démarrage. Les pannes ne sont pas détectées.
- Le logging va permettre de detecter les erreurs, mais trop tard.
- Le monitoring permet d'avoir une vue de l'exterieur.

Hostpital propose de faire des assertions sur la configuration,
l'environnement, *en cours de fonctionnement*. Ce sont les developeurs qui
ajoutent ces assertions.

Cela peut servir à valider un déploiement, pour etre rassuré une fois que le
déploiement effectué. Cela peut aussi service à surveiller un service et
diagnostiquer les problèmes.

Hospital
--------

::
  pip install hospital

Hospital est un outil en python. On définit des tests, de la même manière que
l'on définit des tests unitaires. On fait des assertions, comme pour les tests
unitaires. Hospital propose des helpers pour les cas courants:
`assert_http_response` ou `assert_ping`.

La vue est une vue de l'intérieur. La différence avec le monitoring est que
l'on teste la connectivité entre les services (exemple d'une requete
elasticsearch qui échoue depuis un service django).

Pour la supervision, les healthchecks sont lancés avec une ligne de commande
`hospital-cli`. Il est possible de lancer également ces tests avec nose ou
py.test.

Il est aussi possible de faire le monitoring avec une API HTTP `hospital
serve`.

Les lacunes de hospital
~~~~~~~~~~~~~~~~~~~~~~~

Les healthchecks sont fait actuellement en synchrone. Cela peut prendre du
temps. Il pourrait etre interessant de lancer des taches de manière distribuée
/ en paralelle.

Il pourrait etre utile de faire la distinction entre les smoketests et les
diagnostiques: les premiers sont des petits checks qui permettent de dire si ça
marche, de manière très simple. De l'autre coté, les diagnostiques seraient eux
plus fins.

Wrap up
-------

Validez votre configuration, la connectivité avec les services externes. Faites
des tests souvent !
