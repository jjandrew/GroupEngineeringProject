""" Creates the class for the migration for determining if the customuser is
a user
"""
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for changing the date of the user's
    last submission and their streak number.

        Args:
            migrations.Migration (Migration): The type of migrations to be
            applied on the database.
    """

    dependencies = [
        ('accounts', '0003_alter_customuser_is_user'),
    ]

    operations = [
        # Outlines the migration for altering the last_submission field for a
        # user
        migrations.AddField(
            model_name='customuser',
            name='last_submission',
            field=models.DateField(default='2023-01-01'),
        ),
        # Outlines the migration for altering a customuser's streak
        migrations.AddField(
            model_name='customuser',
            name='streak',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
