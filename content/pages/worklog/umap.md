---
title: uMap
save_as: umap/index.html
template: worklog
total_days: 78
---
Total prévu sur uMap pour moi = 90 jours (y compris le mécénat de Scopyleft)
NLNet = 40 000€ = 62 jours
Fait = 87 jours.

MAIS: pas terminé le travail, il manque:

a. Scale things up:
- Throttling: frequency of sync: ability to send messages by batches
- Handle running multiple processes to handle more load, distribute the load on different WebSocket workers.
- Deal with maximum number of peers connected (what happens when the limit is met?)
b. Handle security:
- Find a mechanism to revoke permissions when the owner changes them
- Deal with an evil client sending messages to an elevated client.
- Process external security review

Ce qui représente 8000€ restant à payer de la part de NLNet pour:
8000€ = 12 jours (en moins)

- Actuellement: 61h de « non payé » = 5 664€ (à la fin de cette semaine) = 9j

Deux sujets:

- Comment est-ce qu'on termine ma « mission » ?
- Des sous ont été mis de côté (par Scopyleft ? Par David ?) plus tôt, qu'il n'a pas consommé, et il proposait de les utiliser ici.







## Mardi 12 Novembre 2024 (3h, 5/5)

## Mercredi 13 Novembre 2024 (8h, 5/5)
## Jeudi 14 Novembre 2024 (7h, 5/5)

## Vendredi 15 Novembre 2024 (7h, 5/5)

## Vendredi 25 Octobre 2024 (6h, 2/5)

Je continue le boulot sur la reconection des websockets, pour pouvoir afficher un dialogue quand on est déconnecté. Je teste et ça semble fonctionner, plutôt.

Je fais un test rapide sur le fait que le debounce peut fonctionner, c'est une première approche mais ça montre que déjà ce sera possible. J'aimerai bien cibler un peu plus pour que uniquement les modifications liées aux mêmes *properties* passent par debounce.

Le manque de motivation suite au sujet conflictuel de la veille (non réellement traité) et au fait que je me sens seul pour travailler sur ce projet de manière générale. Le stress aussi arrivant avec le fait que c'est bientôt la fin du temps prévu et disponible pour avancer.

## Jeudi 24 Octobre 2024 (6h, 1/5)

Dans la matinée, on discute avec Yohan, sur la manière de faire des reviews, et sur les interconnections avec la motivation de participer au projet. Je suis assez frustré par le questionnement de mes propositions et la forme que ça prends. On décide que Yohan prendra le lead sur les changements qu'il demande pour la gestion des layers.

L'après-midi, la motivation est à la baisse, je propose une manière de faire en sorte que les websockets se reconnectent automatiquement.

## Mercredi 23 Octobre 2024 (9h, 5/5)

Je change d'approche pour la gestion des layers, et j'utiliseune approche qui permet de stocker le futur UUID, avant qu'il soit envoyé sur le serveur, je passe du temps à débugger les tests pour finalement me rendre comptes des cas limites.

On discute de l'approche en commentaires interposés, et je commence en parallèle à travailler sur la reconnection des websockets.

## Mardi 22 Octobre 2024 (9h, 4/5)

Je commence par débugger des tests fonctionnels qui ne marchaient pas sur ma branche, parce que je ne vérifiais pas que `options.*` pouvait être envoyé dans le fonction qui vérifiait que le champ était bien dans le schema. Les tests passent. Je merge.

J’enchaîne sur la gestion des layers, et je change la manière dont ils sont enregistrés sur le serveur. Je fais un changement qui permet aux clients de specifier l'UUID lors de la sauvegarde. Certains tests ne passent pas, et c'est compréhensible, il manque encore un peu de travail. J'ai cru à un moment qu'il était normal que les layers ne soit pas demandés par requête spécifique, mais un appel avec Yohan me dit que c'est autre chose.

Biweekly de synchro, il faut que je prenne mes billets de train :-)
## Lundi 21 Octobre 2024 (6h, 5/5)

La reprise sur uMap. C'est l'avant dernière semaine. Je fais un tour des changements faits depuis la dernière fois, et je fait des modifications sur la PR qui permet d'afficher le nombre de pairs connectés.

On a une discussion avec Yohan sur la manière de rendre des données de titre et visibilité, qui est actuellement faite en dehors du `map.render()`. On se dit que ça peut être pas mal de passer par là si possible.

Je fais une revue du code qui permet d'ajouter le support de asgi. J'organise aussi un peu la semaine, en terme de tâches à faire. Demain, j'aimerai bien changer la manière dont la synchronisation des layers fonctionne, en proposant d'inverser l'assignation des UUIDs pour que ce soit le client qui s'en occupe, en tout cas qui puisse suggérer les modifications au serveur.
## Vendredi 27 Septembre 2024 (7h, 5/5)

Je trouve une manière de faire le déploiement avec uWsgi pour le serveur de websockets.

Une session de débug avec David, pendant laquelle on trouve plusieurs problèmes, dont un qui crée des connections websocket en cascade, puisque les clients rejouent en boucle les opérations de modification du statut `syncEnabled` de la carte.

On en profite pour changer le nommage de certaines méthodes, ça faisait longtemps que ça me titillait.

J'en profite pour noter les quelques problèmes qui arrivent en lien avec les layers, dont la création est effectuée par le serveur, ce qui génère quelques soucis au niveau client, lorsque les layers ne sont pas sauvegardés et qu'on commence à faire des opérations dessus.

Je boucle en commençant une branche `display-connected-peers` qui permet de montrer les pairs qui sont actuellement connectés.

## Jeudi 26 Septembre 2024 (10h, 3/5)

Je simplifie le code pour la gestion des opérations dans la PR en cours, puis je me renseigne sur la manière dont il est possible de s'intégrer avec Django Channels, et si ça à du sens.

On se fait une session de discussion avec David, puis un tour du propriétaire suivi d'une session de debug, pour se rendre compte que `makeFeature` ne passe pas sync=false en paramètre.

On a en direct la réponse de NLNet pour le financement pour les tuiles vectorielles, qui est accepté !

Je déploie sur fly.io :-) 

## Mercredi 25 Septembre 2024 (6h, 3/5)

Je travaille sur le lien entre les opérations `update` et `upsert`. Le fait de gérer les cas "offline" nécessite de traiter le conflit qui existe entre les deux, pour éviter que des opérations `upsert` (qui sont envoyés à chaque modification d'une géométrie d'une feature) n'écrasent d'autres opérations arrivées depuis concernant la même feature par exemple.

Cela nécessiterait de faire la distinction entre la création d'une feature et sa modification. On utilise actuellement les événements de `Leaflet.Editable`, qui ne font pas la différence entre les deux.

J'ai pris le temps de transposer cette compréhension dans des tests fonctionnels pour `Operation.isLocalOperationNewer`.

## Mardi 24 Septembre 2024 (9h, 4/5)

- J'ai écris un test fonctionnel pour playwright, pour m'assurer que les pairs qui rejoignent une session d'édition après les autres puissent récupérer les infos qui leurs manquent.
- J'ai trouvé un bug, et je ne comprenais pas du tout ce qui le provoquait. Il semblerait que ce soit lié aux changements liés à l'ajout des cercles proportionnels. Une fois ce type de layer utilisé, il est impossible d'ajouter de nouveaux points sur la carte.
- J'ai compacté les changements et mis à jour la pull request.
- Réunion bi-hebdo avec David et Sophie.
- Commencé à rajouter des tests pour la logique de `isLocalOperationNewer`, je pense que ça va être important d'avoir quelque chose qui marche bien ici, parce que c'est cette fonction qui décide d'appliquer ou non les changements qui viennent de l'extérieur.

## Lundi 23 Septembre 2024 (9h, 5/5)

- J'ai pris le temps de faire un tour des changements effectués ces derniers mois,
- J'ai lu les propositions de Yohan pour faire évoluer le schema des fichiers stockés sur disque (geoJSON).
- J'ai testé que le sync fonctionnait bien avec les ajouts récents, entre autres pour les cercles proportionnels aux valeurs.
- J'ai `rebase` ma branche de travail par dessus les modifications qui ont eu lieu ces derniers mois.
- J'ai écris des tests pour la classe de HybridLogicalClock
- J'ai retravaillé le protocole d'échange de données entre le client et le serveur, pour que le code soit plus simple à comprendre.

