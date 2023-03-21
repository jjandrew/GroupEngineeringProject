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
        ('submission', '0002_roommodel_alter_imagesubmission_room'),
    ]

    operations = [
        # Outlines the migrations for altering, removing and adding each of
        # the fields for the image submission
        migrations.RemoveField(
            model_name='imagesubmission',
            name='lights',
        ),
        migrations.RemoveField(
            model_name='imagesubmission',
            name='no_litter',
        ),
        migrations.RemoveField(
            model_name='imagesubmission',
            name='sockets_off',
        ),
        migrations.RemoveField(
            model_name='imagesubmission',
            name='windows',
        ),
        migrations.AddField(
            model_name='imagesubmission',
            name='litter_items',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='imagesubmission',
            name='number_lights_on',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='imagesubmission',
            name='number_of_lights',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='imagesubmission',
            name='number_of_windows',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='imagesubmission',
            name='number_plugs',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='imagesubmission',
            name='number_plugs_on',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='imagesubmission',
            name='number_windows_open',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='roommodel',
            name='litter_items',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='roommodel',
            name='number_lights_on',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='roommodel',
            name='number_of_lights',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='roommodel',
            name='number_of_windows',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='roommodel',
            name='number_plugs',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='roommodel',
            name='number_plugs_on',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='roommodel',
            name='number_submissions',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='roommodel',
            name='number_windows_open',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
