""" Creates the class for adding a date to image submissions """
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for adding an a date to the image
    submission.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('submission', '0004_imagesubmission_user'),
    ]

    operations = [
        # Adds the date field to the image submission
        migrations.AddField(
            model_name='imagesubmission',
            name='date',
            field=models.DateField(default='2023-01-01'),
            preserve_default=False,
        ),
    ]
