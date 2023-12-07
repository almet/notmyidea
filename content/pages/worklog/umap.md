---
title: uMap
save_as: umap/index.html
template: worklog
total_days: 25
---

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