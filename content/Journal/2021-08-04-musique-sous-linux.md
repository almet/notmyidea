# Faire de la musique sous Linux

*Update du 07/08 : ajout des infos sur le noyau temps réel*

Faire de la musique electronique à été pour moi l'occasion de réinstaller Windows pour pouvoir utiliser [Ableton Live](https://www.ableton.com/en/live/), un des logiciels les plus utilisés dans le domaine. J'étais content de passer du temps à faire de la musique plutôt que du temps à faire tomber les choses en marche, même si mon éthique n'était pas tout à fait d'accord.

C'est un choix que je ne regrette pas : je me suis vraiment amusé, j'ai [fait quelques morceaux](https://soundcloud.com/the-lost-triangle/) et j'ai pu goûter au plaisir du truc. Un des avantages d'apprendre en utilisant des outils *mainstrem*, c'est qu'il y a beaucoup de ressources disponibles (tutoriels vidéo, ami⋅es), ce qui m'a beaucoup facilité la tache dans la découverte du domaine.

Et puis, [Yohan](https://yohanboniface.me/) m'a parlé de [Bitwig](https://www.bitwig.com/), un logiciel de type « Digital Audio Workstation » (DAW) qui tourne nativement sous Linux, et après une petite scéance de test j'ai eu envie de creuser un peu le sujet de l'audio sous Linux.

L'occasion donc d'installer une station musicale sous Linux (j'utilise [Arch Linux](https://archlinux.org/)). Ça marche plutôt bien, ce n'est pas trop long à mettre en place (une fois qu'on sait quoi faire), même si ça reste moins simple que sous Windows. Je suis très content du résultat !

## Configuration

Installer Arch n'est pas très compliqué, mais passe par de la ligne de commande, c'était l'occasion de réviser un peu mes classiques, mais je peux comprendre que ce soit intimidant. Si vous voulez avoir un installeur graphique, il me semble que [Manjaro](https://manjaro.org/) (un dérivé d'Arch) en propose un.

### Configuration du noyau Linux

Ça me paraissait compliqué, et pourtant c'était très simple ! J'ai utilisé le noyau « linux-zen » avec quelques options spécifiques « threadirqs » et le mode « performance » pour les processeurs.

J'ai du installer un paquet logiciel pour avoir des privilèges « temps réel » indispensable pour l'audio : sans ça le plugin VST « Kontakt » plantait directement au lancement.

```bash
sudo pacman -S realtime-privileges
sudo gpasswd -a "$USER" realtime
```

```bash
yay linux-zen
yay rtirq
```

Édition de `/etc/default/grub` pour utiliser threadirqs et passer le scheduling du processeur en « performance ».

```bash
GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet threadirqs cpufreq.default_governor=performance"
```

```bash
# Regénérer la configuration de grub
grub-mkconfig -o /boot/grub/grub.cfg

# S'assurer que « fsync » soit bien utilisé par wine.
echo "export WINEFSYNC=1" >> ~/.profile

# Ajout au groupe audio
sudo gpasswd -a "$USER" realtime
```

Le DAW [Bitwig](https://www.bitwig.com/) que j'utilise n'est pas open source, mais tourne nativement sous Linux. Son installation sous Arch est vraiment on ne peut plus simple : `yay bitwig-studio`.

## VSTs (Instruments virtuels)

J'ai acheté quelques VST qui tournent nativement sous Linux mais également d'autres qui n'ont pas de version Linux native. C'est par exemple le cas de Kontakt.

Dans ce cas, il faut passer par le pont logiciel [yabridge](https://github.com/robbert-vdh/yabridge) ainsi qu'une version récente de wine : [wine-tkg](https://github.com/Frogging-Family/wine-tkg-git/releases/).

Pour installer yabridge, `yay yabridge-bin`.

Installation de wine-tkg :

```bash
wget https://github.com/Frogging-Family/wine-tkg-git/releases/download/6.11.r4.g0dd44a25/wine-tkg-staging-fsync-git-6.11.r4.g0dd44a25-326-x86_64.pkg.tar.zst
sudo pacman -U wine-tkg-staging-fsync-git-6.11.r4.g0dd44a25-326-x86_64.pkg.tar.zst
```

### Installation d'un VST (Kontakt)

Ensuite, installez le VST dans wine :

```bash
wine Kontakt\ 6.3.0\ Setup\ PC.exe
cd patch
wine Kontakt\_patch\_installer\_6\_3_0.exe
```

Spécifiez l'emplacement pour les VST64 : `C:\Program Files\Steinberg\VstPlugins` (emplacement souvent utilisé pour les VST2), je ne sais pas pour quelle raison mais utiliser un emplacement classique peut résoudre des bugs.

Une fois installé, vous pouvez ajouter le fichier qui contient vos VSTs dans yabridge :

```bash
yabridgectl add "/home/alexis/.wine/drive_c/Program Files/Steinberg/VstPlugins"
```
Puis faire `yabridgectl sync` qui va générer les .`so` (format Linux) à partir des `.dll` (format Windows).

Il ne reste plus qu'à ajouter le dossier qui contient les VST dans Bitwig et c'est bon !

J'utilise sans soucis ces instruments Kontakt :

- Una Corda (Piano)
- Studio Drummer (Batterie)

![bitwig-studio-studio-drummer.png](/images/musique-linux.png)

## Carte son

J'utilise une carte son Scarlett 18i8 gen3, qui fonctionne nativement pour sortir de l'audio et pour en capturer. Par contre certains controles ne sont pas exposés, et le logiciel de contrôle / configuration ne tourne pas sous wine.

Mais… (coup de bol ?) quelqu'un s'est motivé [pour écrire le code noyau](https://github.com/geoffreybennett/scarlett-gen2) qui permet de faire ça nativement. Ça vient d'être mergé dans le noyau Linux, et devrait être disponible avec le kernel 5.14, qui devrait bientôt voir le jour (c'est la RC3 au moment ou j'écris ces lignes).

## Controleurs

J'utilise un [Novation Launchkey mini mk3](https://novationmusic.com/en/keys/launchkey-mini) avec les mappings proposés par [DrivenByMoss](http://mossgrabers.de/Software/Bitwig/Bitwig.html) qui permettent de controller nativement Bitwig, c'est assez bluffant, ça marche tout seul !

Installation :

1.  Télécharger l'archive qui contient le code depuis le site web
2.  Extraire le fichier .bwextension dans `~/Bitwig Studio/Extensions`

Il semble aussi que [Push 2 pour Bitwig sous Linux](http://www.mossgrabers.de/Software/Bitwig/Bitwig.html) soit une option interessante (mais bien plus couteuse) !

## VST natif Linux

Il existe un tas de VST open source qui font très bien le taf. J'aime beaucoup toute la collection de VST sans interface graphique (et open source !) qui est proposée par airwindows, (installables avec `yay aur/airwindows-git`)

J'utilise quelques VST payants également. Ceux que j'utilise actuellement, et qui sont compatibles Linux :

- Les instruments de chez [TAL](https://tal-software.com/). J'utilise [TAL-Mod](https://tal-software.com/products/tal-mod) pour faire des bonnes grosses basses
- Ceux de chez [U-he](https://u-he.com/products/). J'utilise [Bazille](https://u-he.com/products/bazille/), un Synthé modulaire polyphonique avec des oscillateurs numériques et de la FM)

Une grosse liste est présente sur [Linux Sound](http://linux-sound.org/linux-vst-plugins.html) si vous voulez creuser :-)

## Configuration pour du temps réel

Edititon du 7/08 : j'ai pu jouer un peu depuis, et je me suis rendu compte que j'avais quelques glitches audio quand j'utilisais wine. J'ai donc fait quelques changements supplémentaires.

Ressources :

- [Le wiki de yabridge sur le tuning perfomance](https://github.com/robbert-vdh/yabridge#performance-tuning)
- [Un outil pour faire un scan des problèmes de perf connus](https://github.com/raboof/realtimeconfigquickscan)
