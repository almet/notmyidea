# Eco-système et stockage générique

**tl;dr Nous devons construire un service de suivi de paiements, et nous
hésitons à continuer à nous entêter avec notre propre solution de
stockage/synchronisation.**

Comme nous l'écrivions [dans l'article
précédent]({filename}/technologie/2015-04-01-service-de-nuages.rst), nous
souhaitons construire une solution de stockage générique. On refait
[Daybed](http://daybed.readthedocs.org) chez Mozilla \!

Notre objectif est simple: permettre aux développeurs d'application,
internes à Mozilla ou du monde entier, de faire persister et
synchroniser facilement des données associées à un utilisateur.

<div id="storage-specs">

Les aspects de l'architecture qui nous semblent incontournables:

</div>

  - La solution doit reposer sur un protocole, et non sur une
    implémentation ;
  - L'auto-hébergement de l'ensemble doit être simplissime ;
  - L'authentification doit être *pluggable*, voire décentralisée
    (OAuth2, FxA, Persona) ;
  - Les enregistrements doivent pouvoir être validés par le serveur ;
  - Les données doivent pouvoir être stockées dans n'importe quel
    backend ;
  - Un système de permissions doit permettre de protéger des
    collections, ou de partager des enregistrements de manière fine ;
  - La résolution de conflits doit pouvoir avoir lieu sur le serveur ;
  - Le client doit être pensé «\*offline-first\*» ;
  - Le client doit pouvoir réconcilier les données simplement ;
  - Le client doit pouvoir être utilisé aussi bien dans le navigateur
    que côté serveur ;
  - Tous les composants se doivent d´être simples et substituables
    facilement.

La première question qui nous a été posée fût «\*Pourquoi vous
n'utilisez pas PouchDB ou Remote Storage ?\*»

## Remote Storage

Remote Storage est un standard ouvert pour du stockage par utilisateur.
[La
specification](http://tools.ietf.org/html/draft-dejong-remotestorage-04)
se base sur des standards déjà existants et éprouvés: Webfinger, OAuth
2, CORS et REST.

L'API est simple, des [projets prestigieux
l'utilisent](http://blog.cozycloud.cc/news/2014/08/12/when-unhosted-meets-cozy-cloud/).
Il y a plusieurs [implémentations](https://github.com/jcoglan/restore)
du serveur, et il existe [un squelette
Node](https://www.npmjs.com/package/remotestorage-server) pour
construire un serveur sur mesure.

![Remote Storage widget](%7Bfilename%7D/images/remotestorage-widget.png)

Le client
[remoteStorage.js](https://github.com/remotestorage/remotestorage.js/)
permet d'intégrer la solution dans les applications Web. Il se charge du
«store local», du cache, de la synchronization, et fournit un widget qui
permet aux utilisateurs des applications de choisir le serveur qui
recevra les données (via Webfinger).

[ludbud](https://github.com/michielbdejong/ludbud), la version épurée de
*remoteStorage.js*, se limite à l'abstraction du stockage distant. Cela
permettrait à terme, d'avoir une seule bibliothèque pour stocker dans un
serveur *remoteStorage*, *ownCloud* ou chez les méchants comme *Google
Drive* ou *Dropbox*.

Au premier abord, la spécification correspond à ce que nous voulons
accomplir:

  - La philosophie du protocole est saine;
  - L'éco-système est bien fichu;
  - La vision politique colle: redonner le contrôle des données aux
    utilisateurs (voir [unhosted](http://unhosted.org/));
  - Les choix techniques compatibles avec ce qu'on a commencé (CORS,
    REST, OAuth 2);

En revanche, vis à vis de la manipulation des données, il y a plusieurs
différences avec ce que nous souhaitons faire:

  - L'API suit globalement une métaphore «fichiers» (dossier/documents),
    plutôt que «données» (collection/enregistrements) ;
  - Il n'y a pas de validation des enregistrements selon un schéma (même
    si [certaines
    implémentations](https://remotestorage.io/doc/code/files/baseclient/types-js.html)
    du protocole le font) ;
  - Il n'y a pas la possibilité de trier/filtrer les enregistrements
    selon des attributs ;
  - Les permissions [se limitent à
    privé/public](https://groups.google.com/forum/#!topic/unhosted/5_NOGq8BPTo)
    (et [l'auteur envisage plutôt un modèle à la
    Git](https://github.com/remotestorage/spec/issues/58#issue-27249452))\[1\]
    ;

En résumé, il semblerait que ce que nous souhaitons faire avec le
stockage d'enregistrements validés est complémentaire avec *Remote
Storage*.

Si des besoins de persistence orientés «fichiers» se présentent, a
priori nous aurions tort de réinventer les solutions apportées par cette
spécification. Il y a donc de grandes chances que nous l´intégrions à
terme, et que *Remote Storage* devienne une facette de notre solution.

## PouchDB

[PouchDB](http://pouchdb.com/) est une bibliothèque JavaScript qui
permet de manipuler des enregistrements en local et de les synchroniser
vers une base distante.

``` 
javascript
var db = new PouchDB('dbname');

db.put({
 _id: 'dave@gmail.com',
 name: 'David',
 age: 68
});

db.replicate.to('http://example.com/mydb');
```

Le projet a le vent en poupe, bénéficie de nombreux contributeurs,
l'éco-système est très riche et l'adoption par des projets [comme
Hoodie](https://github.com/hoodiehq/wip-hoodie-store-on-pouchdb) ne fait
que confirmer la pertinence de l'outil pour les développeurs frontend.

*PouchDB* gère un « store » local, dont la persistence est abstraite et
[repose sur](http://pouchdb.com/2014/07/25/pouchdb-levels-up.html) l'API
[LevelDown](https://github.com/level/levelup#relationship-to-leveldown)
pour persister les données dans [n'importe quel
backend](https://github.com/Level/levelup/wiki/Modules#storage-back-ends).

Même si *PouchDB* adresse principalement les besoins des applications
«\*offline-first\*», il peut être utilisé aussi bien dans le navigateur
que côté serveur, via Node.

### Synchronisation

La synchronisation (ou réplication) des données locales s'effectue sur
un [CouchDB](http://couchdb.apache.org/) distant.

Le projet [PouchDB Server](https://github.com/pouchdb/pouchdb-server)
implémente l'API de CouchDB en NodeJS. Comme *PouchDB* est utilisé, on
obtient un service qui se comporte comme un *CouchDB* mais qui stocke
ses données n'importe où, dans un *Redis* ou un *PostgreSQL* par
exemple.

La synchronisation est complète. Autrement dit, tous les enregistrements
qui sont sur le serveur se retrouvent synchronisés dans le client. Il
est possible de filtrer les collections synchronisées, mais cela [n'a
pas pour objectif de sécuriser l'accès aux
données](http://pouchdb.com/2015/04/05/filtered-replication.html).

L'approche recommandée pour cloisonner les données par utilisateur
consiste à créer [une base de données par
utilisateur](https://github.com/nolanlawson/pouchdb-authentication#some-people-can-read-some-docs-some-people-can-write-those-same-docs).

Ce n'est pas forcément un problème, CouchDB [supporte des centaines de
milliers de bases sans
sourciller](https://mail-archives.apache.org/mod_mbox/couchdb-user/201401.mbox/%3C52CEB873.7080404@ironicdesign.com%3E).
Mais selon les cas d'utilisation, le cloisement n'est pas toujours
facile à déterminer (par rôle, par application, par collection, ...).

## Le cas d'utilisation « Payments »

![Put Payments Here -- Before the Internet - CC-NC-SA Katy Silberger
https://www.flickr.com/photos/katysilbs/11163812186](%7Bfilename%7D/images/put-payments.jpg)

Dans les prochaines semaines, nous devrons mettre sur pied un prototype
pour tracer l'historique des paiements et abonnements d'un utilisateur.

Le besoin est simple:

  - l'application « Payment » enregistre les paiements et abonnements
    d'un utilisateur pour une application donnée;
  - l'application « Donnée » interroge le service pour vérifier qu'un
    utilisateur a payé ou est abonné;
  - l'utilisateur interroge le service pour obtenir la liste de tous ses
    abonnements.

Seule l'application « Payment » a le droit de créer/modifier/supprimer
des enregistrements, les deux autres ne peuvent que consulter en lecture
seule.

Une application donnée ne peut pas accéder aux paiements des autres
applications, et un utilisateur ne peut pas accéder aux paiements des
autres utilisateurs.

### Avec RemoteStorage

![Remote Love - CC-BY-NC Julie
https://www.flickr.com/photos/mamajulie2008/2609549461](%7Bfilename%7D/images/remote-love.jpg)

Clairement, l'idée de *RemoteStorage* est de dissocier l'application
executée, et les données créées par l'utilisateur avec celle-ci.

Dans notre cas, c'est l'application « Payment » qui manipule des données
concernant un utilisateur. Mais celles-ci ne lui appartiennent pas
directement: certes un utilisateur doit pouvoir les supprimer, surtout
pas en créer ou les modifier\!

La notion de permissions limitée à privé/publique ne suffit pas dans ce
cas précis.

### Avec PouchDB

Il va falloir créer une *base de données* par utilisateur, afin d'isoler
les enregistrements de façon sécurisée. Seule l'application « Payment »
aura tous les droits sur les databases.

Mais cela ne suffit pas.

Il ne faut pas qu'une application puisse voir les paiements des autres
applications, donc il va aussi falloir recloisonner, et créer une *base
de données* par application.

Quand un utilisateur voudra accéder à l'ensemble de ses paiements, il
faudra agréger les *databases* de toutes les applications. Quand
l'équipe marketing voudra faire des statistiques sur l'ensemble des
applications, il faudra agrégér des centaines de milliers de
*databases*.

Ce qui est fort dommage, puisqu'il est probable que les paiements ou
abonnements d'un utilisateur pour une application se comptent sur les
doigts d'une main. Des centaines de milliers de bases contenant moins de
5 enregistrements ?

De plus, dans le cas de l'application « Payment », le serveur est
implémenté en Python. Utiliser un wrapper JavaScript comme le fait
[python-pouchdb](https://pythonhosted.org/Python-PouchDB/) cela ne nous
fait pas trop rêver.

## Un nouvel éco-système ?

![Wagon wheel - CC-BY-NC-SA arbyreed
https://www.flickr.com/photos/19779889@N00/16161808220](%7Bfilename%7D/images/wagon-wheel.jpg)

Évidemment, quand on voit la richesse des projets *PouchDB* et *Remote
Storage* et la dynamique de ces communautés, il est légitime d'hésiter
avant de développer une solution alternative.

Quand nous avons créé le serveur *Reading List*, nous l'avons construit
avec [Cliquet](http://cliquet.readthedocs.org/), ce fût l'occasion de
mettre au point [un protocole très
simple](http://cliquet.readthedocs.org/en/latest/api/), fortement
inspiré de [Firefox Sync](http://en.wikipedia.org/wiki/Firefox_Sync),
pour faire de la synchronisation d'enregistrements.

Et si les clients *Reading List* ont pu être implémentés en quelques
semaines, que ce soit en JavaScript, Java (Android) et ASM (Add-on
Firefox), c'est que le principe «\*offline first\*» du service est
trivial.

### Les compromis

Évidemment, nous n'avons pas la prétention de concurrencer *CouchDB*.
Nous faisons plusieurs concessions:

  - De base, les collections d'enregistrements sont cloisonnées par
    utilisateur;
  - Pas d'historique des révisions;
  - Pas de diff sur les enregistrements entre révisions;
  - De base, pas de résolution de conflit automatique;
  - Pas de synchronisation par flux (*streams*);

Jusqu'à preuve du contraire, ces compromis excluent la possibilité
d'implémenter un [adapter
PouchDB](https://github.com/pouchdb/pouchdb/blob/master/lib/adapters/http/http.js#L721-L946)
pour la synchronisation avec le protocole HTTP de *Cliquet*.

Dommage puisque capitaliser sur l'expérience client de *PouchDB* au
niveau synchro client semble être une très bonne idée.

En revanche, nous avons plusieurs fonctionnalités intéressantes:

  - Pas de map-reduce;
  - Synchronisation partielle et/ou ordonnée et/ou paginée ;
  - Le client choisit, via des headers, d'écraser la donnée ou de
    respecter la version du serveur ;
  - Un seul serveur à déployer pour N applications ;
  - Auto-hébergement simplissime ;
  - Le client peut choisir de ne pas utiliser de « store local » du tout
    ;
  - Dans le client JS, la gestion du « store local » sera externalisée
    (on pense à [LocalForage](https://github.com/mozilla/localForage) ou
    [Dexie.js](https://github.com/dfahlander/Dexie.js)) ;

Et, on répond au reste des [specifications mentionnées au début de
l'article](#storage-specs) \!

### Les arguments philosophiques

Il est [illusoire de penser qu'on peut tout faire avec un seul
outil](http://en.wikipedia.org/wiki/Law_of_the_instrument).

Nous avons d'autres cas d'utilisations dans les cartons qui semblent
correspondre au scope de *PouchDB* (*pas de notion de permissions ou de
partage, environnement JavaScript, ...*). Nous saurons en tirer profit
quand cela s'avèrera pertinent \!

L'éco-système que nous voulons construire tentera de couvrir les cas
d'utilisation qui sont mal adressés par *PouchDB*. Il se voudra:

  - Basé sur notre protocole très simple ;
  - Minimaliste et multi-usages (*comme la fameuse 2CV*) ;
  - Naïf (*pas de rocket science*) ;
  - Sans magie (*explicite et facile à réimplémenter from scratch*) ;

[La philosophie et les fonctionnalités du toolkit python
Cliquet](http://cliquet.readthedocs.org/en/latest/rationale.html) seront
bien entendu à l'honneur :)

Quant à *Remote Storage*, dès que le besoin se présentera, nous serons
très fier de rejoindre l'initiative, mais pour l'instant cela nous
paraît risqué de démarrer en tordant la solution.

### Les arguments pratiques

Avant d'accepter de déployer une solution à base de *CouchDB*, les *ops*
de Mozilla vont nous demander de leur prouver par A+B que ce n'est pas
faisable avec les stacks qui sont déjà rodées en interne (i.e. MySQL,
Redis, PostgreSQL).

De plus, on doit s'engager sur une pérennité d'au moins 5 ans pour les
données. Avec *Cliquet*, en utilisant le backend PostgreSQL, les données
sont persistées à plat dans un [schéma PostgreSQL tout
bête](https://github.com/mozilla-services/cliquet/blob/40aa33/cliquet/storage/postgresql/schema.sql#L14-L28).
Ce qui ne sera pas le cas d'un adapteur LevelDown qui va manipuler des
notions de révisions éclatées dans un schéma clé-valeur.

Si nous basons le service sur *Cliquet*, comme c'est le cas avec
[Kinto](http://kinto.readthedocs.org), tout le travail d'automatisation
de la mise en production (*monitoring, builds RPM, Puppet...*) que nous
avons fait pour *Reading List* est complètement réutilisable.

De même, si on repart avec une stack complètement différente, nous
allons devoir recommencer tout le travail de rodage, de profiling et
d'optimisation effectué au premier trimestre.

## Les prochaines étapes

Et il est encore temps de changer de stratégie :) Nous aimerions avoir
un maximum de retours \! C'est toujours une décision difficile à
prendre... `</appel à troll>`

  - Tordre un éco-système existant vs. constuire sur mesure ;
  - Maîtriser l'ensemble vs. s'intégrer ;
  - Contribuer vs. refaire ;
  - Guider vs. suivre.

Nous avons vraiment l'intention de rejoindre l'initiative
[no-backend](https://nobackend.org/), et ce premier pas n'exclue pas que
nous convergions à terme \! Peut-être que nous allons finir par rendre
notre service compatible avec *Remote Storage*, et peut-être que
*PouchDB* deviendra plus agnostique quand au protocole de
synchronisation...

![XKCD — Standards
https://xkcd.com/927/](%7Bfilename%7D/images/standards.png)

Utiliser ce nouvel écosystème pour le projet « Payments » va nous
permettre de mettre au point un système de permissions (*probablement
basé sur les scopes OAuth*) qui correspond au besoin exprimé. Et nous
avons bien l'intention de puiser dans [notre expérience avec Daybed sur
le sujet](http://blog.daybed.io/daybed-revival.html).

Nous extrairons aussi le code des clients implémentés pour *Reading
List* afin de faire un client JavaScript minimaliste.

En partant dans notre coin, nous prenons plusieurs risques:

  - réinventer une roue dont nous n'avons pas connaissance ;
  - échouer à faire de l'éco-système *Cliquet* un projet communautaire ;
  - échouer à positionner *Cliquet* dans la niche des cas non couverts
    par PouchDB :)

Comme [le dit Giovanni
Ornaghi](http://pouchdb.com/2015/04/05/filtered-replication.html):

> Rolling out your set of webservices, push notifications, or background
> services might give you more control, but at the same time it will
> force you to engineer, write, test, and maintain a whole new
> ecosystem.

C'est justement l'éco-système dont est responsable l'équipe *Mozilla
Cloud Services*\!

1.  Il existe le [projet Sharesome](https://sharesome.5apps.com/) qui
    permet de partager publiquement des ressources de son *remote
    Storage*.
