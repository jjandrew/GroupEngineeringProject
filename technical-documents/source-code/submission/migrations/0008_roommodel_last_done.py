""" Creates the class for adding image submission fields. """
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for adding a room model  to an
    image submission.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('submission', '0007_remove_roommodel_number_of_lights_and_more'),
    ]

    operations = [
        # Operation for adding a room model field to the submission model
        migrations.AddField(
            model_name='roommodel',
            name='last_done',
            field=models.DateTimeField(default='2023-01-01 00:00:00 +0000'),
            preserve_default=False,
        ),
    ]
