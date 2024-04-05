---
title: Flash Messenger
save_as: flash/index.html
template: worklog
---

Todo:

- [ ] Ecrire la roadmap quelque part

## Jeudi 28 Mars 2024 (0h, 3h bénévoles, 5/5)

Je reprends le travail du flux d'autentification, pour [le mettre dans un readme](https://gitlab.com/flashmessenger/flashmessenger-server/#authentication-flow) avec un graphique client/serveur.
Je continue d'avancer sur le client en python, en me rendant compte au milieu que les primitives de chiffrement en curves elliptiques "NIST" [ne sont pas considérées sécures](https://safecurves.cr.yp.to/) pour du chiffrement de données.

Je bifurque donc vers l'utilisation de chiffrement symétrique (juste une clé privée) plutôt qu'assimétrique (clé privée + clé publique) pour la partie chiffrement. J'en profite pour regarder un peu ce qu'il se fait en terme de bibliothèques (libsodium, cryptography, [noise](https://noiseprotocol.org/noise.html)) et je réussis à mieux les mettre dans différentes cases. Noise me semble proposer une approche plus haut niveau de comment les primitives de crypto sont utilisées ensemble, dans un protocole qui a du sens du point de vue sécurité, en rendant les vecteurs d'attaque clairs.

J'avance sur le client en python, et je commence à faire l'intégration avec le serveur en rust pour [la vérification des signatures](https://docs.rs/ring/latest/ring/signature/index.html)

## Mercredi 27 Mars 2024 (0h, 9h bénévoles, 4/5)

Le matin on se fait un point avec tout le monde, pour prévoir une roadmap pour le futur, qu'il faudrait retransmettre quelque part.
Je me mets en quête de compiler le serveur rust vers une plateform `x86_64 Linux` depuis une architecture `arm64`. J'apprends au passage comment fonctionne la toolchain de rust.
Le serveur tourne, donc, mais ne veux pas se connecter au redis. Je ne trouve pas pourquoi et je passe à autre chose.

Je passe sur la rédaction d'un client en python qui génère des clés, et qui les utilise pour créer un canal de discussion. C'est à la fois plus dans ma zone de confort de code, mais également sur des problématiques crypto que je ne maitrise pas tout à fait.

Au passage, je jette un coup d'œil au travail en cours de D. qui arrive à cross compiler du rust vers du Java pour Android, en utilisant des JNI et la bibliothèque rust qui va bien.

On se pose aussi avec T. et D. pour réfléchir aux flux d'authentification et de chiffrement des données, parce que je n'arrivais pas à y voir clair seul. Il se trouve qu'il fallait signer les messages avec la clé d'authentification privée, pour pouvoir s'authentifier auprès du serveur pour ce canal.

## Mardi 26 Mars 2024 (0h, 12h bénévoles, 4/5)

Une matinée parler à échanger sur ce qu'on veut faire, et comment on veut se séparer le travail.

L'équipe est naissante, on n'a pas encore l'habitude de travailler ensemble. Je mesure un écart entre les enjeux techniques et les enjeux de simplicité d'utilisation (ça me rappelle [le triangle de Zooko](https://fr.wikipedia.org/wiki/Triangle_de_Zooko)). On se dit qu'avant de partir sur une version plus compliquée, on a envie de creuser aussi sur les aspects techniques.
Je pars sur un prototype de serveur en rust. On s'y mets à plusieurs et on réussis à avoir en fin de soirée un code qui est capable de parler à une base de données redis (ou [redict](https://codeberg.org/redict/redict/)).

J'ai beaucoup aimé un passage ou on était à trois à essayer de faire fonctionner un bout de code rust, en tergiversant et en essayant de comprendre les concepts. C'est vraiment ma manière d'apprendre, en faisant.


