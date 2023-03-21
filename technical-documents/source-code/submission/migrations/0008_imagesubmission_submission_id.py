""" Creates the class for adding image submission fields. """
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for adding a submission id to an
    image submission.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('submission', '0007_remove_roommodel_number_of_lights_and_more'),
    ]

    operations = [
        # The operation for adding the submission ID field to the
        # submission model
        migrations.AddField(
            model_name='imagesubmission',
            name='submission_id',
            field=models.IntegerField(default=0),
        ),
    ]
