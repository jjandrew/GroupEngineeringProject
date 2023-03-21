""" Defines the operations that can be performed on given accounts """
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    """ Defines the database migration for defining and storing basic metrics
    about a customuser.

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                # Migrations to be applied on the database models
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False,
                                           verbose_name='ID')),

                # Migrations for the users password
                ('password', models.CharField(max_length=128,
                                              verbose_name='password')),

                # Migration to find the last time the user logged in
                ('last_login',
                 models.DateTimeField(blank=True, null=True,
                                      verbose_name='last login')),

                # Migration to determine if the user is superuser
                ('is_superuser',
                 models.BooleanField(default=False,
                                     help_text='Designates that this user '
                                     + 'has all permissions without '
                                     + 'explicitly assigning them.',
                                     verbose_name='superuser status')),

                # Migration to determine if the usersname is unique and less
                # than 150 characters long
                ('username',
                 models.CharField(error_messages={'unique':
                                                  'A user with that username'
                                                  + ' already exists.'},
                                  help_text='Required. 150 characters or'
                                            + ' fewer. Letters, digits and'
                                            + ' @/./+/-/_ only.',
                                  max_length=150,
                                  unique=True,
                                  validators=[django.contrib.auth.validators.
                                              UnicodeUsernameValidator()],
                                  verbose_name='username')),

                # Migration to validate the length of the user's first name
                ('first_name',
                 models.CharField(blank=True,
                                  max_length=150,
                                  verbose_name='first name')),

                # Migration to validate the length of the user's last name
                ('last_name',
                 models.CharField(blank=True,
                                  max_length=150,
                                  verbose_name='last name')),

                # Migration to validate the length of the user's email
                ('email',
                 models.EmailField(blank=True,
                                   max_length=254,
                                   verbose_name='email address')),

                # Migration to determine if the user is a staff member
                ('is_staff',
                 models.BooleanField(default=False,
                                     help_text='Designates whether the user'
                                     + 'can log into this admin site.',
                                     verbose_name='staff status')),

                # Migration to determine if the user is active on the site
                ('is_active',
                 models.BooleanField(default=True,
                                     help_text='Designates whether this user '
                                     + 'should be treated as active. Unselect'
                                     + ' this instead of deleting accounts.',
                                     verbose_name='active')),

                # Migration to determine the date the user joined the site
                ('date_joined',
                 models.DateTimeField(default=django.utils.timezone.now,
                                      verbose_name='date joined')),

                # Migration to determine if the user is a moderator
                ('is_mod', models.BooleanField(default=False)),

                # Migration to determine if the current person is a user
                ('is_user', models.BooleanField(default=False)),

                # Migration to find the number of points the user has
                ('points', models.IntegerField(default=0)),

                # Migration to determine which groups the user is in
                ('groups',
                 models.ManyToManyField(blank=True,
                                        help_text='The groups this user'
                                        + ' belongs to. A user will get all'
                                        + ' permissions granted to each of'
                                        + ' their groups.',
                                        related_name='user_set',
                                        related_query_name='user',
                                        to='auth.group',
                                        verbose_name='groups')),

                # Migration to determine the users permissions
                ('user_permissions',
                 models.ManyToManyField(blank=True,
                                        help_text='Specific permissions for'
                                        + ' this user.',
                                        related_name='user_set',
                                        related_query_name='user',
                                        to='auth.permission',
                                        verbose_name='user permissions')),

            ],
            # Options that can be applied to the user
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
