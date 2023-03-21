""" Creates the class for the migration for altering the number of points a
user has. """
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for altering the amount of points a user
    has.

    Args:
        migrations.Migration (Migration): The type of migrations to be
            applied on the database.
    """

    dependencies = [
        ('loginApp', '0002_alter_user_username'),
    ]

    operations = [
        # The operation for altering the points field of a user
        migrations.AlterField(
            model_name='user',
            name='points',
            field=models.PositiveIntegerField(),
        ),
    ]
