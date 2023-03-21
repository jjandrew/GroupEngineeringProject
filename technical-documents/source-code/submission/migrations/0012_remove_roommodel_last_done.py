""" Creates the class for removing the data a room model was last done. """
from django.db import migrations


class Migration(migrations.Migration):
    """ Defines the database migration for removing the data a room model was last done.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('submission', '0011_merge_20230321_1051'),
    ]

    operations = [
        # The operation for removing the last_done field for a room model
        migrations.RemoveField(
            model_name='roommodel',
            name='last_done',
        ),
    ]
