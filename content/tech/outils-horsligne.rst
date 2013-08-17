Accéder à internet hors-ligne
#############################

:date: 07-06-2013
:status: draft

J'ai eu la chance de passer quelques semaines de vacances en Australie
dernièrement. Dans mes déplacements j'ai beaucoup utilisé le train et
n'avais que peu souvent accès à une connexion internet.

Et rapidement je souhaitais faire des recherches sur un tas de choses:
Que ce soit la culture Aborigène locale, les
oiseaux qu'on croisait, les insectes, les lieux, etc.

Les ressources papier existent bien évidemment et mon dos avait le plaisir de
transporter un guide assez complet. Ceci dit, il n'est pas réellement
imaginable de se trimballer avec une encyclopédie sur le dos.

À moins que…

Mise en garde
=============

`Loin de moi l'idée de vouloir utiliser du numérique partout et pour tout <|slug:usages-informatique|>`_ …

La plupart du temps le moyen que je préfère est de tout simplement discuter
avec les gens autour de moi. Mais des fois il n'y à personne autour, ou alors
les questions tomberaient comme un cheveu sur la soupe.

Avoir recours à des outils d'habitude uniquement disponibles en ligne alors que
vous n'avez pas accès à internet peut donc s'avérer réellement utile.

Je ne pense pas que j'aurais par exemple pu trouver un spécialiste des termites à l'endroit où j'en avais besoin :-)

Une encyclopédie
================

Ma première stratégie à donc été d'enregistrer des pages web pour les consulter
plus tard (Wikipedia, Wikitravel, etc, autour des sujets qui m' intéressaient.
Ça fonctionne d'ailleurs assez bien. Le problème étant qu'il faut être
*pro-actif* et savoir à l'avance ce qu'on va faire dans les jours qui viennent.

Et puis je me suis rappelé qu'il était possible de récupérer l'encyclopédie
*Wikipedia* hors ligne. J'avoue que je n'y croyais pas trop, pensant qu'il me
faudrait beaucoup plus de place que ce que mon disque dur pouvait encaisser.

Pas tant, en fin de compte: il faut 16Gb pour la version française. Il il est possible de la récupérer en `bittorrent <http://fr.wikipedia.com/bittorrent>`_, qui permet de récupérer tout ça assez rapidement.

Et paf, vous voila avec un logiciel nommé "kiwix" qui vous permet de lire
wikipedia tranquillement depuis votre ordinateur, sans connexion à internet.

C'est impressionnant ce qu'on peut trouver comme informations dans ce bijou,
à fortiori lorsqu'on n'est pas interrompu par internet tout le temps.

Cartes
======

Pour ce qui est des cartes, j'avoue que mon option préférée est tout simplement
d'avoir des cartes, des vraies, celles qu'on peut déplier. Je peux passer un
temps dingue juste à regarder une carte, je trouve ça passionnant. 

`Open street map <http://openstreetmap.org>`_ est un projet de cartographie collaborative: chacun peut modifier la carte globale pour l'enrichir avec des détails qui lui semblent utile. Et les données récoltées sont reversées sous une licence libre.

Les données existent donc, sur les serveurs d'OSM, il ne reste "juste" qu'à les
récupérer pour une utilisation hors-ligne.

XXX

Petits sites ressources
=======================

Et puis il y à plein d'autres sites qui contiennent une information précieuse,
auxquels vous souhaitez avoir accès hors-ligne. Le blog de votre grand mère
avec ses recettes de flan au Maroual, etc.

Sous linux, il existe un outil génial qui s'appelle `wget`. Il s'agit d'un
couteau suisse du téléchargement. Très simplement, *wget* permet de récupérer
hors ligne une page web, pour la consulter plus tard.

Cet outil est aussi capable de transformer les liens entre pages pour que la
navigation soit possible sur votre copie du site, etc. Pour cela il faut lui
passer quelques options::

    wget -r -k -np http://blog.notmyidea.org

Et vous avez accès à un site hors-ligne, sur votre ordinateur.
"Très bien", me direz vous, mais moi j'ai pas ton machin, "linux", là.

Je me suis amusé à faire un site rapide qui permet de récupérer d'autres sites
hors-ligne, sous forme d'archives *.zip*. Vous entrez l'adresse du site, votre
adresse email et ça s'occupe du reste pour vous !

Le site est ici: http://offline.notmyidea.org et le code ici
https://github.com/ametaireau/offline

Au cas ou ça vous serve.
