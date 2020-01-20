# Packager pour Debian

Aujourd'hui j'ai fais un peu de packaging pour la distribution Linux Debian, avec l'aide d'un ami. C'était assez agréable de pouvoir me faire aider dans cet objectif : j'avais déjà tenté l'expérience en solo par le passé, et m'étais cassé les dents sur le sujet.

Voici quelques notes prises durant l'après-midi, qui pourront sans doute me servir pour la suite.

## Qu'est-ce qu'on fait ?

On essaye de créer un paquet Debian pour une application Web écrite en python. Il s'agit d'une application assez simple, qui communique avec une base de données d'un côté, et avec des utilisateurs de l'autre.

## Y aller par étapes

On a essayé de faire en sorte d'avoir quelque chose de fonctionnel assez rapidement, même si pas entièrement fait dans les règles de l'art. Ça à l'avantage de garder la motivation :-)

1. Produire un paquet `.deb` qui peut s'installer, et qui fait tourner l'application en question ;
2. Avoir un paquet qui passe les règles de validation de Debian ;
3. Intégrer le paquet avec `systemd` ;
4. Intégrer le paquet dans un système de contrôle de version type git ;

## Packaging « simple » - 1ère version fonctionnelle

On commence par faire un paquet  dit « natif ». C'est l'approche la plus simple. 
Deux fichiers sont importants, pour commencer : ``control`` et ``changelog``. Le fichier ``control`` contient un bloc « source » et un ou plusieurs blocs « package », dans l'idée de pouvoir avoir potentiellement plusieurs paquets binaires générés à partir du même package source, ce qui est utile pour les gros paquets.

Voici les étapes qu'on a suivi :

1. Créer les fichiers ``control``, ``changelog`` et ``rules`` dans le répertoire `debian`. Dans la pratique on peut les copier depuis un autre paquet qu'on prends comme modèle ;
2. Installer les dépendances de build avec ``sudo apt install devscripts && mk-build-deps -i -r --root-cmd sudo`` ;
3. Lancer ``dpkg-buildpackage -rfakeroot`` qui va construire le paquet pour nous ;
4. Regarder la sortie de la commande pour voir les dépendances qui ne sont pas déjà prêtes pour Debian ;
5. Pour les quelques dépendances qui n'étaient pas déjà prêtes, on a répété les étapes précédentes.

## Questions diverses & observations

`dh-helper` est une manière de packager « officiellement recommandée », il s'agit d'un ensemble d'outils qui cherchent à se faciliter la tache de *packaging*.

Pour les traductions : il n'est pas nécessaire de faire des paquets séparés pour la traduction, c'est acceptable de tout mettre dans le même paquet.

La documentation peut elle aussi être intégrée dans le même paquet.

Pour les numéros de version, si on a pas de tiret dans le numéro de version, alors il s'agit de la version *upstream*. Si on a un tiret, ce qui est après le numéro de version est la version du *packaging* pour Debian.

`DEB_BUILD_OPTIONS=nocheck` permet de ne pas avoir à lancer les tests à chaque fois qu'on construit le paquet.

## Étapes d'après

- Peut-être utiliser`debian/missing-sources`, en tout cas régler le souci pour les bibliothèques JavaScript et le CSS dont les sources ne sont pas distribuées actuellement (parce que versions minifiées).
- Il est possible d'installer des dépendances et de spécifier des liens symboliques à créer lors de l'installation.
- Intégrer de la documentation sous forme de `manpage`. Il semble que certains outils permettent de le faire de manière simple / automatique, comme « help2man »
- De la même manière qu'on le fait pour les ressources type JS et CSS, il faut intégrer les *fonts*, en faisant référence aux fonts empaquetées pour Debian. 
- Une fois que tout ça fonctionne, passer à un système de build qui comprends git
- Faire une intégration avec `systemd` pour avoir un service qui se lance automatiquement. Ce qui veut aussi dire créer un utilisateur spécifique pour notre service.