## Mardi 10 Septembre 2024 (1h, 3/5)

- Weekly

## Lundi 09 Septembre 2024 (2h, 4/5)

- Retrospective

## Mercredi 04 Septembre 2024 (1h, 5/5)

- Pad to discuss and then answered to NLNet email on the umap vector tiles

## Mardi 27 Août 2024 (3h, 5/5)

- Discussions avec David et Yohan sur la manière de s'organiser pour le futur sur umap.
- Catch-up pour savoir ce qui s'est passé cet été
- Discussions autour de la manière dont les metadonnées vont être stockées
## Vendredi 04 Juillet 2024 (7h, 5/5)

On se fait une session de pair avec Yohan le matin, continuée l'aprem, durant laquelle on a avancé des cas offline, et de comment réconcilier les messages manquants.

David nous rejoint en fin d'aprèm. Une bonne session !

## Jeudi 04 Juillet 2024 (10h, 5/5)

Je reprends le travail sur les messages échangés entre le serveur et les clients, pour trouver un moyen de récupérer les informations qui dates d'avant le "join". Je réussis finalement à trouver un moyen d'utiliser Pydantic comme je le veux, pour parser un message et avoir en retour différents objets, créés dynamiquement, en fonction du type de message.

Je réussis à envoyer l'ensemble des messages d'un client de l'autre côté, et ça s'affiche !
## Lundi 24 Juin 2024 (7h, 5/5)

Un bug remonté par un utilisateur me fait me rendre compte d'un impensé dans le code, et en tirant le fil, je trouve quelques bugs assez génants. Je les corrige.

Une discussion sur la gouvernance, qui débouche sur l'idée d'essayer d'avoir plus de clarté sur notre manière de nous organiser collectivement. Content devoir ce sujet pris en compte, et avancer.

On pair-prog avec David, et c'est aussi l'occasion de discuter ensemble.

## Lundi 17 Juin 2024 (5h, 5/5)

Je commence par décrire ce que je compte faire pour avoir les idées un peu plus
claires, puis j'enchaine sur l'implémentation de la sauvegarde des messages, du
HLC et du protocole de discussion avec le serveur.

Au passage, je me rends compte que le nombre de messages générés par le
`FormBuilder` est bien trop important, et qu'il faudrait plutôt utiliser
l'évènement `onBlur` pour éviter d'envoyer des messages à chaque modification
d'un `input`.

Le serveur à maintenant la possibilité de gérer différents types de messages, et
j'en suis au moment où je fais la selection du pair pour que celui ci envoie ses
messages de l'autre côté. Il me reste à demander côté client, puis à recevoir la
le message et à y répondre, pour enfin récupérer la liste des opérations et les
appliquer localement.

## Lundi 10 Juin 2024 (6h, 4/5)

- Je rédige un article qui résume là où on en est pour la synchro
- Je relis le code du sync engine et j'ai très envie de le simplifier, je fini par le faire et propose une pull request qui permet de virer certains concepts, pour simplifier de manière générale l'implémentation.
- On se fait une rétrospective sur les 6 dernières semaines

## Vendredi 07 Juin 2024 (2h, 5/5)

- On se retrouve avec David pour échanger autour de ce qu'il traverse en ce moment.
- On merge tous les trois ensemble le travail effectué jusqu'ici sur la collaboration temps réel. yay !
- Je planifie les prochaines étapes pour la synchro

## Lundi 03 Juin 2024 (6h, 5/5)

- Trouvé une solution pour que le serveur websocket ne soit lancé que sur un seul worker lorsqu'on utilise pytest. Je me retrouvais dans une situation où le serveur websocket n'arrivait pas à se lancer de manière séparée. [Plus de détails ici](https://blog.notmyidea.org/start-a-process-when-using-pytest-xdist.html)
- Une session avec David durant laquelle on parle des messages d'altertes qui sont affichés lorsqu'il y a conflit. Je me rends compte qu'il serait potentiellement intéressant de changer la manière dont l'algorythme de merge fonctionne, pour lui faire utiliser les `ids` qui ont été introduits sur les features. Ça nous permettrait sans doute d'être plus précis.
- Êcrit un mail pour clarification avec NLNet sur le fait que les plans changent un peu de ce qui était prévu.


## Vendredi 31 Mai 2024 (9h, 6/5)

- Rebase la PR sur la synchro, et traité les points qui étaient en attente (il y en avait quelques uns !). Entre autres:
- Rendu les settings pour la synchro plus compréhensibles en dissociant le « front » et le « back ».
- Ajouté la possibilité de lancer le serveur websockets avec un commande django `umap run_websocket_server`
- Modifié l'API pour synchroniser, qui est maintenant beaucoup plus compréhensible (`this.sync.update("key", "value)`)
- Fait un point avec Yohan et David sur leurs avancées ces dernières semaines, dans lequel on a passé en revue les derniers bouts qui restaient à discuter sur la PR.

J'ai très envie de merger, mais il me reste quelques petits trucs, entre autres que les tests ne passent pas pour le moment. J'ai l'impression que c'est peut-être du en partie à un rebase trop rapide, et au fait que l'outil que j'utilise pour lancer une commande en tant que fixture `pytest` ne semble pas fonctionner correctement.

Je me demande si je ne vais pas tout simplement le faire à la main 🤔

## Jeudi 16 Mai 2024 (7h, 4/5)

De la revue de code, des tests, de la documentation, et un fix, après m'être rendu compte que l'algorithme de merge sur le serveur dupliquait des données en essayant lui aussi de fusionner les modifications, alors qu'elles étaient déjà à jour. La résolution du problème était simplement de le mettre au courant en propageant la version de référence.

## Mercredi 15 Mai 2024 (8h, 5/5)

Je rajoute des tests fonctionnels, et ça fonctionne !

L'après-midi, je présente mon travail à Yohan et David et on discute des aspects liés, et de comment certains points (entre autres les permissions) seront gérés. Ce n'est pas encore clair, mais plusieurs propositions semblent avancer.

## Mardi 14 Mai 2024 (5h, 5/5)

- J'écris des tests puis change la manière dont les clés sont trouvées et mises à jour dans la méthode `updateObjectValue`, pour que ça utilise `reduce`.
- Des test pour vérifier que le *dispatch* les messages entrants génère bien des erreurs quand c'est utile.
- Une discussion avec Yohan sur notre manière de communiquer et les moments où ça génère du stress. C'était utile, et je suis content d'en avoir pris le temps.
- Je fais tourner le serveur de WebSockets durant les tests et j'écris un scenario de test qui vérifie que la synchro fonctionne pour deux points.

## Lundi 13 Mai 2024 (8h, 5/5)

- J'ajoute le support de la synchro pour les *datalayers*, qui n'étaient pas en fait pris en compte lors de leur création ;
- Je fais passer les tests existants, ce qui me permet de trouver quelques problèmes dans l'ordre dont certaines méthodes sont appelées.
- J'en profite pour simplifier la base de code en ne gardant un updater que pour la carte, les *datalayers* et les *features*. (il n'y a plus besoin d'un updater par type de feature, le code est maintenant générique)
- Je rajoute des tests pour les vues de génération des tokens

## Vendredi 10 Mai 2024 (6h, 5/5)

Une journée passée à comprendre comment fonctionne Fly.io pour pouvoir déployer dessus. On a fait une session de pair avec David, pendant laquelle on a réussi à faire tomber le truc en marche, en levant les différents bloquages qu'on découvrait au fil de l'eau. Ça marche presque !

## Jeudi 09 Mai 2024 (7h, 3/5)

J'ai ajouté une manière de vérifier que les messages entrants sont bien acceptables, pour éviter que n'importe quel message soit accepté.

J'ai ajouté une propriété `belongsTo` dans le `SCHEMA`, qui contient une liste des sujets concernés (`map`, `datalayer` ou `feature`). 

Ça m'a permis de me rendre compte de quelques pirouettes qui sont faites actuellement dans le code :

1. pour `map` et les `datalayer`, les propriétés sont dans `.options.{property}` alors que pour les `features` elles sont dans `properties`.
2. Pour les `features`, les propriétés sont contenues dans un *namespace* `_umap_options`.

Je suis repassé sur **toutes** les options qui sont modifiables dans uMap, et fait quelques ajustements pour rendre tout fonctionnel. C'est très satisfaisant d'avancer :-)

