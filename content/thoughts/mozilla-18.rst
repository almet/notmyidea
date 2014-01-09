Retours sur un an et demi de Mozilla
####################################

Il y à un an et demi, je commançais à travailler chez Mozilla, dans l'équipe ou
je suis encore actuellement, l'équipe "services". Depuis, énormement de choses
ont évoluées, tant en ce qui concerne les objectifs de Mozilla que le travail
que j'effectue au jour le jour. Pour autant, mes objectifs personnels
restent intacts.

J'aime bien faire des points de temps à autre, donc allons-y!

Historique
==========

Un an et demi, ça me paraît énorme, c'est le temps le plus long que j'ai passé
à travailler sur un projet, avec les mêmes personnes. Si vous suivez un peu ces
carnets, vous savez surement que je travaille énormement avec `Tarek
<ziade.org>`_ par exemple.


Services
--------

Le principal de mon travail a été de construire des outils. Je suis le
mainteneur de `Cornice <https://github.com/mozilla-services/cornice>`_, un
utilitaire qui vient se greffer par dessus le framework python pyramid pour
vous simplifier la vie et créér des services web; J'ai travaillé un peu
sur un outil de gestion des process nommé `Circus
<https://github.com/mozilla-services/circus>`_, et travaille actuellement
sur un outil de montée en charge dénommé `Loads
<https://github.com/mozilla-servbices/loads>`_

Au tout début de ma *mission*, j'ai travaillé sur un concept de `serveur de
tokens <https://github.com/mozilla-services/tokenserver>`_. L'idée était de
désolidariser l'authentification des services web des services eux mêmes.

L'idée est (je pense) bonne mais le service n'à jamais été utilisé. La raison
étant principalement que Sync, pour lequel le serveur de token à été développé
est en train d'être réécrit et repensé (voir le projet nommé `Profile In The
Cloud <https://wiki.mozilla.org/Identity/PiCL>`_

J'avoue que mettre un projet au rebut comme celui-ci, sans être réellement
prévenu est un peu dur, mais bon, il paraît que ça arrive. L'écriture de celui
ci n'a pas été vaine, puisque Circus est né de besoins la bas, ainsi que beaucoup
d'enseignements personnels.

Marketplace: chouette, on va casser du serveur.
-----------------------------------------------

Après 6 mois à travailler à Services, nous avons commencé à rejoindre l'équipe
du Marketplace pour faire un travail d'audit de performance.

L'idée était de prêter main forte à l'équipe du marketplace, mais les détails
étaient alors assez flous. Le code de marketplace est assez indigeste au
premier abord, ce qui m'avait alors pas mal refroidi. La raison principale
étant que le code est utilisé à la fois par addons.mozilla.org et par
marketplace.firefox.com, rendant les choses souvent un peu plus compliquées
qu'il ne faudrait.

Il y à actullement énormement d'efforts qui sont fait pour aller dans la bonne
direction et faire en sorte que le code soit plus facile à maintenir et que le
projet soit plus facile à aborder.

Une partie du plan à été de sortir certaines fonctionnalités du code du
marketplace, pour en faire quelque chose de plus facile à maintenir et de moins
imbriqué. `Monolith <https://github.com/mozilla/monolith>`_ est le projet qui
fait sortir les statistiques du marketplace, sur lequel j'ai travaillé.

La Communauté
-------------

Circus et Cornice sont deux outils qui semblent utiles à la communauté. J'ai eu
des retours très positifs sur Cornice, et j'essaye de le faire évoluer dans la
direction qui me semble propice.

Nous utilisons actuellement Cornice pour coder `Daybed
<https://github.com/spiral-project/daybed>`_ un service de validation de
formulaires.

Circus commence à recevoir des contributions de plus en plus intéressantes, et
à être utilisé en interne chez nous et chez d'autres, donc c'est une
extrêmement bonne nouvelle !


Enseignements
=============

Mozilla est ma première expérience professionnelle, et par conséquent, je
manque nécessairement de recul sur ce qui est acceptable et ce qui ne l'est
pas. D'une manière générale, avoir un environnement de travail basé sur la
confiance est réellement appréciable.

J'ai encore un peu de mal à savoir quels indicateurs utiliser pour savoir si je
suis "productif" ou non, mais j'ai globalement l'impression que je manque de
concentration et de discipline: prioriser les tâches sur lesquelles je vais
travailler se fait quasiment au jour le jour alors qu'il serait possible de
faire autrement.


Malheureusement, le code n'est pas propre
-----------------------------------------

Je me rends compte que bien souvent je suis assez déçu de la qualité du code
que je regarde. Principalement parce que je ne suis pas capable de le
comprendre rapidement. Spécifiquement, ça m'est arrivé avec certaines parties
de Zamboni, le code du Marketplace dont je parlais plus haut.

C'était extrêmement frustrant pour moi de découvrir que le code écrit à Mozilla
n'était pas exemplaire. Tout le code qui est ajouté à l'heure actuelle est
revu, corrigé et validé par des pairs, mais un certain nombre de projets ont un
historique assez lourd qui rends leur structure complexe.

Je réalise donc que mon travail n'est pas uniquement de savoir écrire du code
propre, mais également de réussir à comprendre du code que je considère comme
"sale" (quitte à l'améliorer au passage !)

Apprendre est un processus actif
--------------------------------

Il est facile de passer à coté de l'apprentissage. Être entouré de gens
talentueux ne suffit pas toujours à continuer à apprendre.

Savoir reconnaitre le fait d'être en situation d'échec est nécessaire. Dire que
l'on comprends pour éviter de passer pour un idiot est un biais qui se prends
assez rapidement, et qu'il fait éviter à tout prix.

Il y a une espèce de honte de ne pas savoir, alors que tout le monde autour
sait ou en tout cas semble savoir. Bien souvent, les gens autour ne savent pas
non plus, ce qui mène à des discussions de comptoir, sans trop savoir pourquoi.

Connaître ses limites techniques est un bon début pour pouvoir les
surpasser.

"Assez bien" est suffisant
--------------------------

La culture de l'excellence 


Écrire des boites à outils et non pas des frameworks
----------------------------------------------------

Écrire des frameworks force les utilisateurs à


Être le moteur de son propre changement
---------------------------------------


La suite ?
==========


