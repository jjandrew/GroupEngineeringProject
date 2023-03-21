""" Creates the class for removing an image submission. """
from django.db import migrations


class Migration(migrations.Migration):
    """ Defines the database migration for removing an image submission

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('submission', '0008_imagesubmission_submission_id'),
    ]

    operations = [
        # The operation for removing an image submission
        migrations.RemoveField(
            model_name='imagesubmission',
            name='submission_id',
        ),
    ]
