""" Creates the class for altering the room model for image submission fields.
"""
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for altering the room model of an image
    submission.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('submission', '0008_roommodel_last_done'),
    ]

    operations = [
        # Operation for adding a room model field to the submission model
        migrations.AlterField(
            model_name='roommodel',
            name='last_done',
            field=models.DateTimeField(default='2023-01-01 00:00:00'),
        ),
    ]
