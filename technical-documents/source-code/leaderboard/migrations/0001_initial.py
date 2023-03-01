from django.db import migrations, models

class Migration(migrations.Migration):
    """ Defines the database migration for creating the leaderboard, with
    columns for the player's name, score and number.
    """

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
