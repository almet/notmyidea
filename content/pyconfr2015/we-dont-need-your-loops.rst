PyconFR 2015 — We don't need your loop
######################################

:date: 2015.10.18
:category: pyconfr2015
:unlisted: true

.. note::

  Voici quelques notes prises durant la PyconFR 2015, à Pau. N'hésitez pas
  à les completer si besoin.

Speaker: serge_sans_paille.

Retour sur le passé des boucles: ASM, fortran, C. Avec APL, la boucle est
cachée au fur et à mesure des évolutions. Écrire une boucle ne devrait pas etre
exprimer comment atteindre le resultat.

En python, par exemple, il vaut mieux utiliser `sum` plutôt que de faire
l'addition nous même (pour faire une addition des elements d'une liste).

Actuellement, le compilateur python est lent si on utilise numpy.sum sur des
matrices complexes.

Comment aller plus vite?
========================

Cython est assez compliqué, il faut savoir ce que l'on fait pour optimiser et
écrire du bon code Cython. 

Avec pythran, l'intelligence est dans le compilateur, qui permet d'écrire
notemment des boucles correctement.

En donnant plus d'informaitons au compilateur, plutôt que de faire des boucles,
cela lui permet d'avoir un contexte qui lui permet d'optimiser le code.

Par contre, cela veut dire que plus de connaissances sont necessaire pour lire
le code python.

pythran permet de compiler directement vers du C++ sans avoir à changer son
code de base (python). C'est utile pour du code numpy notemment.

Questions
=========

Possible de paralelliser de manière explicite **ou** implicite.

**C'est très utile pour les gens qui font du "number crunching". Est-ce que
c'est utile pour d'autres domaines d'application (Web)?**

Pas vraiment. CPython est déjà bien fait pour ces cas d'utilisation.

**Est-il possible de lancer pythran sans faire de commentaires ?**

C'est possible mais cela ne servira pas à grand chose. Il est necessaire de
connaitre le type des objets qui sont utilisés lors des boucles.

**Est-ce que vous songez à un compilateur à la volée ?**

De gros efforts ont été faits dernièrement pour diminuer le temps de
compilation. Mais pour une fonction qui renvoie None prends de l'ordre d'une
seconde ou une demi seconde. Ce n'est pas très utile pour un compilateur à la
volée puisqu'il faudrait des gains de perfs supérieurs à cela.
