from django.db import migrations, models
import uuid

class Migration(migrations.Migration):
    """ Defines the database migration for adding the email, first name and
    last name of a user.
    """
    dependencies = [
        ('loginApp', '0004_alter_user_username'),
    ]

    operations = [
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