Je change la manière dont les settings sont gérés avec les variables d'environnement, et je déploie le tout avec docker, rejoint par david pour une petite session papote et durant laquelle on réussit à faire tourner avec la ligne suivante:

```bash
docker run --privileged --publish 8000:8000 -e "DATABASE_URL=postgis://alexis:@host.docker.internal:5432/umap" -e"SECRET_KEY=tralala" -e "WEBSOCKET_ENABLED=True" -it umap-ws
```
## Mercredi 08 Mai 2024 (7h, 5/5)

L'import de données marche maintenant, ça à demandé quelques changements sur la manière dont les données étaient envoyées. Je suis content d'avoir une démo fonctionnelle. J'ai ensuite fait un peu de pair avec Yohan, pour changer la manière dont les évènements sont gérés.

Je n'écoute plus les changements « au fil de l'eau », mais uniquement quand les données sont vraiment présentes. Par exemple, uniquement la position de fin lors d'un drag-n-drop est envoyée, ce qui est moins impressionnant, mais garde de la bande passante et du CPU pour autre chose.

Je suis repassé ensuite sur certaines fonctionnalités accessibles avec les menus « clic droit » pour m'assurer que tout fonctionne comme prévu, et j'ai corrigé quelques bugs au passage.

Chouette, ça avance :-)

## Mardi 07 Mai 2024 (10h, 5/5)

Je continue de faire marcher la PR en cours sur la synchro. Je suis dans des cas que je n'avais pas encore pris en compte, entre autre j'ai maintenant une meilleure compréhension de la manière dont les menus « clic droit » fonctionnent.

Ça m'a permis de régler certains problèmes, et d'avoir un import quasi fonctionnel (les données manquent, je n'ai pour le moment que les géographies). J'ai fait des changements mineurs et:

- Les websockets ne sont crées que lorsqu'on rentre dans le mode édition
- il est possible de bouger les polygones et les lignes, alors que c'était cassé jusqu'ici

En fin de journée, j'ai finalement réalisé que l'import ne prenait pas en compte les données (uniquement les géométries).

## Lundi 06 Mai 2024 (7h, 5/5)

Le matin, travail avec Aurélie sur l'UX pour la synchro, l'après midi présentation de la PR en cours avec David et Yohan, en sandwich avec la weekly.

Je passe un peu de temps pour comprendre comment fonctionne Docker, et les Dockerfiles dans le cadre de uMap.

On se pose quelques questions autour de la manière de faire de la gestion des permissions, et j'entrevois la possibilité de limiter les vérifications qui sont faite sur le serveur.
## Mardi 30 Avril 2024 (6h, 5/5)

J'ai continué le travail sur la PR en cours, en ajoutant plein de petits bouts qui manquaient pour que ce soit utilisable. On a maintenant un bouton pour démarrer la collaboration « temps réel », et des `settings` qui vont bien pour pouvoir configurer ça comme on veut. Pour le moment j'ai mis le bouton à un endroit comme un autre, mais ça pourra changer.

J'ai pu me rendre compte de quelques parties qui ne fonctionnent pas encore, comme l'import de données.

## Lundi 29 Avril 2024 (7h, 4/5)

La reprise :-) J'ai fait une petite revue de code de ce qu'a proposé Yohan pour les règles de filtrage, et j'ai repris le travail sur la synchro. Laisser respirer entre plusieurs tentatives permet d'affiner. J'ai quelque chose qui fonctionne à peu près bien, minus les quelques cas qui ne sont pas encore couverts.

Présentation du travail prévu par Sophie pour trouver de nouveaux débouchés pour l'instance ANCT, puis retrospective, au format conseil de famille. C'était bien, mais j'aurai voulu préciser la temporalité de la réunion en commençant.

## Vendredi 20 Avril 2024 (6h, 4/5)

J'ai repris le travail que j'avais entamé en tant que « preuve de concept » pour l'intégrer dans une version plus mure. J'ai passé du temps à définir les étapes nécessaires pour arriver à avoir de la synchronisation temps réel, et j'ai déroulé. Je synchronise les propriétés des cartes, ainsi que les features (en tout cas les marqueurs).

Je ne suis pas encore certain que ce soit utile de vérifier le format des messages sur le serveur, et j'ai envie de simplifier plusieurs bouts de code / d'architecture, par exemple ce sont les composants qui se déclarent « synchronisables » et je pense que ça pourrait être fait de manière plus explicite.

## Jeudi 19 Avril 2024 (4h, 4/5)

