""" Creates the class for tracking the number of buidling submissions and the
building's stats since the last submission
"""
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for adding a field to track the number
    of times a building has been submitted along with altering it's stats
    since it's last submission.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('leaderboard', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingmodel',
            name='number_submissions',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='buildingmodel',
            name='stats_since',
            field=models.DateField(default='2023-03-20'),
        ),
    ]
