Le mail doit mourir
###################

:status: draft
:date: 2015-11-24
:headline: Le mail est un protocole qui bien établi qui souffre de nombreux
           problèmes. Est-ce qu'il ne serait pas temps de préparer la suite ?


J'utilise quotidiennent le protocole email, tant bien que mal, tout en sachant
que l'ensemble de mes messages passent en clair sur le réseau pour la plupart
de mes conversations, puisque trop peu de monde utilise le chiffrement des
messages.

Et même si j'arrive à convaincre certains de mes proches à installer PGP, je ne
suis pas satisfait du résultat: les méta-données (qui contacte qui à quel
moment, et pour lui dire quoi) transitent de toute manière, elles, en clair,
à la vue de tous.

Ce problème est lié directement au protocole email: il est *necessaire* de
faire fuiter les metadonnées (au moins le destinataire) pour avoir un protocole
mail fonctionnel.

Le mail réponds à un besoin de communication asynchrone qui permet des
conversations plus réfléchies qu'un simple chat. Il est tout à fait possible
d'utiliser certaines technologies existantes afin de constuire le futur de
l'email, pour lequel:

- Les méta-données sont chiffrées — Il ne soit pas possible de savoir qui
  communique avec qui, et quand;
- Le chiffrement est fort et protégé d'une phrase de passe;
- La saisie d'une clé utilisée dans un échange ne permette pas de déchiffrer
  l'ensemble des échanges (forward secrecy);
- Il ne soit pas possible de réutiliser les données pour incriminer l'emmeteur
  ou le recepteur des messages (deniability);

Avec au moins ces besoins en tête, il semble qu'une revue de l'ensemble des
projets existants pointe du doigt vers `pond <https://github.com/agl/pond>`_,
ou vers Signal.

Malheureusement, Pond est le projet d'une seule personne, qui veut plutôt
utiliser ce code comme demonstration du concept en question.

Voici un tableau de certaines des solutions existantes. Je n'ai volontairement
pas repris l'ensemble des outils existants, et indiqué quelques points de
comparaisons qui me semblaient utiles (Nombre de developeurs, date du dernier
commit).

===========================  ======  ======  ====
Project                      Pond    Signal  PGP  
===========================  ======  ======  ====
Forward secrecy
---------------------------  ------  ------  ----
Meta-data encryption
---------------------------  ------  ------  ----
Deniability
===========================  ======  ======  ====

Hi,

As a prelude, let me say that I've been following this mailing-list since over
a year now and I've learned a bunch of interesting things, so thanks to you
all.

If I understand correctly, the email protocol is badly broken, even if used
with PGP on top of it, mainly because metadata are leaking, by design (at least
for the emitters and recipients of the messages) and that it doesn't propose
forward secrecy.

I'm looking for a protocol that allows:

- Asynchronous messaging;
- Backup-able messages;
- Forward secrecy;
- Hiding of traffic information;

This looks a lot like Pond [0], with the twist that messages are expiring in
Pond (and I would like them not to). But, I could leave with expiration of
messages, if only Pond was maintained and still worked on actively.

So here are multiple questions:

- The ideas behind Pond looks great. Do you have any


[0] https://pond.imperialviolet.org/
