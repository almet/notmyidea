Retours sur deux ans à Mozilla
##############################

:date: 2014-07-29

.. note:: 

  Ça fait un bail que j'ai cet article en cours de rédaction, et je me dis que
  je dois le poster maintenant, sinon je ne le ferais jamais (saloperie de
  perfectionnisme ?)

Il y à deux ans et demi, en décembre, je commençais à travailler chez
Mozilla, dans l'équipe "Cloud Services".

Depuis, énormément de choses ont évoluées, tant en ce qui concerne les
objectifs de Mozilla (avec l'arrivée de FirefoxOS) que le travail que
j'effectue au jour le jour. Pour autant, mes objectifs personnels restent
intacts.

Deux ans ça parait énorme, c'est le temps le plus long que j'ai passé
à travailler sur un projet, avec quasiment les mêmes personnes. Si vous suivez
un peu ces carnets, vous savez surement que j'ai beaucoup travaillé avec `Tarek
<ziade.org>`_ par exemple.

Ça a été (et c'est toujours) un réel plaisir de bosser avec la personne dont
j'avais lu les livres pour apprendre le python, merci !

Services
--------

Le principal de mon travail a été de construire des outils. Je suis le
mainteneur de `Cornice <https://github.com/mozilla-services/cornice>`_, un
utilitaire qui vient se greffer par dessus `le framework python pyramid
<http://docs.pylonsproject.org/projects/pyramid/en/latest/>`_ pour
vous simplifier la vie et créer des services web; J'ai travaillé un peu
sur un outil de gestion des processus nommé `Circus
<https://github.com/mozilla-services/circus>`_, et également sur un outil de
montée en charge dénommé `Loads <https://github.com/mozilla-services/loads>`_

Au tout début, j'ai travaillé sur un concept de `serveur de
tokens <https://github.com/mozilla-services/tokenserver>`_. L'idée était de
désolidariser l'authentification des services web des services eux mêmes.

L'idée est (je pense) bonne mais le service n'a pas été utilisé durant plus de
deux ans. La raison étant principalement que Sync, pour lequel le serveur de
tokens a été écrit, a subi des changements majeurs (qui sont rentrés en
production il y a quelques semaines)

Circus est né de besoins découverts via le token server, et il m'a
personnellement beaucoup appris. Le token server est finalement utilisé dans la
nouvelle version de Sync qui est rentrée en production il y a peu.

Marketplace ("chouette, on va casser du serveur")
-------------------------------------------------

Après 6 mois à travailler à Services, Tarek et moi avons commencé à rejoindre
l'équipe du Marketplace pour faire un travail d'"audit de performance".

L'idée était de prêter main forte à l'équipe du marketplace, mais les détails
étaient alors assez flous. Le code est assez indigeste au premier abord, ce qui
m'avait alors pas mal refroidi. La raison principale étant que le code est
utilisé à la fois par `addons.mozilla.org` et par `marketplace.firefox.com`,
rendant les choses souvent un peu plus compliquées qu'il ne faudrait.

Cet "audit" a été l'occasion de travailler sur des outils de montée en charge
assez sympa, qui ont donné naissance à un projet qu'on utilise assez souvent
maintenant, `Loads`_.

Énormément d'efforts sont fait pour aller dans la bonne direction et faire en
sorte que le code soit plus facile à maintenir et que le projet soit plus
facile à aborder. D'ailleurs, pas mal de copains djangonautes français
travaillent dessus (salut `Mathieu <http://virgule.net>`_, Yohan, `David
<http://larlet.fr>`_ et `Mathieu Agopian <http://mathieu.agopian.info>`_!)

Une partie de notre plan a été de sortir certaines fonctionnalités du code
actuel, pour en faire quelque chose de plus facile à maintenir et de moins
imbriqué. 

La Communauté
-------------

`Circus`_ et `Cornice`_ sont
deux outils qui semblent utiles à la communauté. J'ai eu des retours très
positifs sur Cornice, et j'essaye de le faire évoluer dans la direction qui me
semble propice.

D'ailleurs, Cornice est utilisé (par `Mathieu L.
<http://blog.mathieu-leplatre.info/pages/about.html>`_
— encore un —, `Rémy <http://twitter.com/natim>`_ et moi) actuellement pour coder
`Daybed <https://github.com/spiral-project/daybed>`_ un service de validation
de formulaires, mais ça sera l'objet d'un futur billet.

