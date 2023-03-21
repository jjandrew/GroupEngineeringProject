""" Creates the class for adding a field to track the last time a building was
done
"""
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for adding a field to track the last
    time the building was done.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('leaderboard', '0003_initial'),
    ]

    operations = [
        # Operations for adding the data the building was last done
        migrations.AddField(
            model_name='buildingmodel',
            name='last_done',
            field=models.DateTimeField(default='2023-01-01 00:00:00 +0000'),
        ),
    ]
