Ateliers d'autodéfense numérique
################################

:date: 2016-01-14
:headline: J'ai récemment animé des ateliers d'autodéfense numérique. Voici
           quelques retours et pistes d'améliorations.

Il y a huit mois, je me rendais compte de l'importance du choix des outils pour
faire face à la surveillance généralisée, et notamment en rapport au
chiffrement des données. Une de mes envies de l'époque était l'animation
d'ateliers.

.. epigraph::

    Je compte donc:

    - Organiser des ateliers de sensibilisation aux outils de communication,
      envers mes proches;
    - Utiliser la communication chiffrée le plus souvent possible, au moins
      pour rendre le déchiffrement des messages plus longue, "noyer le
      poisson".

    -- `Chiffrement <http://blog.notmyidea.org/chiffrement.html>`_

J'ai mis un peu de temps à mettre le pied à l'étrier, mais je ressors
finalement du premier atelier que j'ai co-animé avec geb, auprès d'un public de
journalistes.

Pour cette première édition l'idée était à la fois d'aller à la rencontre d'un
public que je connais mal, de leur donner des outils pour solutionner les
problèmes auxquels ils font parfois face, et de me faire une idée de ce que
pouvait être un atelier sur l'autodéfense numérique.

L'objectif pour ce premier atelier était de:

1. Échanger autour des besoins et **faire ressortir des histoires** ou le manque
   d'outillage / connaissances à posé problème, dans des situations concrètes;
2. Se rendre compte des "conduites à risque", **faire peur** aux personnes formées
   pour qu'elles se rendent compte de l'état actuel des choses;
3. **Proposer des solutions concrètes** aux problèmes soulevés, ainsi que le
   minimum de connaissance théorique pour les appréhender.

1. Faire ressortir les problèmes
================================

Afin de faire ressortir les problèmes, nous avons choisi de constituer des
petits groupes de discussion, afin de faire des "Groupes d'Interview Mutuels",
ou "GIM":

.. epigraph::

  l’animateur invite les participants à se regrouper par trois, avec des
  personnes qu’on connaît moins puis invite chacun à livrer une expérience vécue
  en lien avec le thème de la réunion et les deux autres à poser des questions
  leur permettant de bien saisir ce qui a été vécu.

  -- «`Pour s'écouter <http://www.scoplepave.org/pour-s-ecouter>`_», SCOP Le Pavé.

De ces *GIMs* nous avons pu ressortir quelques histoires, gravitant autour de:

- **La protection des sources (d'information)**: Comment faire pour aider
  quelqu'un à faire "fuiter" des données depuis l'intérieur d'une entreprise ?
- **Le chiffrement de ses données**: Comment éviter de faire "fuiter" des données
  importantes lors d'une perquisition de matériel ?

2. Faire peur
=============

Un des premiers objectifs est de faire peur, afin que tout le monde se rende
compte à quel point il est facile d'accéder à certaines données. `Grégoire
<http://blog.barbayellow.com/>`_ m'avait conseillé quelques petites accroches
qui ont ma foi bien marché:

J'ai demandé aux présent.e.s de:

- donner leur mot de passe à voix haute devant les autres: a priori personne ne
  le fera;
- venir se connecter à leur compte email depuis mon ordinateur. J'ai piégé une
  personne, qui est venu pour taper son mot de passe.

Cela à été un bon moyen de parler de l'importance des traces que l'on peut
laisser sur un ordinateur, et de la confiance qu'il faut avoir dans le matériel
que l'on utilise, à fortiori si ce ne sont pas les vôtres.

Pour continuer à leur faire peur, après une brève explication de ce qu'est SSL
nous avons montré comment il était facile de scruter le réseau à la recherche
de mots de passe en clair.

3. Proposer des solutions concrêtes
===================================

Une fois que tout le monde avait pleinement pris sonscience des problématiques
et n'osait plus utiliser son ordinateur ou son téléphone, on à commencé
à parler de quelques solutions.
Plusieurs approches étaient possibles ici, nous avons choisi de présenter
quelques outils qui nous semblaient répondre aux attentes:

- On a expliqué ce qu'était `Tails <https://tails.boum.org>`_, et comment
  l'utiliser et le dupliquer.
- On a pu faire un tour des outils existants sur Tails, notamment autour de
  l'*anonymisation* de fichiers et la suppression effective de contenus.
- Certaines personnes ont pu créer une clé tails avec la persistance de
  configurée.
- Nous nous sommes connectés au réseau `Tor <https://www.torproject.org>`_ et testé
  que nos adresses IP changeaient bien à la demande.
- Nous avons utilisé `CryptoCat <https://crypto.cat>`_ par dessus Tor, afin de
  voir comment avoir une conversation confidentielle dans laquelle il est
  possible d'échanger des fichiers.

Retours
=======

D'une manière générale, pour une formation de trois heures et demi, je suis
assez content de l'exercice, et de l'ensemble des sujets que nous avons pu
couvrir. Il y a beaucoup de place pour l'amélioration, notamment en amont (j'avais
par exemple oublié d'amener avec moi suffisamment de clés USB pour utiliser
Tails).

La plupart des retours qu'on a pu avoir jusqu'à maintenant sont positifs, et il
y a l'envie d'aller plus loin sur l'ensemble de ces sujets.

La suite
========

Il y a beaucoup de sujets que nous n'avons pas abordés, ou uniquement survolés,
à cause du manque de temps disponible. Idéalement, il faudrait au moins une
journée entière pour couvrir quelques sujets plus en détail (on peut imaginer
avoir une partie théorique le matin et une partie pratique l'après-midi par
exemple).

J'ai choisi volontairement de ne pas aborder le chiffrement des messages via
PGP parce que `je pense que la protection que ce média propose n'est pas
suffisante <{filename}/crypto/pgp-problemes.rst>`_, mais je suis en train de
revenir sur ma décision: il pourrait être utile de présenter l'outil, à minima,
en insistant sur certaines de ses faiblesses.

Un compte twitter à été créé recemment autour des crypto-party à Rennes, si
vous êtes interessés, `allez jeter un coup d'œil <https://twitter.com/CryptoPartyRNS>`_!

Je n'ai pas trouvé de ressources disponibles par rapport à des plans de
formation sur le sujet, j'ai donc décidé de publier les nôtres, afin de
co-construire avec d'autres des plans de formation.

Ils sont pour l'instant disponibles `sur Read The Docs
<http://autodefense-numerique.readthedocs.org/en/latest/>`_. Tous les retours 
sont évidemment les bienvenus !
