from django.db import migrations, models

class Migration(migrations.Migration):
    """ Defines the database migration for creating a user object, with
    columns for the player's name, score and number.
    """
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('points', models.IntegerField()),
            ],
        ),
    ]