Circus commence à recevoir des contributions de plus en plus intéressantes, et
à être utilisé en interne chez nous et chez d'autres, donc c'est une
extrêmement bonne nouvelle.

Talkilla / Loop
---------------

Après quelques temps, j'avais envie d'apprendre de nouveau. Python c'est génial
mais c'était devenu ma "zone de confort". J'adore découvrir des choses, donc
c'était le moment de faire en sorte que ça continue!

C'était aussi l'occasion de travailler avec `Nicolas
<https://nicolas.perriault.net/>`_ et `Romain <http://monkeypatch.me/blog/>`_.
Je suivais le projet Talkilla de plus ou moins loin depuis quelques mois,
c'était donc l'occasion à ne pas manquer.


En rentrant dans cette équipe, je cherchais principalement à avoir un projet
visible pour les utilisateurs finaux. Refaire un peu de frontend, apprendre
à faire du JavaScript propre et découvrir de nouvelles personnes.

J'y ai aussi récupéré une équipe qui essaye de suivre les principes de
l'agilité et qui est sur mon fuseau horaire (pour la plupart). Le rêve.

L'idée derrière Talkilla est d'utiliser la technologie de communication pair
à pair dans les navigateurs (WebRTC) pour faire des appels audio / vidéo. En
d'autres termes, c'est un peu transformer votre firefox en téléphone, sauf que
personne ne peut espionner ce qui se passe entre vous et l'autre bout du fil.

A peine arrivé dans le projet (peut-être un mois et quelques après mon
débarquement) le choix a été fait de tout réécrire depuis zéro, dans un projet
qui se nomme actuellement "Loop", qui veut proposer la même chose, mais inclus
directement dans Firefox.

C'est en bonne voie, on a quelque chose qui fonctionne dans nightly, et le code
du serveur fonctionne pas mal. Le code du serveur est ici:
https://github.com/mozilla-services/loop-server.

Un client est en train d'être implémenté dans Firefox et un autre en tant
qu'application pour FirefoxOS. Le boulot ne s'arrête pas de pleuvoir, mais je
pense qu'on va dans une direction intéressante.

Pour être complètement terminé, il faudrait qu'on soit capable de se passer
complètement de notre provider, TokBox (que l'on utilise en tant que relai
média), pour que n'importe qui puisse choisir d'utiliser son propre serveur
STUN / TURN et installe son serveur loop chez lui.

Le travail à distance
=====================

Quand j'ai commencé à travailler à Mozilla, j'ai décidé de venir m'installer
à Paris. La plupart des personnes de mon entourage ont d'ailleurs fait des gros
yeux, parce qu'ils connaissaient mon avis sur la ville en question, mais casser
des préjugés n'est jamais une mauvaise chose.

Après deux ans passés à Paris, j'ai décidé de partir m'installer à Rennes,
puisque de toute manière, la plupart de mon travail s'effectue au jour le jour
à distance. En d'autres termes, la plupart de mon équipe n'est pas à coté de
moi quand je travaille, ce qui veut dire que je peux travailler depuis
n'importe où.

Ce qui fonctionne pour moi, c'est de ne quasiment jamais travailler depuis la
maison. J'utilise `un espace de coworking <http://www.lacantine-rennes.net/>`_
qui est un moyen de garder ma vie perso séparée de ma vie privée et de
rencontrer des gens passionnés par ce qu'ils font.

