Astuces SSH
###########

:date: 27-12-2012

Tunelling
=========

Parce que je m'en rapelle jamais (tête de linote)::

    $ ssh -f hote -L local:lolnet.org:destination -N


.ssh/config
===========

(merci `gaston <http://majerti.fr>`_ !)

La directive suivante dans .ssh/config permet de sauter d'hôte en hôte
séparés par des "+" ::

    Host *+*
            ProxyCommand ssh $(echo %h | sed
    's/+[^+]*$//;s/\([^+%%]*\)%%\([^+]*\)$/\2 -l \1/;s/:/ -p /')
    PATH=.:\$PATH nc -w1 $(echo %h | sed 's/^.*+//;/:/!s/$/ %p/;s/:/ /')

On peut donc spécifier des "sauts" ssh du style::

    ssh root@91.25.25.25+192.168.1.1

Ensuite on peut essayer de rajouter::

    Host <label_pour_mon_serveur_privé>
        user <monuser(root)>
        IdentityFile  <chemin vers ma clé ssh pour le serveur publique>
        hostname ip_serveur_publique+ip_serveur_privé
