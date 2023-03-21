""" Creates the class for the migration for deleting a user. """
from django.db import migrations


class Migration(migrations.Migration):
    """ Defines the database migration for deleting a user from the database.

    Args:
        migrations.Migration (Migration): The type of migrations to be
            applied on the database.
    """
    dependencies = [
        ('loginApp', '0005_user_email_user_first_name_user_last_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
