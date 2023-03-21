""" Creates the class for deleting a leaderboard model. """
from django.db import migrations


class Migration(migrations.Migration):
    """ Defines the database migration for deleting a leaderboard model.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """

    dependencies = [
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        # The operation for deleting the leaderboard
        migrations.DeleteModel(
            name='Leaderboard',
        ),
    ]
