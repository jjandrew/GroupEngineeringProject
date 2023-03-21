""" Creates the class for merging migrations. """
from django.db import migrations


class Migration(migrations.Migration):
    """ Defines the database operation for merging migrations

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('submission', '0009_alter_roommodel_last_done'),
        ('submission', '0009_remove_imagesubmission_submission_id'),
    ]

    operations = [
    ]
