""" Creates the class for the migration for adding a first name, surname
and email to a user object. """
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for adding the email, first name and
    last name of a user.

    Args:
        migrations.Migration (Migration): The type of migrations to be
            applied on the database.
    """
    dependencies = [
        ('loginApp', '0004_alter_user_username'),
    ]

    operations = [
        # The operations for adding a first name field, last name field and
        # email field for a user object
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='test@test.com', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='testl', max_length=50),
            preserve_default=False,
        ),
    ]
