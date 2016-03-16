Let's Encrypt + HAProxy
#######################

:date: 2016-02-11
:headline: Comment j'ai mis en place des certificats SSL avec Let's Encrypt
           derrière haproxy.

.. epigraph::

    It’s time for the Web to take a big step forward in terms of security and
    privacy. We want to see HTTPS become the default. Let’s Encrypt was built
    to enable that by making it as easy as possible to get and manage
    certificates.

    -- `Let's Encrypt <https://letsencrypt.org/>`_

Depuis début Décembre, la nouvelle *autorité de certification* Let's Encrypt
est passée en version *Beta*. Les certificats SSL sont un moyen de 1. chiffrer la
communication entre votre navigateur et le serveur et 2. un moyen d'être sur
que le site Web auquel vous accédez est celui auquel vous pensez vous connecter
(pour éviter des `attaques de l'homme du milieu
<https://fr.wikipedia.org/wiki/Attaque_de_l'homme_du_milieu>`_).

Jusqu'à maintenant, il était nécessaire de payer une entreprise pour faire en
sorte d'avoir des certificats qui évitent d'avoir ce genre d'erreurs dans vos
navigateurs:

.. image:: {filename}/static/unsecure-connection.png
    :alt: Message de firefox lorsque une connexion n'est pas sécurisée.

Maintenant, grâce à Let's Encrypt il est possible d'avoir des certificats SSL
**gratuits**, ce qui représente un grand pas en avant pour la sécurité de nos
communications.

Je viens de mettre en place un procédé (assez simple) qui permet de configurer
votre serveur pour générer des certificats SSL valides avec Let's Encrypt et
le répartiteur de charge `HAProxy <http://www.haproxy.org/>`_.

Je me suis basé pour cet article sur d'`autres
<https://blog.infomee.fr/p/letsencrypt-haproxy>`_ `articles
<http://blog.victor-hery.com/article22/utiliser-let-s-encrypt-avec-haproxy>`_, dont je
vous recommande la lecture pour un complément d'information.

Validation des domaines par Let's Encrypt
=========================================

Je vous passe les détails d'installation du client de Let's Encrypt, qui sont
`très bien expliqués sur leur documentation
<https://github.com/letsencrypt/letsencrypt#installation>`_.

Une fois installé, vous allez taper une commande qui va ressembler à::

  letsencrypt-auto certonly --renew-by-default
  --webroot -w /home/www/letsencrypt-requests/ \
  -d hurl.kinto-storage.org \
  -d forums.kinto-storage.org

Le *webroot* est l'endroit ou les preuves de détention du domaine vont être
déposées.

Lorsque les serveurs de Let's Encrypt vont vouloir vérifier que vous êtes bien
à l'origine des demandes de certificats, ils vont envoyer une requête HTTP sur
``http://domaine.org/.well-known/acme-challenge``, ou il voudra trouver des
informations qu'il aura généré via la commande ``letsencrypt-auto``.

J'ai choisi de faire une règle dans haproxy pour diriger toutes les requêtes
avec le chemin ``.well-known/acme-challenge`` vers un *backend* nginx qui sert
des fichiers statiques (ceux contenus dans
``/home/www/letsencrypt-requests/``).

Voici la section de la configuration de HAProxy (et `la configuration
complete
<https://github.com/almet/infra/blob/master/haproxy/haproxy.cfg#L63-L72>`_
si ça peut être utile)::

   frontend http
       bind 0.0.0.0:80
       mode http
       default_backend nginx_server

       acl letsencrypt_check path_beg /.well-known/acme-challenge
       use_backend letsencrypt_backend if letsencrypt_check

       redirect scheme https code 301 if !{ ssl_fc } !letsencrypt_check

   backend letsencrypt_backend
       http-request set-header Host letsencrypt.requests
       dispatch 127.0.0.1:8000

Et celle de NGINX::

   server {
       listen 8000;
       server_name letsencrypt.requests;
       root /home/www/letsencrypt-requests;
   }

Installation des certificats dans HAProxy
=========================================

Vos certificats SSL devraient être générés dans ``/etc/letsencrypt/live``, mais
ils ne sont pas au format attendu par haproxy.  Rien de grave, la commande
suivant convertit l'ensemble des certificats en une version compatible avec
HAProxy::

  cat /etc/letsencrypt/live/domaine.org/privkey.pem /etc/letsencrypt/live/domaine.org/fullchain.pem > /etc/ssl/letsencrypt/domaine.org.pem

Et ensuite dans la configuration de haproxy, pour le (nouveau) *frontend* https::

  bind 0.0.0.0:443 ssl no-sslv3 crt /etc/ssl/letsencrypt

Faites bien attention à avoir un *frontend* `https` pour tous vos sites en HTTPS.
`Pour moi cela ressemble à ça
<https://github.com/almet/infra/blob/master/haproxy/haproxy.cfg#L38-L60>`_.

Une fois tout ceci fait, redémarrez votre service haproxy et zou !

Automatisation
==============

Pour automatiser un peu tout ça, j'ai choisi de faire ça comme suit:

* Un fichier domaine dans ``letsencrypt/domains/domain.org`` qui contient le script ``letsencrypt``.
* Un fichier d'installation de certificats dans
  ``letsencrypt/install-certs.sh`` qui s'occupe d'installer les certificats
  déjà générés.

Et voila ! `Le tout est dans un dépot github
<https://github.com/almet/infra/>`_, si jamais ça peut vous servir, tant mieux !

