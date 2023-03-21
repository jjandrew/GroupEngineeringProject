""" Creates the class for altering when the building was last done."""
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for altering the field containing the
    data the building was last done.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('leaderboard', '0006_alter_buildingmodel_stats_since'),
    ]

    operations = [
        # Operation for altering the last_done date for a building
        migrations.AlterField(
            model_name='buildingmodel',
            name='last_done',
            field=models.DateTimeField(default='2023-01-01 00:00:00 +0000'),
        ),
    ]
