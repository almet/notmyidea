PyconFR 2015 — Cliquet
######################

:date: 2015.10.17
:category: pyconfr2015
:unlisted: true

.. note::

  Voici quelques notes prises durant la PyconFR 2015, à Pau. N'hésitez pas
  à les completer si besoin.

Speaker: Mathieu Leplatre (@leplatrem), Mozilla

Toolkit HTTP, pour éventuellement faire des microservices.

1. Origines
2. Protocole
3. Toolkit
4. Conversation

Origines
========

Stockage de données, Cloud Services, Mozilla. 
Le boulot, c'est de faire des APIs. On nous demande de faire des APIs, tout
le temps.

Souvent, les mêmes questions sont à l'ordre du jour. Heartbeat, codes
d'erreurs, etc. L'inventaire de tout ce qui est attendu d'une API, au dela de
ce qui est la valeur ajoutée du service.

Définition d'un protocole. Définir une API REST n'est pas aussi évident qu'il
y parait. Il faut définir les formats de JSON, les status, etc.

La réutilisation de certaines protocoles existants était possible (Sync, en
production depuis quelques années).

Réutiliser du code nous permettait et faire un template pour démarrer plus
facilement, pour se concentrer sur le métier de l'API. Puisque les besoins ne
sont pas toujours les mêmes, avoir une boite à outil permet de choisir ce que
l'on souhaite.

Protocole
=========

- Création d'un protocole qui respecte les bonnes pratiques. CORS, avoir les
  bons codes de status, arrêter de se poser toujours les mêmes questions.
  Contrairement à ce qu'on imagine, la spécification HTTP n'est pas si facile
  à suivre. Plutôt que d'écrire un document, un toolkit à été créé.
- Les ops ont besoin de quelques endpoints: un heartbeat (monitoring) des
  endpoints de batch, un endpoint "hello", pour connaitre le type de service,
  ses URLs etc.
- La service renvoie toujours un JSON avec la description de l'erreur. Cela
  permet d'avoir tout le temps la même gestion des erreurs. Utilisation du
  header "backoff" qui permet de demander aux clients d'arreter de faire des
  requetes durant une durée spécifée par le serveur.
- Pour les resources "REST", quelques règles sont définies: quel est le format
  du JSON, quel est la syntaxe du querystring pour filtrer, ordonner, gérer les
  opérations concurentes, etc.
- Comment la validation fonctionne ? La pagination ? La définition des
  permissions ? Les erreurs.

Définir le protocole une seule fois permet de se mettre d'accord avec les Ops.
On ne créé pas une RFC pour l'instant, il faut qu'on valide ce qu'on a fait,
il est necessaire de valider notre approche.

Toolkit
=======

La stack en place est basée sur Pyramid et Cornice. Autre chose aurait pu petre
utilisé. Mais pyramid à été choisi pour son approche simpliste et qui permet de
rajouter de la complexité au fur et à mesure.

Cliquet propose de faire l'ensemble du boilerplate, la lecture du protocole, et
vous permet de créer les backends souhaités.

Il est possible de choisir les methodes HTTP acceptables, les URLs à utiliser
etc. Tweaker l'API est possible, la chose qui reste toujouts stable est le
protocole.

le toolkit vise à faire quelque chose de pluggable. Tout est controllable
depuis la configuration.

Pour le deploiement, cela veut dire que le monitoring est déjà connecté, et il
est possible de changer la configuration depuis un fichier `.ini`.

Il est aussi possible de faire du profiling en ajoutant deux lignes de code,
qui permet de générer des graphs qui permettent d'identifier les goulots
d'étranglement.

Microservices ?
===============

- Cliquet apporte une manière standard de surveiller, deployer, configurer des
  services.
- Il est possible de se focaliser sur la logique de l'application, en faisait
  une abstraction des backends, etc.
- Le fait de figer l'API permet d'avoir des clients génériques que l'on peu
  réutiliser d'une application à l'autre.

Cliquet est utilisé pour
========================

- Kinto, un service générique de stpclage de données.
- Syncto, un proxy pour Sync en utilisant le protocole.
- La liste de lecture, service qui à été shutdown.

Questions
=========

- **Qu'est-ce qui est pluggable ?** Les choix qui sont fait dans cliquet
  concernent le protocole. Le toolkit est lui fait de manière "pluggable". Il
  est par exemple possible de changer le backend, l'authentification, le cache
  ou les permissions.
- **Quelles sont les parties non standard? Est-il prévu de representer ça via
  une RFC ?** Le seul sujet qui pourrait etre utile dans une RFC serait de
  définir les headers attendus pour la validation et l'écriture
  concurrentielle. L'ensemble de ce qui est proposé est standard.
- **Existe-il un client JavaScript, comme pour Kinto ?** Actuellement, non. Par
  contre, Kinto.js est prévu pour que la partie commune entre les APIs (le
  protocole) peut etre extrait.
