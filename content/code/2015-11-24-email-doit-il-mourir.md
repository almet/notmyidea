title: Le mail doit-il mourir ?
headline: Le mail est un protocole bien établi qui souffre de nombreux problèmes. Est-ce qu'il ne serait pas temps de préparer la suite ?

J'utilise quotidiennement le protocole email, tant bien que mal, tout en sachant que l'ensemble de mes messages passent en clair sur le réseau pour la plupart de mes conversations, puisque trop peu de monde utilise le chiffrement des messages.

Et même si j'arrive à convaincre certains de mes proches à installer PGP, je ne suis pas satisfait du résultat: les méta-données (qui contacte qui à quel
moment, et pour lui dire quoi) transitent de toute manière, elles, en clair, à la vue de tous.

Ce problème est lié directement au protocole email: il est *necessaire* de faire fuiter ces meta-données (au moins le destinataire) pour avoir un protocole
mail fonctionnel.

Le mail répond à un besoin de communication asynchrone qui permet des conversations plus réfléchies qu'un simple chat (miaou). Il est tout à fait possible d'utiliser certaines technologies existantes afin de construire le futur de l'email, pour lequel:

- Les méta-données seraient chiffrées — Il n'est pas possible de savoir qui
  communique avec qui, et quand;
- Le chiffrement serait fort (et protégé d'une phrase de passe ?);
- La fuite d'une clé de chiffrement utilisée dans un échange ne permette pas de
  déchiffrer l'ensemble des échanges (forward secrecy);
- Il ne soit pas possible de réutiliser les données comme preuve pour
  incriminer l'emmeteur du message (deniability);

Avec au moins ces besoins en tête, il semble qu'une revue de l'ensemble des projets existants pointe du doigt vers [pond](https://github.com/agl/pond), ou vers [Signal](https://www.whispersystems.org).

Malheureusement, Pond est le projet d'une seule personne, qui veut plutôt utiliser ce code comme démonstration du concept en question.