Depuis que je suis arrivé à Rennes, Rémy a commencé à travailler avec moi, et
c'est un réel bonheur que de pouvoir partager des journées de travail. On
"pair-prog" énormément et j'ai l'impression d'avoir un boost dans ma
productivité quotidienne.

Enseignements
=============

Mozilla est ma première expérience professionnelle, et par conséquent, je
manque nécessairement de recul sur ce qui est acceptable et ce qui ne l'est
pas. D'une manière générale, avoir un environnement de travail basé sur la
confiance est réellement appréciable (La première réaction des gens quand je
dis que je peux travailler à distance, c'est de me demander comment ils font
pour être sur que je travaille. Et la réponse est… il n'y en a pas).

J'ai encore un peu de mal à savoir quels indicateurs utiliser pour savoir si je
suis "productif" ou non, mais j'ai globalement l'impression que je manque de
concentration et de discipline: beaucoup d'interruptions n'aident pas à se
concentrer.

La motivation fluctue aussi énormément: un jour on est super motivé, un autre
c'est juste impossible de la trouver. Après quelques expérimentations, le mieux
(pour moi) est d'avoir des horaires fixes, pour pouvoir séparer le travail du
reste, de ne pas hésiter à faire des pauses et d'écouter un peu ses envies et
son corps (si je suis crevé, ça ne sert à rien de se lever pour aller
travailler, il vaut mieux se reposer un peu pour être plus efficace ensuite,
par exemple).

J'ai essayé de tirer quelques enseignements de ces deux années:


Malheureusement, le code n'est pas propre
-----------------------------------------

Je me rends compte que bien souvent je suis assez déçu de la qualité du code
que je regarde. Principalement parce que je ne suis pas capable de le
comprendre rapidement. Spécifiquement, ça m'est arrivé avec certaines parties
de `Zamboni <https://github.com/mozilla/zamboni>`_, le code du `Marketplace
<http://marketplace.firefox.com>`_ dont je parlais plus haut, avec certaines
parties de Talkilla ou alors le code de Firefox lui même.

C'était extrêmement frustrant pour moi de découvrir que le code écrit à Mozilla
n'était pas exemplaire. Tout le code qui est ajouté à l'heure actuelle est
revu, corrigé et validé par des pairs, mais un certain nombre de projets ont un
historique assez lourd qui rends leur structure complexe.

Je réalise donc que mon travail n'est pas uniquement de savoir écrire du code
propre, mais également de réussir à comprendre du code que je considère comme
"sale" (quitte à l'améliorer au passage !).

Et c'est pas du gâteau; je m'attendais à réussir à comprendre des projets
complexes facilement, mais aucun miracle de ce coté là. Il faut réussir
à rester concentré pendant suffisamment longtemps pour pouvoir tirer tous les
fils et commencer à démêler… Pas facile !

Apprendre est un processus actif
--------------------------------

Il est facile de passer à coté de l'apprentissage. Être entouré de gens
talentueux ne suffit pas pour continuer à apprendre.

Savoir reconnaitre un échec est nécessaire. Dire que l'on comprends pour éviter
de passer pour un idiot est un biais qui se prends assez rapidement, et qu'il
faut éviter à tout prix.

Surtout au début, c'était une erreur que je faisais énormément, une question
d'égo probablement.

Il y a une espèce de honte de ne pas savoir, alors que tout le monde autour
sait ou en tout cas semble savoir. Bien souvent, les gens autour ne savent pas
non plus, ce qui mène à des discussions de comptoir, sans trop savoir pourquoi.

Connaître ses limites techniques est un bon début pour pouvoir les surpasser.
Chercher à les rencontrer est un processus actif.

Le manque de temps m'empêche bien souvent de pouvoir prendre un livre technique
et de pouvoir l'apprécier. Je ne sais pas exactement pourquoi, peut être par
sur-dose, mais je n'ai ouvert que quelques rares livres techniques durant ces
deux années. Et j'aimerais bien que ça change !


"Assez bien" est suffisant
--------------------------

La culture de l'excellence se mets parfois au milieu du chemin. On oublie
souvent que "le mieux est l'ennemi du bien".

Rien ne sert de faire des commits parfaits tout le temps. Quand j'ai besoin de
"hacker" sur un projet, je ne voulais d'abord pas tout péter, par peur de ne
plus m'y retrouver.

Mon approche actuelle est bien différente: on mets les mains dans le cambouis
jusqu'à ce que ça marche, et ensuite on répare les dégâts. Enfin… dans une
certaine mesure hein !


Écrire des boites à outils et non pas des frameworks
----------------------------------------------------

Écrire des frameworks force les utilisateurs à les utiliser, et à les connaitre
dans les moindres recoins. Heureusement, il existe déjà énormément de
frameworks qui pour la plupart font très bien leur travail. Ce qui nous manque
ce n'est pas plus de frameworks, mais bel et bien plus de boites à outils.

Une boite à outil prends un problème bien défini et propose une solution pour
ce problème. Une boite à outils est, en mon sens, ce qu'on appelle une
bibliothèque. Pas besoin de réécrire tout votre projet pour utiliser ma
nouvelle bibliothèque afin de profiter des fonctionnalités qu'elle apporte
(alors que c'est le cas avec un framework, justement).


Être le moteur de son propre changement
---------------------------------------

Facile à dire, héhé ! D'une manière générale, je me rends compte qu'il est
facile de se plaindre sans pour autant être moteur du changement que l'on
souhaite voir arriver.

Ça vaut le coup de se donner la peine de faire changer les choses, surtout
à Mozilla, parce que le changement n'est pas seulement vu d'un mauvais œil.

Pour que les choses évoluent, il faut être force de proposition. Se plaindre
n'a jamais servi à rien si ce n'est pas suivi d'actes ;)

Je dis de temps en temps que Mozilla est une "do-o-cratie" (celui qui fait
à raison), et je le pense de plus en plus. Quand j'ai envie que quelque chose
soit fait, et bah… il faut le faire !


Ne pas chercher à avoir raison
------------------------------

Peu importe qui a raison, l'important n'est pas de chercher à montrer que tu
sais, mais de trouver ce qui est juste. Ça parait peut être évident, mais bien
souvent on cherche à se mettre en avant, au détriment du projet… Allez, gardons
nos égos de coté ;)

Arrêter le négativisme
----------------------

Il est très facile de se laisser embarquer dans le négativisme. Il y a toujours
des choses qui ne vont pas, et probablement il y en aura toujours. Ce ne sont
pas des raisons suffisantes pour perdre le moral. Identifier les points faibles
est important est permet de savoir ce qu'il est nécessaire d'améliorer, mais
regarder les choses du coté positif (et il y en a nécessairement un !) est
indispensable !

À plusieurs reprises je me suis retrouvé dans des crises de négativisme, pour
un tas de raisons différentes. La meilleure manière de s'en sortir: en causer
et trouver des solutions, prendre le problème à bras le corps, et ne pas
considérer que c'est un problème sur lequel on a aucune prise possible.

La suite ?
==========

Je n'ai aucune idée d'à quoi va ressembler la suite, et c'est justement ce que
j'apprécie et qui m'effraie en même temps…

Je fais actuellement énormément de Javascript et je travaille sur des
projets qui semblent avoir plus de sens qu'avant (même si je vois déjà des
choses que je souhaiterais améliorer, mais chaque chose en son temps). Donc
techniquement j'apprends et dans ma quête de faire des produits qui touchent un
utilisateur.

Depuis quelques semaines, je peux travailler une journée par semaine sur un
projet qui me tiens vraiment à cœur: daybed (http://daybed.rtfd.org).
L'objectif est de faire en sorte que le projet avance et soit utilisé au sein
de mozilla.

Avant toute autre chose, il faudra faire des changements de "pitch" pour qu'il
soit plus simple d'expliquer ce que Daybed souhaite faire, mais… c'est une autre
histoire.
