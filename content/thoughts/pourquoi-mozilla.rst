Pourquoi Mozilla?
#################

:date: 2012-07-16
:tags: logiciel-libre, valeurs
:lang: fr

Depuis que j'ai commencé à bosser chez Mozilla, je me retrouve assez souvent à
expliquer ce que j'y fais. J'aime bien raconter l'histoire de Mozilla, la
mission, et comment je m'y rattache.

Je prends bien sur un malin plaisir à expliquer à chaque fois les tenants et
les aboutissants, aussi je me suis dit que ça pouvait avoir du sens de l'écrire
quelque part.

Ça parle bien sur de logiciel libre, de protection de la vie privée et de
contres pouvoirs.

Je ne m'adresse pas ici aux officionados du logiciel libre et du non contrôle
du web, mais aux potentiels intéressés, qui souhaitent comprendre ce qu'on fait
à Mozilla, pourquoi et comment, et plus particulièrement quel est le rôle que
je joue la dedans.

Logiciel libre
==============

Une des premières choses qui vient à l'esprit des gens quand on parle de
Mozilla, et par extension de Firefox, c'est qu'il s'agit d'un logiciel gratuit.
D'un logiciel soit disant "libre". Avouez que le concept est de prime abord
curieux. Un logiciel qui serait libéré, mais libéré de quoi ?

Je ne vais pas refaire la génèse du logiciel et du logiciel libre, mais pour
résumer et expliquer ça très grossièrement, le logiciel libre c'est pour moi
l'idée de la collaboration. "Plutôt que de travailler chacun dans son coin,
construisons ensemble quelque chose qui nous sera utile à tous". Ça marche dans
le domaine de l'informatique parce qu'on est exposé à un bien commun non
matériel. Ce n'est pas parce que je te donne un logiciel que je ne l'ai plus.
La duplication est possible et elle rends la collaboration plus facile.

Euh, oui mais…
--------------

Ok, ok. Et comment on coopère ? Derrière un logiciel, il faut écrire des lignes
de code, il faut décrire comment doit se comporter le logiciel dans l'ensemble
des cas qu'il peut rencontrer. Mais pas seulement. Beaucoup de personnes
travaillent pour faire en sorte que Firefox soit disponible dans près de 100
langues et dialectes par exemple.

J'aime beaucoup penser que le logiciel libre réussit à réunir des personnes
avec des objectifs differents. Linux, qui est un logiciel libre est par exemple
utilisé dans beaucoup de domaines très différents tels que la médecine,
l'automobile ou l'énergie.

Le logiciel libre est une valeur clé que nous défendons chez Mozilla.

Protection de la vie privée
===========================

Mozilla en fait un peu sa devise. Nous ne sommes pas une entreprise, nous
n'avons aucun intérêt à enfermer les utilisateurs chez nous, et surtout nous
n'exploitons et n'exploiterons pas les données utilisateurs à des fins
commerciales. Point.

Stockage des données
--------------------

Un exemple qui est frappant est celui de `Sync`_, l'outil qui permet de
synchroniser les données de navigation entre plusieurs périphériques (Cela peut
être utile pour avoir votre historique de navigation partagé entre votre
ordinateur de bureau et un téléphone portable par exemple)

Les données qui sont stockées dans un service tel que sync sont cruciales: vos
mots de passe et votre historique de navigation par exemple. Imaginez ce que
des annonceurs publicitaires pourraient faire avec ces données. Il est assez
facile de connaître votre profil et donc d'ensuite faire de la publicité
ciblée à partir de ces informations. Voire pire. Donner ces données à qui fait
suffisemment pression sur vous pour les récupérer.

Heureusement, les données qui sont stockées sur les serveurs Sync sont
chifrées, et seul l'utilisateur a accès a la clé de chiffrement et de
déchiffrement. En d'autres termes, en ayant accès aux serveurs de Mozilla, même
de l'intérieur, je pourrais avoir accès à vos données mais je ne pourrais rien
en faire car celles-cis me sont impossible à déchiffrer.

