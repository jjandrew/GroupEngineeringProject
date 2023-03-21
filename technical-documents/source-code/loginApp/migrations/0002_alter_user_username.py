from django.db import migrations, models

class Migration(migrations.Migration):
    """ Defines the database migration for altering the username of a user. """
    dependencies = [
        ('loginApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
