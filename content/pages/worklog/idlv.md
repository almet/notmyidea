---
title: Indiens dans la ville
save_as: idlv-ghost/index.html
total_days: 2
template: worklog
---

Transformation d'un site web depuis hugo vers ghost.

## 8 Octobre 2024 (1h, 4/5)

Mise à jour de ghost suite à [une faille de sécurité](https://github.com/TryGhost/Ghost/security/advisories/GHSA-78x2-cwp9-5j42). Ce n'était pas si simple, parce que ghost veut absolument nous simplifier la vie et au final nous la rends plus compliquée 🧰

J'ai du :

- Changer la version de node qui était utilisée par défaut dans le script `ghost`:
 ```
  vim ~/.npm-packages/lib/node_modules/ghost-cli/bin/ghost
  ```
- Modifier les checks qu'il faisait pour s'assurer qu'il y avait assez d'espace disque libre, parce que ça bloquait
```
vim ~/.npm-packages/lib/node_modules/ghost-cli/lib/commands/doctor/checks/free-space.js
```
- lancer `ghost upgrade`
- relancer le worker dans l'interface d'admin
- ???
- PROFIT !

J'en ai profité pour faire la migration des services vers l'infrastructure logicielle 2024
## 12 Janvier 2023 (1h, 4/5)

Changement de la pagination par défaut. J'ai mis du temps à trouver ou était le bon réglage, mais c'était très simple une fois trouvé. Je m'attendais à trouver l'information dans l'admin, mais cela fait partie des réglages du thème.

## 30 Octobre 2023 (0h, 1h bénévoles, 2/5)

Incorporation des changements de Charly

## 13 Septembre 2023 (0h, 3h bénévoles, 3/5)

Incorporation des changements suite à discussion

## 20 Juillet 2023 (0h, 1h bénévoles, 1/5)

(Depuis les vacances)

Réponse à un mail de Charly

## 23 Juin 2023 (0h, 2h bénévoles, 3/5)

Ajout de la fonctionnalité de galerie.

## 22 Juin 2023 (0h, 1h bénévoles, 2/5)

Mail + recherches photoswipe ghost.

## 06 Juin 2023 (3h, 4/5)

- Déploiement sur Alwaysdata.
- Discussion avec leur support.
- Copie des données déjà importées
- Création des comptes pour Marin et Laura


## 05 Juin 2023 (4h, 5/5)

(Dans le train)

- Fini l'intégration du thème (quasiment)
- Importé quelques posts (mais c'est très long) et toutes les pages du site actuel.
- Me renseigner sur le fonctionnement de l'export de données dans Ghost. Il faudra faire un vrai backup des données et des fichiers.

## 01 Juin 2023 (3h, 5/5)

(Dans le train)

- Commencé le thème. Mieux compris le fonctionnement de Hugo (ma foi, c'est barré).
- Modifié le thème de base de Ghost pour reprendre l'aspect du site actuel.
- Me familiariser avec scss.
- Comprendre qu'il est possible de faire un yarn dev pour que les modifications du thème en local se retrouvent sur l'interface.

## 25 Mai 2023 (2h, 4/5)

- Installation de Ghost localement.
- Récupération de l'ancien site. Se rendre compte que les templates ne sont pas à jour.
- Conditions tarifaires de AlwaysData : 7€/mois payés annuellement (=84€HT = 100,8€ à l'année)
- Lu [la doc de Handlebar](https://handlebarsjs.com/guide/block-helpers.html#raw-blocks) et de Ghost pour les templates https://ghost.org/docs/themes/structure/
- Fait un test d'installation de Ghost sur Alwaysdata
