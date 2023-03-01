from django.db import migrations

class Migration(migrations.Migration):
    """ Defines the database migration for deleting the database."""

    dependencies = [
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Leaderboard',
        ),
    ]
