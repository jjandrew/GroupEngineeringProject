""" Creates the class for creating a leaderboard database. """
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for creating the leaderboard model,
    with columns for ID, player name and the player's score.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """

    initial = True

    dependencies = [
    ]

    operations = [
        # The operation for creating the leaderboard model
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('player_name', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
