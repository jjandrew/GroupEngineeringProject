# Generated by Django 4.1.5 on 2023-03-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0003_remove_imagesubmission_lights_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagesubmission',
            name='user',
            field=models.CharField(default='invalidUser', max_length=100),
            preserve_default=False,
        ),
    ]
