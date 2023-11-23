---
title: Argos
save_as: argos/index.html
template: worklog
total_days: 8
---

## Mardi 23 Novembre 2023 (0h, 1h bénévoles, 5/5)

J'ai passé un peu de temps à répondre a des tickets, merger et faire des petites modifications dans le code, c'était très plaisant.

Il est maintenant [possible de lancer le serveur depuis l'extérieur du venv](https://framagit.org/framasoft/framaspace/argos/-/merge_requests/8), et j'ai lu quelques demandes de modifications de Luc.

## Jeudi 16 Novembre 2023 (0h, 1h bénévoles, 5/5)

- [Migré vers la nouvelle manière de définir la config dans Pydantic](https://framagit.org/framasoft/framaspace/argos/-/merge_requests/6)

## Lundi 06 Novembre 2023 (0h, 2h bénévoles, 5/5)

J'ai passé un peu de temps avec Matthieu Leplatre pour faire une revue du code que j'ai écrit. 

## Jeudi 19 Octobre 2023 (6h, 2h bénévoles, 5/5)

Préparation de la discussion avec Luc, puis j'ai ajouté de la documentation et j'ai fait pas mal de finitions.

## Mercredi 18 Octobre 2023 (7h, 1h bénévoles, 5/5)

J'ai passé une journée de travail dessus.
Beaucoup de choses faites. La base de code est plus solide, et surtout testée ce qui me rassure.

## Mardi 17 Octobre 2023 (1h, 4/5)

- J'ai ajouté les dépendences dans le pyproject.toml
- Updated the CLI interface

## Mercredi 11 Octobre 2023 (7h, 1h bénévoles, 4/5)

J'ai passé la journée dessus.Il me reste 3 demi journées.

J'ai passé beaucoup de temps à mettre en place des tests au niveau de l'app. La manière dont l'application était initialisée ne permettait pas de l'utiliser dans les tests. Je n'ai pas tout à fait terminé, mais je pense que c'est le moment pour essayer de passer à PostgreSQL, parce que c'est ce qui va tourner en production.

De ce que je comprends, plusieurs approches :
1. Utiliser une connection pool
2. Faire des requêtes en asynchrone (voir [la doc](https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html))

Je suis vraiment pas loin d'un truc bien, j'aimerai quand même vraiment avoir des tests pour tester les cas limites, là beaucoup de choses se font à vue et j'ai peur que des bugs ne se cachent.

Fait :

  - [x] Ajouter une notion de sévérité dans la config
  - [x] Ajouter une notion de fréquence dans la config

## Mardi 10 Octobre 2023 (5h, 4/5)

  - [x] Sécuriser les appels des agents au backend
  - [x] Ajouter le support pour les !include

## Lundi 09 Octobre 2023 (7h, 4/5)

- [x] Terminer le backend de vérification SSL
- [x] Décider comment faire pour faire remonter les différents niveaux d'alerte (L'agent ne devrait pas décider, c'est le travail du serveur)

J'ai pas mal refactoré le code, et c'est maintenant possible de faire une partie des checks (la finalisation) côté serveur. Nous avons aussi maintenant un check SSL fonctionnel.
    
La base de données gère maintenant une relation, et j'ai commencé à écrire quelques tests également, ainsi que packagé ça dans un package python.
    
C'était plutôt une journée un peu décousue, mais je suis content du résultat. C'était beaucoup de grosses modifications et donc avoir le temps de le faire pour avoir le contexte en tête aide pas mal.

## Jeudi 05 Octobre 2023 (2h, 4/5)
  
Je n'ai pas pris de notes.

## Mercredi 04 Octobre 2023 (4h, 4/5)
  
J'ai pu avancer, mais je me suis confronté à plusieurs soucis de concentration. Ici au coworking c'est aussi un endroit pour socialiser, et donc je suis moins efficace. Les pomodoros m'aident à me recentrer, j'ai quasiment une API fonctionnelle. Je galère un peu avec Pydantic parce que je ne le connais pas encore bien, j'espère que ce sont des efforts qui vont payer sur le long terme.
  
La prochaine fois je pense avancer sur les requêtes pour ordonnancer tout ça, et faire quelques tests pour valider que tout marche bien comme je veux.

## Mardi 03 Octobre 2023 (3h, 4/5)
  
Session de travail assez agréable. J'ai commencé à faire fonctionner l'outil, et je commence maintenant à travailler sur les checks en tant que tels. Je sens qu'il t a quelques fragilités au niveau de la structure des données (schémas / validation avec Pydantic).
  
Je pense que la prochaine étape sera de faire tous les checks, et de les faire retourner des données à l'API. Puis ensuite de s'assurer que les jobs ne sont pas distribués à plusieurs workers en paralelle.


## Lundi 02 Octobre 2023 (4h, 4/5)
  
Je suis content de cette session de travail. J'ai repensé encore une fois le modèle de données pour arriver à quelque chose qui me semble mieux. J'ai continué à travailler sur la codebase avec fastapi que je trouve plus élégante et sur laquelle il sera possible de passer en asynchrone ensuite.
  
Les fichiers de configuration, une fois parsés, permettent de créer les enregistrements dans la base de données. La première version de l'API est bientôt prête. La prochaine étape est de bosser sur les workers.

## Mercredi 27 Septembre 2023 (4h, 4/5)
  
1h pour mettre en place un bouncer ZNC. J'ai plutôt fait des recherches sur des outils alternatifs pour l'API, suite à mon impression de passer du temps à refaire des choses qui sont déjà fournies par d'autres outils. J'espère que c'était une bonne idée ! Le prix à payer pour me remettre le pied à l'étrier. En fin de journée j'ai réussi à vraiment réfléchir au problème métier, et à déterminer un bon modèle de données ainsi que des scénarios d'utilisation. Au final, je pense qu'il faut passer par fastapi (qui propose de l'asynchrone ASGI de base) mais rester sur SQLAlchemy (Pewee à une API qui semble plus simple, mais qui ne supporte pas très bien l'asynchronicité). Pour la suite, je pense qu'il faut que je me concentre plus sur les fonctionalités de base.

## Mardi 26 Septembre 2023 (4h, 4/5)
  
J'ai continué de bootstrapper et j'ai importé des bouts de codes qui manquaient pour lancer le serveur web, gérer la configuration du service, la gestion de la base de données, des migrations etc.
  
## Lundi 25 Septembre 2023 (3h, 4/5)
  
J'ai commencé à boostraper le projet, fait un module qui est capable de lire le fichier de configuration (en YAML) et de valider que ce qui s'y trouve est correct. J'utilise Pydantic pour ça, que je ne connaissais pas.