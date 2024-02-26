---
title: Changing the primary key of a model in Django
tags: django, orm, migrations
---

I had to change the primary key of a django model, and I wanted to create a
migration for this.

The previous model was using django [automatic primary key fields](https://
docs.djangoproject.com/en/5.0/topics/db/models/#automatic-primary-key-fields)

I firstly changed the model to include the new `uuid` field, and added the `id`
field (the old primary key), like this:

```python

    uuid = models.UUIDField(
        unique=True, primary_key=True, default=uuid.uuid4, editable=False
    )
    id = models.IntegerField(null=True, blank=True)
```

Then I created the migration, it:

- Adds a new `uuid` field/column in the database
- Iterate over the existing items in the table, and generates an uuid for them
- Change the old primary key to a different type
- Drop the old index
- Mark the new uuid as a primary key.

To generate the migrations I did `django-admin makemigrations`, and iterated on
it. Here is the migration I ended up with:

```python
import uuid

from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ("umap", "0017_migrate_to_openstreetmap_oauth2"),
    ]

    operations = [
        # Add the new uuid field
        migrations.AddField(
            model_name="datalayer",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, null=True, serialize=False
            ),
        ),
        # Generate UUIDs for existing records
        migrations.RunSQL("UPDATE umap_datalayer SET uuid = gen_random_uuid()"),
        # Remove the primary key constraint
        migrations.RunSQL("ALTER TABLE umap_datalayer DROP CONSTRAINT umap_datalayer_pk"),
        # Drop the "id" primary key…
        migrations.AlterField(
            "datalayer", name="id", field=models.IntegerField(null=True, blank=True)
        ),
        # … to put it back on the "uuid"
        migrations.AlterField(
            model_name="datalayer",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                unique=True,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
```

## Generating UUIDs in pure python

The uuid generation can also be done with pure python, like this. It works with all databases, but might be slower. Use it with `migrations.RunPython()`.

```python
def gen_uuid(apps, schema_editor):
    DataLayer = apps.get_model("umap", "DataLayer")
    for row in DataLayer.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=["uuid"])
```

## Getting the constraint name

One of the things that took me some time is to have a way to get the constraint name before removing it. I wanted to do this with the Django ORM, but I didn't find how. So here is how in plain SQL. This only works with PostgreSQL, though.

```python
migrations.RunSQL("""
DO $$
BEGIN
    EXECUTE 'ALTER TABLE umap_datalayer DROP CONSTRAINT ' || (
        SELECT indexname
        FROM pg_indexes
        WHERE tablename = 'umap_datalayer' AND indexname LIKE '%pkey'
    );
END $$;
"""),
```
