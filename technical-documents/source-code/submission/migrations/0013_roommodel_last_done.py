""" Creates the class for adding the date a room model was last done. """
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for adding a field to store the date a
    room was last done.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('submission', '0012_remove_roommodel_last_done'),
    ]

    operations = [
        # The operation for adding the date a room was last done
        migrations.AddField(
            model_name='roommodel',
            name='last_done',
            field=models.DateTimeField(default='2023-01-01 00:00:00 +0000'),
        ),
    ]
