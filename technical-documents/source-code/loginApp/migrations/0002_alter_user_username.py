""" Creates the class for the migration for altering the username of a user.
"""
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for altering the username of a user.

    Args:
        migrations.Migration (Migration): The type of migrations to be
            applied on the database.
    """
    dependencies = [
        ('loginApp', '0001_initial'),
    ]

    operations = [
        # The operation for altering the username field of a user
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
