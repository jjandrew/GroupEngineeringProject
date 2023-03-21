""" Creates the class for creating merging the two leaderboards together. """
from django.db import migrations


class Migration(migrations.Migration):
    """ Defines the database migration for merging the two leaderboards
    together.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('leaderboard', '0004_buildingmodel_last_done'),
        ('leaderboard', '0004_buildingmodel_number_submissions_and_more'),
    ]

    operations = [
    ]
