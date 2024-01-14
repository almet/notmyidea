---
title: Chariotte
save_as: chariotte/index.html
template: worklog
---
## Dimanche 17 Décembre 2023 (0h, 8h bénévoles, 4/5)

J'ai passé beaucoup de temps pour essayer de comprendre pourquoi les emails n'étaient pas envoyés lors de la récupération de mot de passe. J'ai fini par trouver en utilisant un bon vieux debugger, comme quoi c'est la solution à privilégier autant que possible.

Le code actuel utilise `username` comme un champ de stockage d'emails, et Django avait du mal à retrouver ses petits (il cherchait dans le champ `email` sans succès). J'ai fini par trouver la solution. Je suis content de réussir à remonter en compétences sur le debug de django, même si je pensais que ça me prendrais moins de temps :-)

J'ai aussi mis en place de la documentation.

## Lundi 27 Novembre 2023 (0h, 4h bénévoles, 3/5)

Chariotte.fr est maintenant hébergé par Alwaysdata !
Arthur m'a envoyé les données puis j'ai fait la commande suivante :

```bash
gpg --decrypt hb_chariotte_prod.pgdump.asc > hb_chariotte_prod.pgdump
scp hb_chariotte_prod.pgdump  chariotte:..
pg_restore -C -f - hb_chariotte_prod.pgdump | sed 's/hb_chariotte_prod/chariotte_prod/g' | psql -U chariotte_prod -d chariotte_prod -h postgresql-chariotte.alwaysdata.net
```

Le soir, j'ai tenté de comprendre pourquoi les mails ne sont pas envoyés. Sans trop réussir malheureusement.
