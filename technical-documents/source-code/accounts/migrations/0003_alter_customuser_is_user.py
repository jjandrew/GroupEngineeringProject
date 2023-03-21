""" Creates the class for the migration for determining if the customuser is
a user
"""
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for determining if the customuser is
    a user

        Args:
            migrations.Migration (Migration): The type of migrations to be
            applied on the database.
    """

    dependencies = [
        ('accounts', '0002_alter_customuser_email'),
    ]

    # Outlines the migration for altering the user field for a customuser
    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_user',
            field=models.BooleanField(default=True),
        ),
    ]
