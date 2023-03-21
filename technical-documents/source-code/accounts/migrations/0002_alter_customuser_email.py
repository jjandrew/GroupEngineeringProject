""" Creates the class for the migration for altering the email of a
customuser.
"""
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for altering the email of a customuser.
    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    dependencies = [
        ('accounts', '0001_initial'),
    ]

    # Outlines the migration for altering the customuser's email
    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
