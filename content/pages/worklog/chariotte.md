---
title: Argos
save_as: argos/index.html
template: worklog
---

## 27 Novembre 2023 (0h, 2h bénévoles, 4/5)

Chariotte.fr est maintenant hébergé par Alwaysdata !
Arthur m'a envoyé les données puis j'ai fait la commande suivante :

```bash
gpg --decrypt hb_chariotte_prod.pgdump.asc > hb_chariotte_prod.pgdump
scp hb_chariotte_prod.pgdump  chariotte:..
pg_restore -C -f - hb_chariotte_prod.pgdump | sed 's/hb_chariotte_prod/chariotte_prod/g' | psql -U chariotte_prod -d chariotte_prod -h postgresql-chariotte.alwaysdata.net
```