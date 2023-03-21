""" Creates the class for removing image submission fields. """
from django.db import migrations


class Migration(migrations.Migration):
    """ Defines the database migration for removing the number of lights,
    windows, plugs and the plugs on from the image submission model.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('submission',
         '0006_remove_imagesubmission_number_lights_on_and_more'),
    ]

    operations = [
        # The operations for removing each of the relevant fields
        # from the image submission model
        migrations.RemoveField(
            model_name='roommodel',
            name='number_of_lights',
        ),
        migrations.RemoveField(
            model_name='roommodel',
            name='number_of_windows',
        ),
        migrations.RemoveField(
            model_name='roommodel',
            name='number_plugs',
        ),
        migrations.RemoveField(
            model_name='roommodel',
            name='number_plugs_on',
        ),
    ]
