""" Creates the class for the migration for creating a user object. """
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for creating a user object, with
    columns for the player's name, score and number.

    Args:
        migrations.Migration (Migration): The type of migrations to be
            applied on the database.
    """
    initial = True

    dependencies = [
    ]

    operations = [
        # The operation to create the user, with the required fields
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('points', models.IntegerField()),
            ],
        ),
    ]
