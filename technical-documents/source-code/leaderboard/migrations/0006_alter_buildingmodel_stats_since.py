""" Creates the class for creating a leaderboard database. """
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for creating the leaderboard model,
    with columns for ID, player name and the player's score.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('leaderboard', '0005_merge_20230321_1051'),
    ]

    operations = [
        # Operation for altering the stat's since field
        migrations.AlterField(
            model_name='buildingmodel',
            name='stats_since',
            field=models.DateField(default='2023-03-21'),
        ),
    ]