Mozilla essaye de mettre le doigt la ou ça fait mal dans l'innovation web: la
publicité et le respect de la vie privée des utilisateurs. Facebook, Google,
Twitter sont autant d'entreprises qui gagnent de l'argent grâce à leurs
utilisateurs et à leurs données privées. 

Cela n'est pas *nécessairement* un mal mais il me semble important d'informer
les utilisateurs d'Internet la dessus, et de leur proposer des méthodes qui
leur permettent de protéger leur vie privée.

.. _Sync: https://www.mozilla.org/en-US/mobile/sync/

Décentralisation
----------------

Un autre aspect important est le fait que vous n'avez pas besoin de dépendre des
serveurs de Mozilla si vous ne souhaitez pas en dépendre. Bien que nous
fassions tout ce qui est en notre pouvoir pour avoir des serveurs très réactifs
et capables de tenir la charge, nous ne sommes pas à l'abri de pannes. Auquel
cas il vous faudra simplement vous armer de patience.

Mais il est possible pour vous de maintenir votre propre serveur et de ne pas
dépendre de Mozilla pour stocker vos données privées. J'ai parlé de Sync mais
Mozilla (j'en parle un peu plus bas) travaille aussi sur un système
d'exploitation pour téléphone portable, nommé Firefox OS (anciennement Boot 2
Gecko), et sur l'écosystème qui va avec.

Actuallement, si vous souhaitez synchroniser vos contacts par exemple, vous
dépendez quasiment toujours d'une autorité à qui vous ne faites peut être pas
confiance: Apple, Microsoft ou bien Google.

On ne vous propose pas simplement de nous faire confiance, on vous propose la
possibilité de ne faire confiance à qui vous souhaitez, et ça peut être vous si
vous souhaitez. La décentralisation à ceci de bon qu'elle vous laisse le choix
d'où vous souhaitez stocker vos données.

Innovation et standardisation
=============================

Mozilla, dès ses débuts, a été un laboratoire. Firefox (si je ne me trompe pas)
a été le premier navigateur à avoir des onglets. Le web, c'est cool parce que
ça bouge tout le temps !

La dernière innovation en date est Firefox OS: utilisons les technologies du
web pour créer un téléphone: utilisons le web comme plateforme, et profitons de
tout l'écosystème qui existe déjà autour de celui-ci.

C'est bien que ça bouge mais il faut qu'on se mette d'accord sur comment on
veut faire bouger les choses. La guerre des navigateurs a eu lieu. Ne pas
reproduire ça est parfois un challenge. La standardisation, tout le monde s'y
mets.

On a gagné une guerre: aux utilisateurs de choisir les outils qu'ils souhaitent
et non pas aux développeurs d'imposer leurs choix.

Et moi, qu'est-ce que je fais la dedans ?
=========================================

Je travaille donc dans l'équipe nommée Services. On travaille à la mise en
place de services web qui sont capables de tenir la charge, de fonctionner de
manière décentralisée.

Ce travail a plusieurs objectifs:

* Mettre à disposition des outils pour les développeurs, leur permettant de
  créer des services de bonne qualité rapidement;
* Permettre aux utilisateurs d'héberger eux mêmes leurs propres serveurs si ils
  le souhaitent, réduisant leur dépendance a des services externes.
* Écrire les services en question de telle manière que les utilisateurs (vous
  !) puissent les utiliser sans trop de tracas :)

Ça semble peu. mais j'aime ce boulot. Éthiquement et techniquement. C'est ça,
pour moi, la mission de Mozilla. Si vous avez des suggestions sur ce qui
pourrait être amélioré dans les services de Mozilla en termes de protection de
la vie privée, de décentralisation et de haute disponibilité, vous savez vers
qui vous tourner !

La liste des projets sur lesquels je travaille ou j'ai travaillé à Mozilla pour
l'instant:

* https://github.com/mozilla-services/tokenserver
* http://circus.io/
* http://powerhose.rtfd.org/
* https://github.com/mozilla-services/server-aitc
* http://cornice.readthedocs.org/en/latest/index.html
* https://github.com/mozilla/PyBrowserID/
* http://chaussette.readthedocs.org/en/0.3/index.html
