Title: Comment est-ce que vous générez vos formulaires ?
Headline: Présentation d'une solution pour gérer vos formulaires en gardant la main sur les données générées
Category: tech
Image: images/forms.jpg
Image_link: https://www.flickr.com/photos/kurtfaler/2946570890/in/photolist-5unWSo-nxwHk4-fwjQ1b-Xk5F1e-2nyhfK-Wewupi-qRH2Xe-2XeevA-2nyiGe-VoQgbo-2nyh1z-rgyTKm-aPe8yB-9X8MXQ-5zmZi-Vmx4Qu-9X5V9P-5g5EkR-9erwKR-pfUuMZ-obTwRp-dsPpSz-ckgYNh-9X8Zvf-ASZGaH-7LTmLX-fuJpoW-dabtsC-e32SSu-jV9aSa-5vvCn5-9CAB7c-g6y6sK-8N5tB8-87iko3-dsPqmz-4PAkkC-9X67E8-dYGSEz-9X634n-a2GgEA-98kTPP-a6Lpcf-9X5YMk-jcUL1s-7QJYFF-axhDsE-p9vhA8-fA6GmA-5kZtaV
Image_author: Kurt Faler
Image_license: CC BY-NC-ND 2.0

TL; DR: Je viens à peine de *releaser* la première version d'un service de génération de formulaires.
Allez jeter un coup d'œil sur [https://www.fourmilieres.net](https://www.fourmilieres.net)

*En février 2012, je parlais ici [d'un service de génération de formulaires](https://blog.notmyidea.org/carto-forms.html).
Depuis, pas mal d'eau à coulé sous les ponts, on est passé par pas mal d'étapes pour
finalement arriver à une première version de ce service de génération de
formulaires (à la *google forms*).*

En tant qu'organisateurs d'évènements (petits et gros), je me retrouve souvent
dans une situation ou je dois créer des formulaires pour recueillir des
informations. Actuellement, la meilleure solution disponible est *Google Forms*,
mais celle ci à plusieurs problèmes, à commencer par le fait que le code n'est
pas libre et que les données sont stockées chez Google.

La plupart du temps, le besoin est assez simple: je veux spécifier quelques
questions, et donner un lien à mes amis pour qu'ils puissent y répondre.
Je reviens ensuite plus tard pour voir la liste des réponses apportées.

![Capture de l'interface de création du formulaire]({static}/images/formbuilder/formbuilder-build.png)

## Fonctionnalités

Il existe pas mal de solutions techniques qui essayent de répondre à la même
problématique, mais la plupart d'entre elles sont assez souvent compliquées,
nécessitent de se créer un compte, et/ou ne vous laisse pas la main libre sur
les données générées, voire le code est assez difficile à faire évoluer ou à
déployer.

Je voulais donc quelque chose de simple à utiliser *et* pour les créateurs de
formulaires *et* pour les utilisateurs finaux. Pas de chichis, juste quelques
vues, et des URLs à sauvegarder une fois l'opération terminée.

![Capture de l'écran avec les URLs générées]({static}/images/formbuilder/formbuilder-created.png)
![Capture d'écran d'un exemple de formulaire]({static}/images/formbuilder/formbuilder-form.png)

### Pas de compte

Vous n'avez pas besoin d'avoir un compte sur le site pour commencer à l'utiliser.
Vous créez simplement un nouveau formulaire puis envoyez le lien à vos amis pour
qu'eux puissent à leur tour le remplir.

![Capture de la page d'accueil, ou aucun compte n'est requis]({static}/images/formbuilder/formbuilder-welcome.png)

### Gardez la main sur vos données

Une fois que vous avez récupéré les réponses à vos questions, vous pouvez
récupérer les données sur votre machines dans un fichier `.csv`.

![Capture de la page de resultats, il est possible de télécharger en CSV.]({static}/images/formbuilder/formbuilder-results.png)

### API

L'ensemble des données sont en fait stockées dans [Kinto](https://kinto.readthedocs.org)
qui est interrogeable très facilement en HTTP. Ce qui fait qu'il est très facile de
réutiliser les formulaires que vous avez construits (ou leurs réponses) depuis
d'autres outils.

### Auto-hébergeable

Un des objectifs de ce projet est de vous redonner la main sur vos données.
Bien sur, vous pouvez utiliser l'instance qui est mise à votre disposition sur
[wwww.fourmilieres.net](https://www.fourmilieres.net), mais vous pouvez
également l'héberger vous même très
simplement, et vous êtes d'ailleurs fortement encouragés à le faire ! Notre
objectif n'est pas de stocker l'ensemble des formulaires du monde, mais de
(re)donner le contrôle aux utilisateurs !

## On commence petit…

Cette *release* n'est (bien sur) pas parfaite, et il reste encore pas mal de
travail sur cet outil, mais je pense qu'il s'agit d'une base de travail
intéressante pour un futur où Google n'a pas la main sur toutes nos données.

La liste des champs supportés est pour l'instant assez faible (Texte court,
Texte long, Oui/Non, choix dans une liste) mais elle à vocation à s'étendre, en
fonction des besoins de chacun.

J'ai d'ailleurs créé [un formulaire pour que vous puissiez me faire part de vos
retours](https://www.fourmilieres.net/#/form/cfd878264cec4ed2), n'hésitez pas !

## Et, euh, comment ça marche ?

Le *formbuilder*, comme j'aime l'appeler se compose en fin de compte de deux
parties distinctes:

- [Kinto](https://kinto.readthedocs.org), un service qui stocke
  des données coté serveur et qui les expose via des **APIs HTTP**
- [Le formbuilder](https://github.com/kinto/formbuilder), une application
  JavaScript qui ne tourne que coté client (dans votre navigateur) qui permet
  de construire les formulaires et d'envoyer les données sur les *APIs* coté
  serveur.

Au niveau de la *stack* technique, le **formbuilder** est codé en ReactJS. Un
des points techniques intéressants du projet est qu'il génère en fin de compte du
[JSON Schema](http://jsonschema.net/), un format de validation de données *JSON*.

Donc, reprenons! Vous arrivez sur la page d'accueil puis cliquez sur
"Create a new form", puis vous vous retrouvez face à une interface ou vous pouvez
ajouter des champs de formulaire. Une fois ce travail effectué, vous appuyez sur
"Create the form".

- Le JSON Schema est alors envoyé au serveur Kinto, qui l'utilisera pour valider
  les données qu'il recevra par la suite.
- Ce JSON Schema sera aussi utilisé lors de l'affichage du formulaire aux
  personnes qui le remplissent.
- Un jeton d'accès est généré et ajouté à l'URL, il s'agit de l'identifiant du
  formulaire.
- Un second jeton d'accès administrateur et généré, il vous faut le garder de
  coté pour avoir accès aux réponses.

Bref, en espérant que ça vous serve ! Un petit pas dans la direction des données
rendues à leurs utilisateurs !
