Title: Les problèmes de PGP
Headline: Quels sont les soucis liés à PGP, que faire ?

> Flip a bit in the communication between sender and recipient and they
> will experience decryption or verification errors. How high are the
> chances they will start to exchange the data in the clear rather than
> trying to hunt down the man in the middle?
> 
> \-- <http://secushare.org/PGP>

Une fois passé l'euphorie du "il faut utiliser PGP pour l'ensemble de
nos communications", j'ai réalisé lors de discussions que PGP avait
plusieurs problèmes, parmi ceux-ci:

  - Les *meta données* (y compris le champ "sujet" de la conversation)
    sont quand même échangées en clair (il est possible de savoir qu'un
    message à été échangé entre telle et telle personne, a telle date);
  - PGP se base sur un protocole de communication qui est lui non
    chiffré, et il est donc facile de soit se tromper, soit dégrader le
    mode de conversation vers une méthode non chiffrée;
  - Il est facile de connaître votre réseau social avec PGP, puisque
    tout le principe est de signer les clés des personnes dont vous
    validez l'identité;
  - En cas de fuite de votre clé privée, tous les messages que vous avez
    chiffrés avec elle sont compromis. On dit que PGP ne fournit pas de
    *forward secrecy*;
  - La découverte de la clé de pairs se passe souvent *en clair*, sans
    utiliser une connexion "sécurisée" (HTTPS). Tout le monde peut donc
    voir ces échanges et savoir de qui vous cherchez la clé;
  - Les discussions de groupes sont très difficiles: il faut chiffrer
    pour chacun des destinataires (ou que ceux-ci partagent une paire de
    clés).

Je suis en train de creuser à propos les alternatives à PGP, par exemple
[Pond](https://pond.imperialviolet.org/), qui lui ne construit pas par
dessus un standard déjà établi, et donc n'hérite pas de ses défauts
(mais pas non plus de son réseau déjà établi).

En attendant, quelques bonnes pratiques sur PGP ;)

## Bonnes pratiques

Il est en fait assez facile d'utiliser PGP de travers. Riseup à fait [un
excellent
guide](https://help.riseup.net/en/security/message-security/openpgp/best-practices)
qui explique comment configurer son installation correctement.

  - J'en ai déjà parlé, mais il faut absolument choisir des phrases de
    passes suffisamment longues. Pas facile de les retenir, mais
    indispensable. Vous pouvez aussi avoir un document chiffré avec une
    clé que vous ne mettez jamais en ligne, qui contiens ces phrases de
    passe, au cas ou vous les oubliez.
  - Générez des clés RSA de 4096 bits, en utilisant sha512;
  - Il faut utiliser une date d'expiration de nos clés suffisamment
    proche (2 ans). Il est possible de repousser cette date si
    nécessaire, par la suite.

Parmi les choses les plus frappantes que j'ai rencontrées:

  - Utiliser le *flag* –hidden-recipient avec PGP pour ne pas dévoiler
    qui est le destinataire du message;
  - Ne pas envoyer les messages de brouillons sur votre serveur, ils le
    seraient en clair \!;
  - Utilisez HPKS pour communiquer avec les serveurs de clés, sinon tout
    le trafic est en clair.

Le [projet Bitmask](https://bitmask.net/) vise lui à rendre les outils
de chiffrement d'échanges de messages et de VPN simples à utiliser,
encore quelque chose à regarder.

Enfin bref, y'a du taf.
