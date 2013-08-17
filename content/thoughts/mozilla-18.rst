Retours sur un an et demi de Mozilla
####################################

Il y à un an et demi, je commançais à travailler chez Mozilla, dans l'équipe ou
je suis encore actuellement, l'équipe "services". Depuis, énormement de choses
ont évoluées, tant en ce qui concerne les objectifs de Mozilla que le travail
que j'effectue au jour le jour. Pour autant, mes objectifs personnels
restent intacts.

J'aime bien faire des points de temps à autre, donc allons-y!

Un an et demi, ça me paraît énorme, c'est le temps le plus long que j'ai passé
à travailler sur un projet, avec les mêmes personnes. Si vous suivez un peu ces
carnets, vous savez surement que je travaille énormement avec `Tarek
<ziade.org>`_ par exemple.

Services
========

Le principal de mon travail a été de construire des outils. Je suis le
mainteneur de **Cornice**, un utilitaire qui vient se greffer par dessus pyramid
pour vous simplifier la vie et créér des services web; J'ai travaillé un peu
sur un outil de gestion des process nommé **Circus**, et travaille actuellement
sur un outil de montée en charge dénommé **Loads**.

Au tout début de ma *mission*, j'ai travaillé sur un concept de `serveur de
tokens <https://github.com/mozilla-services/tokenserver>`_. L'idée était de
désolidariser l'authentification des services web des services eux mêmes.

L'idée est (je pense) bonne mais le service n'à jamais été utilisé. La raison
étant principalement que Sync est en train d'être réécrit et repensé.

J'avoue que mettre un projet au rebut comme celui-ci, sans être réellement
prévenu est un peu dur, mais bon, il paraît que ça arrive. L'écriture de celui
ci n'à pas été vaine, puisque il en ressort Circus ainsi que beaucoup
d'enseignements personnels.

Marketplace
===========

Après 6 mois à travailler à Services, nous avons commencé à rejoindre l'équipe
du Marketplace pour travailler sur son passage à l'échelle.

Cette partie est aussi connue sous le nom de "Chouette, on va casser des serveurs".

L'idée était de prétêr main forte à l'équipe de développement du marketplace,
mais les détails étaient assez flous. Le code de marketplace est assez
indigeste au premier abord, ce qui m'à pas mal refroidi. Il y à un effort en
cours pour améliorer la qualité du code et en faire quelque chose de plus
maintenable.

Une partie du plan à été de sortir certaines fonctionalités du code du
marketplace, pour en faire quelque chose de plus facile à maintenir et de moins
imbriqué. *Monolith* est le nom du projet de qui fait sortir les statistiques
du marketplace.

La communauté
=============

Circus et Cornice sont deux outils qui sont utiles à la communauté,
semble-t-il. J'ai eu des retours très positifs sur Cornice, et j'essaye de le
faire évoluer dans la direction qui me semble propice.

Enseignements
=============

Mozilla est ma première expérience professionelle. Ça signifie que j'ai
beaucoup à apprendre, encore, et c'est tant mieux.

Voilà quelques enseignements que j'ai tiré de ce temps passé à Mozilla.


Malheureusement, le code n'est pas propre
-----------------------------------------

Je me rends compte que bien souvent je suis assez déçu de la qualité du code
que je regarde. Principalement parce que je ne suis pas capable de le
comprendre rapidement. Spécifiquement, ça m'est arrivé avec zamboni, le code du
marketplace.

C'était extremement frustrant pour moi de découvrir que le code écrit à Mozilla
n'était pas super carré. Tout le code qui est ajouté à l'heure actuelle est
revu et corrigé par des pairs, mais un certain nombre de projets ont un
historique assez lourd qui rends leur structure plus compliqué que ce qui
devrait.

Je suppose que je suis un peu trop idéaliste, pour le coup. Mon travail est
bien évidemment de savoir écrire du code propre, mais également de comprendre
du code que je considère comme "sale", quitte à l'améliorer.

Apprendre est un processus actif
--------------------------------

Il est facile de passer à coté de l'apprentissage. Être entouré de gens
talentueux ne suffit pas toujours. Ma principale erreur ici était de penser que
je savais, ou alors de dire que je savais alors que non, de toute évidence, je
ne savais pas.

Il y a une espèce de honte de ne pas savoir, alors que tout le monde autour
sait ou en tout cas semble savoir. Bien souvent, les gens autour ne savent pas
non plus et on se retrouve dans un espèce de flou artistique, sans trop savoir
pourquoi.

Connaître ses limites techniques, c'est un bon début pour pouvoir les
surpasser. Je pense que je ne voulais pas reconnaitre ma non-connaissance dans
certains dommaines, à tord.

"Assez bien" est suffisant
--------------------------

La culture de l'excellence 


"Write toolkits, not frameworks"
--------------------------------

Écrire des frameworks force les utilisateurs à
