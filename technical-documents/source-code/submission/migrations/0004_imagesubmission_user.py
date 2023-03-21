""" Creates the class for allowing for image submission migrations """
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for adding an image submission field
    to the submission app.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('submission', '0003_remove_imagesubmission_lights_and_more'),
    ]

    operations = [
        # Adds the field for image submission
        migrations.AddField(
            model_name='imagesubmission',
            name='user',
            field=models.CharField(default='invalidUser', max_length=100),
            preserve_default=False,
        ),
    ]
