from django.db import migrations, models

class Migration(migrations.Migration):
    """ Defines the database migration for altering the amount of points a user
    has.
    """

    dependencies = [
        ('loginApp', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='points',
            field=models.PositiveIntegerField(),
        ),
    ]
