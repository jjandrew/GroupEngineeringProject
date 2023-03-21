""" Creates the class for removing and altering submission fields. """
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for removing and altering each of the
    fields in the image submission model.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('submission', '0005_imagesubmission_date'),
    ]
    # Outlines the migrations for altering, removing and adding each of
    # the fields for the image submission
    operations = [
        migrations.RemoveField(
            model_name='imagesubmission',
            name='number_lights_on',
        ),
        migrations.RemoveField(
            model_name='imagesubmission',
            name='number_of_lights',
        ),
        migrations.RemoveField(
            model_name='imagesubmission',
            name='number_of_windows',
        ),
        migrations.RemoveField(
            model_name='imagesubmission',
            name='number_plugs',
        ),
        migrations.RemoveField(
            model_name='imagesubmission',
            name='number_plugs_on',
        ),
        migrations.RemoveField(
            model_name='imagesubmission',
            name='number_windows_open',
        ),
        migrations.AddField(
            model_name='imagesubmission',
            name='lights_status',
            field=models.CharField(choices=[(
                'OFF', 'Off'),
                ('AUTO', 'Automatic'),
                ('ON', 'On')],
                default='OFF',
                max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagesubmission',
            name='windows_status',
            field=models.CharField(choices=[(
                'CLOSE', 'Closed'),
                ('AUTO', 'Automatic'),
                ('OPEN', 'Open')],
                default='CLOSE',
                max_length=5),
            preserve_default=False,
        ),
    ]
