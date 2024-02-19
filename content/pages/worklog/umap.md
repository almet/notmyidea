---
title: uMap
save_as: umap/index.html
template: worklog
total_days: 25
---

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
