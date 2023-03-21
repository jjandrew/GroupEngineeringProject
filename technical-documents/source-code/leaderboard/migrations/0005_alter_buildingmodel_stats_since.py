""" Creates the class for altering the building model's stats. """
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for altering the field containing the
    building model's stats since a given date.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('leaderboard', '0004_buildingmodel_last_done'),
    ]

    operations = [
        # Operation for altering the stats since field.
        migrations.AlterField(
            model_name='buildingmodel',
            name='stats_since',
            field=models.DateField(default='2023-03-20'),
        ),
    ]
