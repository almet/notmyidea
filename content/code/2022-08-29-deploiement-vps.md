---
title: Installation de Mosquitto, InfluxDB, Telegraf et Grafana
tags: Administration Système
---

Récemment, on a m'a demandé un petit coup de main pour aider à l'installation d'une pile logicielle qui permet de stocker des données temporelles et en faire des graphiques.

Voici donc quelques notes prises durant l'installation du système, concues pour que des personnes qui n'y connaissent pas grand chose puissent s'y retrouver.

L'objectif, c'est d'avoir des cartes Arduino qui envoient des données de manière régulière sur un système qui va nous permettre de les stocker et d'en faire des graphiques.

Pour ça, nous allons utiliser :

- Un *Broker* [Mosquitto](https://mosquitto.org/) qui va permettre de receptionner les données depuis les différents *clients*, puis de les dispatcher à qui en a besoin ;
- Une base de données [InfluxDB](https://www.influxdata.com/products/influxdb-overview/), qui permet de stocker des données temporelles ;
- Un *agent* [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) qui va prendre les données du broker et les stocker dans la base de données InfluxDB.
- [Grafana](https://grafana.com/), une *application web* qui permet de visualiser les données stockées dans InfluxDB.

Voici donc un document qui résume les étapes que j'ai suivies pour mettre en place les différents élements utiles :

## Installer et se connecter au serveur

Dans notre cas, on est passé par un VPS chez OVH, qui tourne sous [Debian 11](https://www.debian.org/), qui a le mérite d'être une distribution Linux stable, reconnue et (relativement) simple à utiliser.

Dans un terminal, vous pouvez vous connecter en utilisant la ligne de commande suivante :

*Les lignes suivantes sont des lignes d'invite de commande, on les rencontre assez souvent dans les documentations sur le web. Le signe `$` signifie le début de la ligne de commande. Le signe `#` signifie le début des commentaires.*

```bash

$ ssh utilisateur@adresseip
```

Une fois connecté, on va mettre à jour les logiciels qui sont présents sur le serveur. 

```bash

$ sudo apt update # mise à jour des dépôts (la liste des logiciels).
$ sudo apt upgrade # mise à jour des logiciels.
```

## Configurer les DNS

Nous allons avoir besoin de deux sous domaines qui redirigent vers le serveur. Bien sur, il faut adapter `ndd.tld` et le remplacer par votre nom de domaine :

1. moquitto.ndd.tld
1. graphs.ndd.tld

Pour faire ça, chez OVH ça se passe dans la console de « OVH Cloud », direction « Noms de domaines », et puis il faut rajouter deux enregistrements de type « A » qui pointent vers l'adresse IP du serveur.

En temps normal, l'adresse IP vous est fournie par OVH. Si vous avez un doute, vous pouvez l'obtenir depuis le serveur avec la commande `ip a`.

## Installer Mosquitto

```bash
$ sudo apt install mosquitto # installation depuis les dépots officiels
```

Une fois installé, [il faut sécuriser l'installation avec un utilisateur et un mot de passe](https://mosquitto.org/documentation/authentication-methods/).

```bash
$ sudo mosquitto_passwd -c /etc/mosquitto/passwd <username>
```

Ensuite dans le fichier de configuration il faut spécifier où est le fichier qui contient les mots de passe. Pour éditer je recommande l'utilisation de l'éditeur de texte `nano`. 

```bash
$ sudo nano /etc/mosquitto/mosquitto.conf
```

Voici les lignes à rajouter :
```conf
listener 1883
password_file /etc/mosquitto/passwd
```

Puis il faut relancer le service mosquitto :

```bash
$ sudo systemctl restart mosquitto
```

Avant de pouvoir utiliser mosquitto, il faut [régler le firewall](https://docs.ovh.com/gb/en/dedicated/firewall-network/) de chez OVH pour qu'il accepte de laisser passer les messages pour le broker MQTT.

Il faut ajouter une règle dans le Firewall qui laisse passer toutes les connections TCP, avec l'option « établie ».

### Vérifions que tout fonctionne comme prévu :

Dans une console, écoutons…
```bash

$ mosquitto_sub -h mosquitto.ndd.tld -p 1883 -u <username> -P <password> -t topic
```

Et dans une autre envoyons un message :

```bash
$ mosquitto_pub -h mosquitto.ndd.tld -p 1883 -u <username> -P <password> -t topic -m 30
```

Vous deviez voir « 30 » apparaitre dans la première console. Si c'est bon, tout fonctionne !

## Installation d'InfluxDB et Telegraf

Coup de bol, InfluxDB propose directement des packets pour Debian, sur leur dépot, qu'il faut donc ajouter en suivant ces quelques lignes :

```bash
sudo apt install -y gnupg2 curl wget
wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
echo "deb https://repos.influxdata.com/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
sudo apt update
```

Puis ```sudo apt install influxdb telegraf``` pour l'installer.

Ensuite, vous pouvez le lancer maintenant et indiquer au système de le lancer tout seul au démarrage :

```bash
$ sudo systemctl enable --now influxdb
$ sudo systemctl enable --now telegraf
```

### Configuration de Telegraf

Telegraf permet de faire le lien entre les messages envoyés sur le broker MQTT et la base de données InfluxDB.

Ici, il faut rentrer un peu plus dans le vif du sujet, et ça dépends des messages que vous avez à stocker.

Dans notre cas, nous avons trois types de messages :

- /BatVoltage, int
- /Temperature, int
- /GPS, string

Voici un fichier de configuration, qui reste à modifier en fonction des données.

```conf
[global_tags]
[agent]
  interval = "10s"
  round_interval = true
  metric_batch_size = 1000
  metric_buffer_limit = 10000
  collection_jitter = "0s"
  flush_interval = "10s"
  flush_jitter = "0s"
  precision = "0s"
  hostname = ""
  omit_hostname = false

[[outputs.influxdb]]
  urls = ["http://127.0.0.1:8086"]
  database = "telegraf"

[[inputs.mqtt_consumer]]
    servers = ["tcp://127.0.0.1:1883"]
    name_override = "mqtt_consumer_float"
    topics = [
     "Topic/BatVoltage",
     "Topic/Temperature",
    ]
    username = "<username>"
    password = "<password>"
    data_format = "value"
    data_type = "integer"

```

## Installation de Grafana

```bash

sudo apt-get install -y apt-transport-https
sudo apt-get install -y software-properties-common wget
sudo wget -q -O /usr/share/keyrings/grafana.key https://packages.grafana.com/gpg.key
echo "deb [signed-by=/usr/share/keyrings/grafana.key] https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
sudo apt update
sudo apt-get install grafana
sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable grafana-server
sudo /bin/systemctl start grafana-server
```

### Nginx

```
sudo apt install nginx certbot python3-certbot-nginx
```

Puis il faut créer un fichier de configuration dans `/etc/nginx/sites-enabled/graphs.ndd.tld` avec le contenu suivant :

```nginx
map $http_upgrade $connection_upgrade {
  default upgrade;
  '' close;
}

upstream grafana {
  server localhost:3000;
}

server {
  listen 80;
  server_name graphs.ndd.tld;
  root /usr/share/nginx/html;
  index index.html index.htm;

  location / {
    proxy_set_header Host $http_host;
    proxy_pass http://grafana;
  }

  # Proxy Grafana Live WebSocket connections.
  location /api/live/ {
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_set_header Host $http_host;
    proxy_pass http://grafana;
  }
}
```

Une fois ces fichiers de configuration en place, il faut penser à la mise en place du SSL qui permet d'avoir une connexion sécurisée (https).

Il suffit de lancer cette ligne de commande et de suivre les questions posées :

```
sudo certbot --nginx
```

Voilà ! A ce moment là, tout doit être fonctionnel, il ne reste plus qu'à configurer le Grafana pour grapher les données enregistrées dans InfluxDB.