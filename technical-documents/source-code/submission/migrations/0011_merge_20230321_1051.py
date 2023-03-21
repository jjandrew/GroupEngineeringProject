""" Creates the class for merging image submission databases. """
from django.db import migrations


class Migration(migrations.Migration):
    """ Defines the database migration for merging image submission databases.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('submission', '0008_alter_imagesubmission_building_and_more'),
        ('submission', '0010_merge_20230320_1646'),
    ]

    operations = [
    ]
