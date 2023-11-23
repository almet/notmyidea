---
title: Importing a PostgreSQL dump under a different database name
headline: Simple commands to help you during an import
tags: postgresql, sysadmin
---

For [Chariotte](https://chariotte.fr), I've had to do an import from one system to the other. I had no control on the export I received. It contained the database name and the ACLs, which I had to change to match the ones on the new system.

## Decrypting the dump

First off, the import I received was encrypted, so I had to decrypt it. It took me some time to figure out that both my private **and public** keys needed to be imported to the pgp. Once that was done, I could decrypt with

```bash
# Decrypt the file
gpg --decrypt hb_chariotte_prod.pgdump.asc > hb_chariotte_prod.pgdump

# Upload it to the server with scp
scp hb_chariotte_prod.pgdump  chariotte:.
```

## Importing while changing ACLs and database name

On the server, here is the command to change the name of the database and the user. The file I received was using the so-called "custom" format, which is not editable with a simple editor, so you have to export it to SQL first, and then edit it before running the actual queries.

```bash
# Convert to SQL, then replace the table name with the new one, and finally run the SQL statements.
pg_restore -C -f - hb_chariotte_prod.pgdump | sed 's/hb_chariotte_prod/chariotte_temp/g' | psql -U chariotte_temp -d chariotte_temp -h yourhost
```