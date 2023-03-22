from django.db import migrations, models

class Migration(migrations.Migration):
    """ Defines the database migration for altering the email of a customuser.
    """

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