En écrivant les notes, je me rends compte que la raison pour laquelle les websockets ne sont pas same-origin avec notre domaine n'est pas que ça pourrait être hebergé sur un autre domaine, mais que wss:// et https:// ne semblent pas être considérés comme le même domaine. D'où [la pirouette nécessaire](https://websockets.readthedocs.io/en/stable/topics/authentication.html#cookie) (à base d'iframes) pour lier le cookie au bon domaine.

Je me dis qu'une des options est que le serveur nous renvoie un token signé par le serveur, qui pourrait contenir les permissions qui sont données, dans le même esprit que des JWT.

Je tombe sur une partie du code qui utilise du SHA1 pour les signatures, que je considérais comme insécure. En [creusant un peu](https://crypto.stackexchange.com/questions/845/what-is-wrong-with-using-sha1-in-digital-signatures-why-is-a-robust-hash-functi), je me rends compte que pour le moment, sha1 est considéré insécure, mais qu'il n'y a pas encore d'attaques connues dessus qui permettent d'utiliser du « second-pre-image », c'est à dire des signatures différentes de celles d'origine, mais qui sont aussi valides. On est bon pour ce coup là.

## Mardi 17 Avril 2024 (6h, 3/5)

J'avance sur un première implementation du serveur de websockets, avec l'idée de relayer les messages entre les clients. J'attaque par l'authentification des connections, qui est nécessaire pour éviter que des attaquants (potentiels) utilisent la connection websocket pour faire par exemple de l'élévation de privilèges (pour pouvoir éditer un layer auquel iels n'ont normalement pas accès). 

Je passe du temps à lire les différents moyens de s'authentifier, et je commence une implémentation. J'en profite pour valider les entrées avec Pydantic.

## Lundi 16 Avril 2024 (7h, 4/5)

Une matinée passée à travailler sur de l'UX, en completant le document donné par Aurélie. Ça donne quelques idées c'est chouette.
L'après midi, je me synchronise avec David, puis avec Yohan. Je merge la PR pour pouvoir faire du rendu « dynamique » (ce qui va permettre de faire du rendu depuis des évènements distants).

## Vendredi 12 Avril 2024 (6h, 5/5)

Je continue ma compréhension de ce qu'on pourrait techniquement faire pour supporter du hors-ligne. J'ai rédigé un bout de README pour un projet qui pourrait faire une sorte de K/V store pour des documents GeoJSON. Tout n'est pas encore clair, mais ça progresse.

## Lundi 08 Avril 2024 (5h, 4/5)

Une après-midi à Grenoble avec Aurélie, on a passé du temps à creuser les aspects UX sur la collaboration temps réel, en faisant un persona et en prenant un cas concret d'utilisation. 

Une réunion sur la documentation avec David, Aurélie, Framasoft et Antoine Riche. C'était chouette de pouvoir discuter clairement de leurs intentions sur le sujet. Ça me donne envie d'avancer, content que David prenne le sujet, on va surement partir sur notre propre documentation.

J'ai passé du temps à lire la documentation sur les WebSockets en python, je comprends mieux comment faire du routing, et comment tout ça va passer à l'échelle.

## Vendredi 05 Avril 2024 (4h, 4/5)

J'ai fait passer les tests sur la Pull Request en cours. Les tests ajoutés sur cette PR m'ont permis de detecter des bugs que j'avais introduit lors de la refactorisation des `utils`, content de les trouver 😅.

Je fais un tour des différents outils qui permettent l'édition collaborative et je note les parcours qui y sont présents.

Je continue ma réflexion autour de la propagation des changements locaux vers d'autres pairs: actuellement ces changements ne sont pas liés au format GeoJSON, et je me demande si cela serait possible. Ça aurait l'avantage de s'intégrer facilement avec d'autres outils qui utilisent ce format, et ça permettrait de résoudre le problème du chargement initial: ce ne serait plus les clients qui enverraient leur dernière version courante, mais le serveur qui compacterait les opérations en attente.

## Lundi 01 Avril 2024 (5h, 5/5)

J'ai relu, modifié puis envoyé la proposition pour les tuiles vectorielles pour uMap. J'ai ensuite discuté avec Vadims (de JSON Joy) de notre cas d'utilisation. Il semble ressortir qu'il serait quand même plus simple d'avoir un serveur qui est capable d'avoir une representation de l'état du document.

Le serveur pourrait stocker les opérations (indéxées) qui lui sont envoyées, avec une vue de l'état du document, qui serait compacté de temps en temps. 

On a évoqué le fait que ce serait aussi peut-être plus simple pour nous d'utiliser des Hybrid Logical Clocks (ts + logical time + userId), et de recoder un CRDT nous même. Il m'a parlé de museapp ([Metamuse podcast — Muse](https://museapp.com/podcast/)) qui semble avoir fait ça et qui en ont parlé dans un podcast.

J'ai ensuite mergé les deux PR en attente sur les changement dans la suite de test, et rajouté quelques entrées dans le schema, qui ne prenait pas en compte les données à l'intérieur des layers (choropleth, etc.).

## Jeudi 29 Mars 2024 (5h, 4/5)

J'ai travaillé sur deux propositions de financement: une pour NLNet pour la quelle on propose d'ajouter les fonctionnalitézs de tuiles vectorielles, et l'autre pour Google Season of Docs ou on aimerait bien avoir quelqu'un qui nous aide à améliorer la documentation technique.

J'ai aussi avancé sur la séparation des tests unitaires JS avec le reste, et ça passe !

## Lundi 25 Mars 2024 (9h, 4/5)

Le matin je travaille à faire passer les tests. J'ai pas mal bloqué sur le JSDom (encore), et la manière d'intégrer tout ça dans le contexte des tests. C'est plus clair maintenant, mais j'aurai aimé que ce soit plus simple dès le début.

L'après midi à été utilisée à comprendre ce qui s'est passé lors de la mise en prod, le passage aux UUIDs étant moins simple que prévu, avec un cas limite qui arrive parce que la liste des fichiers à purger (les anciennes versions) mettait en tête de liste les nouveaux fichiers, qui utilisaient les UUIDs (en tout cas, dans certains cas). On a mis quelques heures a trouver ce qui se passait, à priori ça devrait être réparé.

## Vendredi 22 Mars 2024 (4h, 3/5)

On a fait un point avec Virgile autour du google season of docs, on se dit que ça pourrait être chouette de faire une proposition sur la partie documentation technique.
J'enchaine avec un point sur une prochaine session NLNet, ou on aimerait proposer de faire des vector tiles. Je comprends mieux de quoi il s'agit, et je vois les futurs que ça ouvre pour uMap, entre autres avec le lien possible avec les données OSM.

J'aimerai bien que ce soit une étape dans l'idée d'avoir un jour des cartes plus facilement accessibles hors ligne, et synchronisables. J'ai enchainé sur le fait de séparer les tests unitaires actuels, qui tournent dans un navigateur, du reste des tests. L'idée étant de les faire tourner dans un contexte de ligne de commande, pour s'intégrer avec le CI, entre autres.

## Jeudi 21 Mars 2024 (6h, 3/5)

J'ai passé une journée à écrire des tests, à la fois pour playwright (j'en ai profité pour découvrir qu'il était possible d'enregistrer sa session, et que le code soit produit pour moi derrière), et pour des tests unitaires JS. Je tire un peu la langue, c'est long et fastidieux, et je n'ai pas encore terminé. 

## Lundi 18 Mars 2024 (6h, 5/5)

Je commence à creuser sur l'intégration des websockets avec Django Channels, l'implication technique que ça pourrait avoir pour les personnes qui déploient, pour finalement changer d'approche en fin d'après-midi suite à une discussion avec David et Yohan, ce sera surement plus simple d'ajouter un serveur de manière séparée (au moins pour le moment) pour les personnes qui ont envie d'ajouter de la synchro.

On s'est fait un moment de rétrospective, avec le format du conseil de famille, proposé par David. Je me suis senti faire équipe avec le reste des participant·es.

Puis, un moment pour planifier les prochains développement. On discute de comment nommer les jalons dans notre outil de gestion des fonctionnalités. 

## Dimanche 17 Mars 2024 (2h, 5/5)

J'ai continué à améliorer l'article sur les CRDTs.

## Samedi 16 Mars 2024 (2h, 5/5)

J'ai refais une passe sur l'article sur les CRDTs, en changeant sa structure et en clarifiant certains aspects. On est pas loin d'un article prêt, j'aimerai bien refaire une dernière passe dessus pour que les "key takeaways" soient plus clairs (et moins nombreux).

## Vendredi 15 Mars 2024 (4h, 5/5)

J'ai terminé ([PR](https://github.com/umap-project/umap/pull/1692)) la séparation du rendering avec la mise à jour des données, en suivant la piste commencée mardi, puis j'ai passé un peu de temps à faire marcher json joy, suite aux retours du mainteneur. L'API générale me semble bien pour des gens qui utilisent des composants qui savent se re-rendre, mais quand on a besoin de savoir ce qui a été modifié dans le patch, il faut regarder la dedans à la main ce qui rends toute l'opération un peu plus précaire.

Bon, j'ai réussi à faire marcher le tout c'est l'important ! J'en ai profité pour bouger le code de [leaflet-sync](https://gitlab.com/umap-project/leaflet-sync) dans l'organisation umap-project dans gitlab.

Normalement, tout est en place pour qu'on puisse commencer à ajouter du websocket dans le mix, surement dans le courant de la semaine prochaine !

## Mardi 12 Mars 2024 (7h, 5/5)

Une bonne journée, passée majoritairement en pair prog avec Yohan. On a d'abord fait un point de synchro sur l'avancement général de la synchro, durant lequel on a plus ou moins décidé d'aller dans un premier temps vers la version simple de la synchronisation, en faisant en sorte que les clients écrasent les données des autres clients, avec le serveur qui s'occupe de faire le passe-plat.

Ça laisse les CRDTs de côté pour le moment, l'objectif devenant donc d'avoir quelque chose de fonctionnel derrière un feature flag pour les gens qui ont envie de tester, au risque de renverser le café au milieu de la table. On verra ensuite en quoi les CRDTs sont utiles, si c'est le cas.

Ensuite, je suis donc reparti sur ce que j'avais laissé de côté hier, à savoir le fait d'avoir des données en plus expliquées dans le schema, pour savoir ce qui va se rerendre. L'idée avec le schéma étant d'avoir quelque chose d'abstrait, on est parti sur une clé `impacts` qui permet de lister ce que chaque propriété impacte: l'ui, les données, etc.

On a déroulé ce fil là ensuite, en repassant sur chacune des propriétés et en ajoutant celles qui manquaient. Un peu fastidieux, mais ça me donne une meilleure compréhension de certains bouts du code.

Je me suis arrêté au moment ou on commençait à voir en quoi certaines propriétés des layers nécessitaient un comportement spécifique (par exemple le choropleth), affaire à suivre !
## Lundi 11 Mars 2024 (8h, 5/5)

J'ai fait un tour des pull requests en cours le matin, c'était chouette d'avoir un peu de bande passante pour faire le tour de ce qui avait été proposé et qui était en attente. J'ai ensuite continué la comparaison des différentes bibliothèques de CRDT, en cherchant à comprendre quelle était l'utilisation réseau.

Une conversation avec Alex CC sur le discord d'Automerge m'a permis de mieux comprendre que le modèle implémenté par automerge-repo-websockets était en fait un modèle ou le serveur centralise (et donc fait tourner le CRDT) les flux, alors que je pensais que c'était les clients qui se relayaient les messages.

On se fait un petit point de synchro avec David, ça faisait longtemps, c'était bien ! Je creuse sur les différentes manières d'implementer le flux de données, et de manière sur l'approche à prendre autour de cette synchronisation.

Ça me pousse à questionner le choix du décentralisé: je me demande si il est réellement souhaitable, et ce qu'il nous apporterait, concrètement, vis à vis d'une approche plus traditionnelle avec le serveur au centre. Il va falloir trancher pour avancer.

Weekly, durant laquelle on me demande de justifier les heures facturées qui étaient prévues mais un peu flottantes. Ça me poussera à être plus clair dans le futur.

Après la weekly, je commence à implémenter les `propertyRenderer`, en essayant de les intégrer avec le nouveau concept de "schema" qui a été mergé recemment. L'idée étant d'avoir un seul endroit ou les propriétés sont définies, ainsi que leur comportement. Les propriétés pouvant appartenir à différents contextes (la carte, les layers, les features) il faut trouver comment représenter ce contexte sans trop ajouter de complexité, mais en restant flexible pour le futur. On part sur une clé `renderers` qui est un objet avec en clé les différents contextes:

```js
renderers: {
	map: ['list', 'of', 'renderers']
	features: ['list', 'of', 'renderers']
}
```

Au passage, je me rends compte qu'il est possible de grandement simplifier le code qui s'occupe d'appeler les renderers, pour le mettre dans une fonction (à la python) plutôt que dans une classe. Après tout, il n'y a pas besoin d'avoir tout le contexte de la classe, uniquement de pouvoir appeler les méthodes pour se re-rendre.
## Vendredi 8 Mars 2024 (7h, 5/5)

J'ai refais une passe rapide sur les PR en cours d'intégration, et j'en ai profité pour m'assurer que le merge des features entre les anciennes versions (sans ids) et les nouvelles (avec ids) vont pouvoir fonctionner. Je suis content de voir que c'était déjà prévu dans le code d'origine, ouf, une chose de moins à se soucier.

Je continue l'article sur les CRDTs, et j'en vois bientôt le bout. Il me manque certaines données comme la consommation de bande passante que j'aimerai bien rajouter, il me semble que c'est pertinent. J'ai aussi envie de regarder d'un peu plus près le protocole de synchronisation avec Websocket, pour voir ce qui transite.

## Jeudi 7 Mars 2024 (3h, 5/5)

J'ai avancé sur l'article de blog sur les CRDTs, puis j'ai continué à travailler sur l'intégration d'automerge, puis de jsonjoy. J'ai bloqué sur certains petits trucs. L'équipe d'automerge est vraiment top et prompte à aider, je m'étais fait la réflexion il y a quelques temps déjà.

Pur jsonjoy, c'est une autre paire de manche. Je n'arrive pas à comprendre ce qui ne fonctionne pas, j'ai fait une demande sur le github, on verra ou ça mène.

## Mercredi 6 Mars 2024 (2h, 4/5)

J'ai codé un prototype qui utilise Y.js pour faire de la synchro d'une carte leaflet assez basique. Ça fonctionne. J'ai pris des notes sur le fonctionnement pour l'article de blog de résumé.

## Mardi 5 Mars 2024 (2h, 4/5)

Je travaille depuis Barcelone cette semaine. J'ai fait une passe ce matin sur les pull request en attente, et j'ai fait quelques changements dessus, en intégrant les retours de David et Yohan.

## Jeudi 29 Février 2024 (9h, 4/5)

J'ai intégré les changements faits sur mes pull requests en cours, puis je suis passé sur la recherche d'un correctif pour les `Last-Modified` qui n'ont une résolution qu'à la seconde, ce qui peut poser souci dans certains cas, si il y a des éditions concurrentes.

J'ai un peu challengé le fait d'utiliser des `Etag`, que je trouve plus élégants (et standards), mais pour le moment je suis parti sur une version avec des headers maison, en attendant qu'on se mette d'accord sur la marche à suivre. C'était intéressant de discuter de ça parce que ça m'a permis de découvrir quelques problèmes dans le code, concernant la gestion du "concurrency control".

Les versions étaient générés à deux endroits différents (une fois avec la date de dernière mise à jour du fichier, le `mtime`) et une fois avec un appel à `time.time() * 1000` dans le code, ce qui peut expliquer pourquoi il y avait des ratés dans la réconciliation des versions. C'était chouette de demander de l'aide sur la fin de session, tout était en place pour débugger, mais j'avais le cerveau frit. A deux, on a trouvé facilement :-)

C'était même doublement intéressant d'amener le sujet des `ETag` parce que ça permet de faire remonter le fait que Yohan n'est parfois pas à l'aise avec les changements vu que c'est qui fait la maintenance du site derrière. Un sujet intéressant à creuser je pense. Content de mettre la main dessus : -)

On s'est rendu compte à la fin de la session que les tests étaient bons, mais que lorsque les édits arrivent exactement au même moment, il y a une race condition: une seule des deux requêtes peut être au courant que la première à été modifiée, et donc des éditions peuvent se perdre. On se dit que c'est très peu probable dans la réalité, alors on passe outre. Peu-être qu'on pourrait regarder du côté d'un lock sur une méthode specifique (avec des arguments specifiques). 
## Lundi 26 Février 2024 (10h, 5/5)

J'ai continué le passage vers les uuids pour les datalayers, le matin j'ai finalement trouvé un moyen de récupérer le nom de la contrainte, et l'après midi on a passé un peu de temps avec yohan pour faire de la migration de données pour les utilisateurs qui font un usage un peu détourné des datalayers (en les utilisant en remoteUrl).

Weekly, et puis on a discuté avec David et Yohan de comment on pourrait faire évoluer le formbuilder dans le futur. Une des pistes serait de faire des forms un peu à la django, qui pourraient ensuite se rendre de manière automatique. On a discuté du fait de passer sur une formule HTML un peu plus directe (plutôt que de manipuler le DOM en JavaScript), mais pour le moment on reste la dessus.

Je continue le soir et je rends possible le fait d'appliquer les migrations dans l'autre sens. Je reprends doucement sur les différentes libs CRDT, l'idée étant de retravailler sur le code de démo que j'avais commencé en arrivant.

## Samedi 24 Février 2024 (4h, 5/5)

J'ai suivi mon envie de creuser sur les CRDT, je sens qu'on est bientôt prêts pour
pouvoir avancer sur le sujet, mais je manque d'une bonne compréhension des différentes
libs, de ce qu'elles proposent (API), et de comment on va les utiliser.

J'ai pris l'approche « article » et donc j'ai commencé la rédaction d'un article de
comparaison des différentes approches (ce qu'attends NLNet, d'ailleurs). C'est chouette
de voir que j'avance petit à petit, et que le chemin pour arriver à destination, même si
il n'est pas complètement clair, est au moins visible.

## Jeudi 22 Février 2024 (10h, 5/5)

Une bonne grosse journée :-) J'ai avancé sur le changement vers des UUIDs pour
les layers, je suis pas encore sur que ce soit la version finale mais ça avance
dans la bonne direction. J'ai l'impression que je vais devoir aller voir d'un
peu plus près les entrailles de Django et des migrations pour pouvoir récupérer
le bon nom des contraintes qui sont générées par l'ORM.

J'en ai profité pour remettre au gout du jour la PR sur les IDs des features, et
pour commencer à travailler sur le problème du `Last-Modified` qui ne peut pas
avoir plus d'une requête à la même seconde, ce qui nous cause des soucis.

C'est chouette de faire quelques pull requests :-)

## Lundi 19 Février 2024 (8h, 4/5)

Un bout de temps pour debugger des histoires d'agent ssh qui n'utilise plus la
passphrase par defaut avec gnome-keyring. Il se trouve que depuis la version
46, la fonctionalité ssh [est maintenant désactivée par defaut](https://
wiki.archlinux.org/title/GNOME/Keyring#SSH_keys). Ça aura permis de mieux comprendre
le fonctionnement des agents SSH.

On enchaine sur un bug dans le deploiement avec Docker, mais sans avoir accès aux logs
c'est compliqué d'y voir clair. A priori quelque chose se passe mal, affaire à suivre.

Je reprends sur la synchro des layers, et je me rends compte qu'il n'est en fait pas
nécessaire d'avoir accès aux formbuilders lors de la phase d'update (c'est
uniquement utile pour rerendre les formbuilder si ils sont actuellement
ouverts). Peut-être utile, mais pas indispensable.

On enchaine le début d'ap-s midi avec Aurélie, et on décide d'avancer sur l'expérience
utilisateur pour la synchro. Je suis content de discuter de ça, c'est nouveau pour moi.

Weekly, puis discussion avec David et Yohan sur la suite des évènements, on décide d'utiliser
des UUIDs plutôt que des IDs de base de Django. C'est pas si simple ! J'en profite pour
redécouvrir les migrations avec Django.

On s'arrête au milieu de la session, hate de prendre la suite.


## Jeudi 15 Février 2024 (7h, 4/5)

Le matin j'ai terminé l'article d'update, puis j'ai enchainé sur la
synchronisation des layers. C'est un peu plus compliqué que pour le reste des
features, et je suis donc content de le faire en dernier. Je fais un peu de
refactoring. Je dois arrêter au milieu pour enchaine sur ma soirée. Il faudra
réussir à mapper les `properties` avec les `formbuilders` qui vont bien, pour
que le client qui reçoit puisse appliquer les modifications utiles.

Une bonne journée, j'aurais aimé continuer et ne pas laisser au milieu :-)

## Lundi 11 Février 2024 (7h, 5/5)

Une session matinale de pair avec Yohan durant laquelle on discute de comment synchroniser l'éditeur tabulaire (on se rends compte qu'il n'y a pas besoin de grand chose), et du protocole de synchronisation. On se dit que ce serait surement mieux de réutiliser certaines parties du code plutôt que de les recréer (sérialisation et désérialisation des coordonées des features).

Je change donc le code en fonction, puis on se fait une petite réunion hebdomadaire ou on parle principalement du financement du projet. On se capte ensuite avec David. J'aimerai extraire quelques bouts de ce que j'ai fait pour en faire des *pull requests* et je lui demande des retours avant d'aller plus loin.

Je termine la journée par la rédaction d'un article de blog sur mon avancée générale sur le sujet.

## Jeudi 08 Février 2024 (6h, 4/5)

Je n'ai pas pris de notes.

## Lundi 05 Février 2024 (4h, 3/5)

Je commence par ajouter la suppression des points dans ma démo, ce qui fonctionne, et on se fait une petite session rapide avec Yohan pendant laquelle je lui demande de m'éclairer sur les endroits dans le code où je pourrais me connecter. On avance vite et ça fonctionne. J'enchaine avec la retrospective qui permet de soulever quelques points intéressants, mais qui semble frustrante pour l'équipe. On clarifie ensuite certains aspects autour du financement du projet avec David et Yohan.

## Jeudi 01 Février 2024 (1h, 3/5)

Discussion avec Yohan autour de l'API pour les requêtes, pour réussir à utiliser des classes natives JavaScript plutôt que de passer par des évènements « à la » Leaflet.

## Mercredi 31 Janvier 2024 (8h, 5/5)

J'ai enfin réussi à me concentrer. J'ai continué la réécriture et la simplification du code existant, puis j'ai ajouté du code qui pemret l'ajout d'un marker et sa modification.
Ça commence à ressembler un peu plus à quelque chose, j'ai l'impression de débloquer des bouts de trucs qui me tenaient en haleine et mécontent.
J'ai pu faire une petite vidéo de démo en fin de session.

<video controls width="80%">
  <source src="https://files.notmyidea.org/umap-sync-features.webm" type="video/webm">
</video>

## Mardi 30 Janvier 2024 (6h, 5/5)

J'ai passé du temps à refondre le code déjà écrit concernant la synchronisation. L'API se clarifie et se simplifie, ça fait du bien. On a fait une session de pair avec David durant laquelle on a pu trouver comment écouter les événements qui sont lancés lors de la création d'un point, et j'ai fini par supprimer tout un tas de complexité qui n'était pas nécessaire.

Je suis plus content du code actuel, plus simple et direct, et aussi plus facile à modifier. Bien dormir m'aide à être plus concentré !

## Lundi 29 Janvier 2024 (6h, 5/5)

Avec Yohan, on s'attaque à un bug dans les tests de l'algorithme de merge des layers. L'idée est d'attendre que certaines requêtes soient passées pour continuer les tests dans playwright (merci [`page.expect_response`](https://playwright.dev/python/docs/network#variations)).

On se rends compte que ce qu'on pensait être un test intermittent est en fait un bug: les headers `Last-Modified` et consort sont en fait à la seconde prêt, et les fichiers correspondants stockés sur le serveur à la milliseconde, ce qui fait qu'il peut y avoir prise de pinceaux dans le tapis, et le mauvais fichier est utilisé dans la reconstruction.

On a ensuite discuté avec David + Yohan de plusieurs aspects, autour de la solution à ce problème (surement des headers maison pour éviter des soucis avec les `ETAGs` et leur utilisation par des proxy intermédiaires)

On continue avec une discussion sur notre système de versioning et sur l'idée de faire une 2.0 pour introduire des changements importants. La discussion est moins tendue que la dernière fois c'est chouette :-)

## Mercredi 24 Janvier 2024 (5h, 3/5)

Session rapide de pair avec David, on avance sur  la connection websocket et leur intégration avec les formulaires.

## Mardi 23 Janvier 2024 (5h, 4/5)

J'ai ajouté le support de la synchro pour les metadonnées de la carte sur mon prototype, j'ai fait des messages websockets + une infrastructure légère qui permet de voir venir les autres types de synchro. Je passe par l'écrasement des données de l'autre carte plutôt que par des CRDTs. Pour le moment pas de gestion de l'offline, mais je me dis que c'est secondaire.

## Lundi 22 Janvier 2024 (7h, 2/5)

Je continue sur mon prototype de synchronisation. Je commence à connecter la partie websockets, avec une implémentation avec [websockets](https://websockets.readthedocs.io) en python.

L'après-midi, j'essaye d'aller plus loin et pour les besoins de la démo de plugger [Y-WebSocket](https://github.com/yjs/y-websocket), mais je bloque (encore) sur l'utilisation de modules JS. J'essaye de contourner en faisant des pirouettes avec webpack (pour qu'il expose un module attaché à la fenêtre), mais je me retrouve face à des soucis de recursion infinie que j'ai du mal à comprendre.

Je me dis que peut-être que [Json-Joy](https://jsonjoy.com/) sera utile ici, et je commence à le plugger dans le code que j'ai fait, avant de me rendre compte que son API est un peu différente de celle de Y.js ou Automerge. Je ne comprends pas tout à fait comment utiliser le projet et je perds du temps la dessus. Je n'ai pas réussi à trouver beaucoup d'exemples d'utilisation et ça me questionne sur la documentation et l'usage réel de ce projet.

## Mardi 16 Janvier 2024 (3h, 0/5)

Discussion avec David et Yohan autour de notre manière de s'outiller. J'ai du mal à comprendre ce qui bloque, mais j'ai l'impression qu'on patine. J'ai l'impression d'apporter plus d'inconfort que l'inverse, et je ressors de la réunion avec un sentiment de frustration.

## Lundi 15 Janvier 2024 (3h, 3/5)

Une réunion avec toute l'équipe durant laquelle j'ai pu poser des questions
sur notre manière de nous organiser, et sur le role de la réunion hebdomadaire.
Je suis content de l'avoir fait, hate de voir comment les choses vont évoluer.

Une courte session avec David pour échanger sur l'approche prise pour le moment.

## Vendredi 12 Janvier 2024 (3h, 3/5)

J'ai continué à coder la piste initiée mercredi. Je me rends compte qu'il me
faudra peut-être un moyen de faire du lien entre les données, et que cette
information soit stockée quelque part (pour des re-rendus en cascade, si des
données sont dépendantes d'autres données).

En tout cas, j'ai une interface un peu plus claire pour le Mixin de `rerender`.


## Mercredi 10 Janvier 2024 (7h, 4/5)

La piste des IDs est finalement écartée pour l'instant, je ne suis pas encore
certain d'en avoir besoin, peut-être qu'il n'est pas utile d'identifier les
features de manière unique au niveau de la base de données, et que cette
information n'est utile que de manière ponctuelle pour la synchronisation de
données (avec les CRDTs).

On a changé d'approche avec Yohan pour commencer à coder et voir ou ça
bloquerait. On a commencé par ajouter de la synchro sur les champs du
formbuilder de la carte.

Je suis assez surpris par la relative simplicité de la tâche: je m'attendais à
quelque chose de bien plus compliqué, mais — en tout cas pour le formbuilder —
c'est assez simple puisque lui modifie des données qui lui sont extérieures. Il
est donc possible de se connecter sur son étape finale pour updater les données
à synchroniser.

Actuellement, des `callbacks` sont définis manuellement par le code qui appelle
le formbuilder (pour re-rendre les éléments qui en ont besoin), on factorise
tout ça, pour faire en sorte que les données qui viennent de l'extérieur mettent
aussi à jour l'interface.

Je suis content de réussir à avancer sur des trucs un peu plus concrets. Aussi
très content des discussions « en off » avec Yohan. L'impression qu'on réussi à
commencer à désamorcer certains trucs avant qu'ils ne s'installent.

En fin de journée, je repasse sur la proposition de Json Joy qui me semble
intéressante en terme d'API, et plus tournée vers des composants réutilisables.

Avec un peu de recul, les avancées de ces quelques jours ne sont pas techniques,
mais humainess. On a passé du temps à confronter des approches, avant de se
rendre compte qu'il s'agissait *aussi* de peurs chez l'un et chez l'autre, ce
qui nous a permis  de trouver un moyen de travailler ensemble plus efficacement.
Frustrant de ne pas avoir avancé techniquement, mais l'impression d'être sur de
bons rails humains, et d'avoir pu dégrossir certains aspects du code pour me les
rendre compréhensibles.

## Mardi 09 Janvier 2024 (8h, 3/5)

On discute avec Yohan de comment faire pour avancer, on commence à travailler
en pair pour plutôt décider se séparer le travail au lieu de le faire ensemble.

Yohan s'occupera de faire une séparation du code qui fait le « rendering », je
travaille sur la partie qui fait la synchronisation de données, qui va utiliser
les APIs exposées par Yohan.

Ce choix m'aide à me sentir plus à l'aise: je n'ai pas besoin de faire trop
de refactoring sur un code que je ne connais pas et qui me demande beaucoup de
temps de lecture et de compréhension.

Une discussion avec David me fait imaginer un scénario que j'avais oublié:
faire une bibliothèque Leaflet qui permet de faire de la synchro de données, de
manière générique. J'aime bien le fait que ça propose une séparation claire de
qui fait quoi, et permettrait d'avoir une frontière bien définie avec le code
actuel.

Je ne trouve pas trop ma place dans la weekly qui est plus orientée décisions
stratégiques que updates des uns et des autres. Ça me pose question, j'aimerai
bien réussir à aborder le sujet lors d'un prochain point.

Je travaille sur un bout de code qui ajoute la gestion des identifiants sur les
features GeoJSON, et j'ajoute un test dans playwright (c'est plaisant). Utiliser
des UUIDs (v4) voudrait dire avoir 36bits * 12 000 000 layers * 50 features =
21,6GB de données en plus sur la base de données de OSMFR.

Partir sur des identifiants plus courts permet d'utiliser moins d'espace.

Je suis content des bouts de discussions qu'on a pu avoir, qui entament une
réflexion sur la manière dont on travaille ensemble, ce qu'on attends l'un de
l'autre. Je me rends compte que ma confiance en moi est faible, et que j'ai
besoin de la conforter avant d'être efficace pour travailler avec d'autres.

Content de la découverte, et d'avoir pu l'expliciter auprès de Yohan.
J'espère que ça débouchera sur quelque chose de sain et productif.

## Lundi 08 Janvier 2024 (9h, 3/5)

Matinée passée et début d'après midi avec Yohan à faire une release de uMap puis
à faire du bugfix dessus ensuite. Fin d'après-midi à discuter de la manière dont
on peut imaginer la suite du travail ensemble. On patine un peu, on a du mal à
trouver une manière de fonctionner qui nous convienne à tous les deux.

## Lundi 18 Décembre 2023 (9h, 5/5)

J'ai creusé sur mon idée de faire en sorte de synchroniser un point, j'ai une meilleure compréhension de ou m'insérer dans le code, et j'ai pu commencer à coder un bout de code qui fait la connexion avec le stockage.

J'ai aussi commencé à coder la partie stockage, en mettant de côté pour le moment la partie CRDT en tant que telle, j'ai l'impression de voir comment ça va fonctionner maintenant, et l'intégration avec Y.JS me semble difficile sans utiliser de bundler js, ce qui est peut-être un signe qu'il faut aller voir ailleurs (Json Joy me fait de l'oeil)

J'ai découvert la documentation de Leaflet [sur comment les objets fonctionnent](https://leafletjs.com/reference.html#class) et la documentation de [Leaflet Editable](http://leaflet.github.io/Leaflet.Editable/doc/api.html#editable) qui étaient en fait des lectures indispensables à la bonne compréhension du code de umap.

On a terminé la journée avec une session de pair avec Yohan qui était vraiment bien :  j'avais des questions précises et on a pu avancer ensemble vers plus de clarté.

## Samedi 16 Décembre 2023 (4h, 5/5)

J'ai eu envie de commencer à m'intégrer avec uMap, pour ce qui est de la synchronisation des données. Pas forcement pour faire les choses *en version finale*, mais plutôt pour avancer un peu sur ma compréhension du code de manière générale.

Objectif: faire de la synchronisation de données pour un point. Quand il est ajouté sur une carte, je veux pouvoir récupérer un évènement de l'autre côté et l'afficher sur cette seconde carte. Éventuellement j'aimerai bien pouvoir suivre le drag-n-drop également.

J'ai passé l'aprèm à mettre des petits points d'arrêts dans mon navigateur web, pour mieux comprendre où ce serait le plus logique de m'insérer pour voir les modifications sur la carte, pour enfin commencer à ajouter `Y.js` dans le code (en tant que module).

Le fait qu'on utilise pas de bundler rends les choses un peu plus compliquées, mais je suis content d'avoir la main sur comment les choses sont faites.

J'ai un peu bloqué sur l'utilisation de Y.JS, qui s'attends à ce que d'autres modules soient disponibles dans des namespaces spécifiques, ce qui ne correspond pas vraiment à nos pratiques.

J'ai découvert [import maps]() et j'ai commencé à les utiliser, mais ça ne semble pas suffire pour notre approche "simpliste". En tout cas, pas pour Y.JS (https://github.com/yjs/yjs/issues/325)

## Vendredi 15 Décembre 2023 (7h, 3/5)

🚗 J'ai travaillé depuis la maison, suite à des soucis de voiture. 

J'ai continué le travail sur l'ajout de l'utilisation de modules Javascript, pour pouvoir gérer les imports et les exports, plutôt que d'avoir tout dans le namespace global.

J'ai pu discuter avec Vincent puis avec David du sujet. Je suis content [de l'approche prise](https://github.com/umap-project/umap/pull/1463), qui devrait permettre de moderniser un peu la base de code, sans pour autant utiliser des technologies de transpilation, ni de bundling qui rendent l'expérience développeur plus complexe.

J'en ai profité pour [ajouter mes apprentissages](https://github.com/umap-project/umap/pull/1471) dans la documentation développeur, le genre d'informations que je récupère à droite à gauche et qui sont utiles pour pouvoir contribuer.

J'ai un peu réorganisé mes notes autour des différents challenges qu'on a sur ce projet concernant les différents aspects (stockage, réactivité, réconcialiation des données, transport). Et entre autre autour de la partie transport.

## Jeudi 14 Décembre 2023 (8h, 5/5)

Réunion le matin avec Yohan et NLNet, l'idée était de valider notre plan d'action, et c'est bon. Les documents sont signés on est surs d'avoir le financement. Sacrée nouvelle :-)

J'ai découvert au passage quelques bibliothèques intéressantes ([JSON Joy](https://jsonjoy.com/) et [p2panda](https://p2panda.org/)), qui pourraient potentiellement nous intéresser. 

J'ai passé un peu de temps en amont pour retravailler la proposition qu'on leur avait faite, et après pour leur donner dans le format qu'iels souhaitaient.

L'après-midi j'ai passé un peu de temps pour voir comment on pourrait utiliser des modules JS dans umap sans tout changer pour autant 😇

## Mercredi 13 Décembre 2023 (2h, 3/5)

Je n'ai pas pris de notes.

## Mardi 12 Décembre 2023 (4h, 4/5)

Matinée loupée suite à une blessure au poignet la veille au soir. Après-midi passée en partie avec David pour mettre en place l'utilisation de web components.

## Lundi 11 Décembre 2023 (8h, 5/5)

Matinée passée à imaginer comment les données pourraient êtres structurées dans le client, et comment l'interface pourrait se faire avec les objets leaflet.

Après-midi à faire un point humain, puis un point technique, avec la rencontre de (peut-être ?) notre prochaine bizdev.

Discussion technique avec David. Peut-être qu'un algorithme de merge qui serait présent sur le serveur et sur le client pourrait nous permettre de nous passer de la complexité des CRDTs?

## Mercredi 06 Décembre 2023 (6h, 3/5)

J'ai terminé de faire quelques légers changements dans la documentation, avant de me plonger dans le code javascript et de commencer à faire du refactoring.

J'ai passé du temps à comprendre comment avoir côte à côte des modules ES6 et du code de type « script ». J'ai ensuite commencé à créer des modules javascript en charge de la sauvegarde des données. En tirant les fils je me rends compte qu'il va sans doute falloir que je repasse sur le code qui s'occupe des requêtes XHR à l'ancienne, pour le remplacer par de l'async/await.

J'avais oublié à quel point faire des requêtes depuis le navigateur était compliqué à l'époque !

## Mardi 05 Décembre 2023 (8h, 4/5)

J'ai mis à plat ce que j'ai appris ces dernières semaines sur le projet, pour pouvoir décider vers où aller pour la suite des évènements.

Une discussion avec Yohan me fait pencher vers la piste que je mettais de côté à cause des changements qui sont nécessaires côté client: les CRDTs.

## Mercredi 29 Novembre 2023 (5h, 3/5)

J'ai passé du temps sur la PR du merge optimiste, pour essayer de changer le fonctionnement qui passe actuellement par la modification des champs de formulaires envoyés, ce que je ne trouve pas très clean.

Le travail pour faire autrement me semble trop important pour le moment, on accepte la PR telle quelle, avec l'idée de passer par une API plus tard, avec la refonte avec DRF.

J'ai aussi travaillé sur la documentation.

## Mardi 28 Novembre 2023 (4h, 2/5)

Travail de projection pour NLNet, puis réunion l'après-midi. J'ai ensuite repris les recherches pour affiner l'utilisation des CRDTs.

## Lundi 27 Novembre 2023 (8h, 4/5)

Matinée passée à organiser ma semaine, à participer a la présentation de NLNet (très bon accueil, et clarifications utiles), puis à faire un petit tour de uMap côté front avec Yohan.

L'après-midi j'ai commencé à intégrer les notes que j'ai prises sur le côté JS à la documentation actuelle, et j'en ai profité pour refaire un tour sur la documentation actuelle pour la simplifier et la clarifier.

## Vendredi 24 Novembre 2023 (2h, 3/5)

Réunion d'avancement et point avec David et Yohan pour préparer la suite concernant NLNet.

Je suis content d'avoir préparé le point, et je mesure l'importance donnée aux personnes dans les process.

## Jeudi 23 Novembre 2023 (3h, 4/5)

J'ai passé du temps pour faire passer les tests dans le CI, et résolu quelques problèmes au passage.

## Mercredi 22 Novembre 2023 (9h, 5/5)

J'ai exploré l'utilisation de Websockets pour le transport, entre autre sa consommation mémoire, il semblerait que ce soit tout à fait acceptable (1gb de mémoire permet de gérer 1500 connexions concurrentes).

WebRTC n'est [actuellement pas supporté par Tor Browser ](https://gitlab.torproject.org/legacy/trac/-/issues/8178)([pour le moment](https://gitlab.torproject.org/tpo/applications/tor-browser/-/issues/41021)), donc j'imagine que c'est une fausse piste.

J'ai repassé un bon coup sur la PR du merge optimiste. Je suis content du résultat: le code et des tests me semblent plus lisibles et compréhensibles.

L'après-midi à été passée avec Yohan qui m'a fait un tour du frontend. J'en ai profité pour prendre des notes que je pense publier dans la documentation. C'était très utile d'avoir ses explications, le code n'est pas si simple à prendre en main.

## Mardi 21 Novembre 2023 (8h, 4/5)

Une matinée passée à la fois à préparer la semaine et à rédiger un résumé de ce que j'ai fait la semaine dernière.
J'ai passé un peu plus de temps à comprendre en profondeur le code de merge de la PR de Biondi biondo, pour pouvoir l'expliquer dans un article de blog.

L'après-midi j'ai participé à la weekly et lu l'article de blog de Figma qui explique leur approche pour implementer du temps réel.

J'avance petit à petite sur la piste d'utiliser un CRDT "maison", voire pas de CRDT du tout, en fonction de nos besoins réels. Un CRDT nous permettrait d'avoir plusieurs personnes qui travaillent en même temps sur une même feature (au sens GeoJSON), mais je ne sais pas encore si c'est un cas d'usage réel.

## Samedi 18 Novembre 2023 (0h, 4h bénévoles, 3/5)

J'ai passé un peu de temps à intégrer l'intégration continue de Github. Je pensais que ce serait rapide mais je ne devais pas être très réveillé…

## Vendredi 17 Novembre 2023 (6h, 3/5)

J'ai passé du temps pour essayer de comprendre comment utiliser SQLite en local à l'intérieur d'un navigateur, en utilisant [cr-sqlite](https://vlcn.io/docs/cr-sqlite/intro). J'ai un prototype qui fonctionne à peu près et qui permet de récupérer les éditions en local pour les synchroniser avec une autre base SQLite.

Fait un point avec l'équipe sur l'avancement général l'après-midi.

Ensuite continué à creuser sur l'utilisation de SQLite avec cr-sqlite.


## Mardi 14 Novembre 2023 (8h, 2/5)

Une matinée passée avec Yohan pour à la fois [avancer sur la PR pour merger des conflits simples](https://github.com/umap-project/umap/pull/772/). On a passé le code en revue et fait quelques changements cosmétiques qui devraient aider à la compréhension générale.

La deuxième partie de la matinée à été utilisée pour discuter des découvertes et des questions que je me pose quand à comment faire pour ajouter ces fonctions de collaboration temps réel.

Plusieurs trucs à noter :
- Il est possible de challenger l'utilisation de geoJSON pour le stockage des données. On a parlé entre autres de pmtiles et de sqlite.

J'ai passé un début d'après-midi à installer mon environnement de travail sur Linux, puis j'ai :
- terminé de rebaser la pull request pour faire un merge optimiste.
- amélioré la vitesse d'execution des tests

Découvertes :
- https://www.geopackage.org/
- https://vlcn.io/docs/js/reactivity

## Lundi 13 Novembre 2023 (8h, 4/5)

J'ai cherché à comprendre comment il serait possible de s'intégrer avec Leaflet. Je connais assez mal l'écosystème donc j'ai cherché les plugins autour de stockage de données et de la synchronisation.

Beaucoup de clicks, de lecture et de compréhension des contours de l'écosystème SIG, et de l'écosystème de Leaflet.

J'ai aussi creusé autour des SSE et de WebRTC, question de comprendre les limites et avantages de chacun.

## Mardi 07 Novembre 2023 (8h, 3/5)

- Lu la documentation d'automerge
- Commencé à faire un prototype pour voir le fonctionnement d'automerge en python
- Installé les dépendances rust, compilé automerge
- Réunion discussion avec Yohan sur mes questions et sur les différentes pistes

## Lundi 06 Novembre 2023 (4h, 4/5)

- Lu le code qui est dans uMap actuellement pour comprendre le fonctionnement actuel
- Commencé à rédiger un document avec les différentes options pour faire de la synchro
- Fais des recherches sur les différentes options pour faire de la synchro
