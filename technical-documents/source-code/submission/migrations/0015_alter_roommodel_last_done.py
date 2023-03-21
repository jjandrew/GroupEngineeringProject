""" Creates the class for altering the date a room was last done. """
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for altering the last_done date for a
    building on the leaderboard.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('submission', '0014_alter_roommodel_last_done'),
    ]

    operations = [
        # The operation for altering the field.
        migrations.AlterField(
            model_name='roommodel',
            name='last_done',
            field=models.DateTimeField(default='2023-01-01 00:00:00 +0000'),
        ),
    ]
