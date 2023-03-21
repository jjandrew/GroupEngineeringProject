""" Creates the class for migrating and initialising the submission app. """
from django.db import migrations, models


class Migration(migrations.Migration):
    """ Defines the database migration for creating the image submission model,
    with columns for ID and the choice of building the user is submitting
    (each building on campus).

    Args:
        migrations.Migration (Migration): The type of migrations to be applied
            on the database.
    """
    initial = True

    dependencies = [
    ]

    operations = [
        # Creates a migration with each of the fields below
        migrations.CreateModel(
            name='ImageSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(choices=[('ALEXANDER',
                                                        'Alexander'),
                                                       ('AMORY', 'Amory'),
                                                       ('BILLDOUGLASCINEMAMUSEUM',
                                                        'Bill Douglas Cinema Museum'),
                                                       ('BUSINESSSCHOOLBUILDINGONE',
                                                        'Business School Building:One'),
                                                       ('BYRNEHOUSE',
                                                        'Byrne House'),
                                                       ('CATHOLICCHAPLAINCY',
                                                        'Catholic Chaplaincy'),
                                                       ('CENTREFORRESILLI' +
                                                        'ENCEINENVIRONMENT,WATERANDWASTE',
                                                        'Centre for Resil' +
                                                        'lience in Environment, Water and Waste'),
                                                       ('CLAYDEN', 'Clayden'),
                                                       ('CLYDESDALEHOUSE',
                                                        'Clydesdale House'),
                                                       ('CORNWALLHOUSE',
                                                        'Cornwall House'),
                                                       ('CORNWALLHOUSESWIMMINGPOOL',
                                                        'Cornwall House Swimming Pool'),
                                                       ('DEVONSHIREHOUSE',
                                                        'Devonshire House'),
                                                       ('DIGITALHUMANITIESLAB',
                                                        'Digital Humanities Lab'),
                                                       ('EXETERNORTHCOTTTHEATRE',
                                                        'Exeter Northcott Theatre'),
                                                       ('ESTATESERVICECENTRE',
                                                        'Estate Service Centre'),
                                                       ('FAMILYCENTREOWLETS',
                                                        'Family Centre (Owlets)'),
                                                       ('FORUM', 'Forum'),
                                                       ('GEOFFREYPOPE',
                                                        'Geoffrey Pope'),
                                                       ('GREATHALLANDUNIVERSITYRECEPTION',
                                                        'Great Hall and University Reception'),
                                                       ('HARRISON',
                                                        'Harrison'),
                                                       ('MATHEMATICALSCIENCES',
                                                        'Mathematical Sciences'),
                                                       ('HATHERLY',
                                                        'Hatherly'),
                                                       ('HENRYWELLCOMEBUILDINGFORBIOCATALYSIS',
                                                        'Henry Wellcome Building' +
                                                        'for Biocatalysis'),
                                                       ('HOPEHALL',
                                                        'Hope Hall'),
                                                       ('INNOVATIONCENTREPHASE1AND2',
                                                        'Innovation Centre Phase 1 and 2'),
                                                       ('INSTITUTEOFARABANDISLAMICSTUDIES',
                                                        'Institute of Arab and Islamic Studies'),
                                                       ('INTOINTERNATIONALSTUDYCENTRE',
                                                        'INTO International Study Centre'),
                                                       ('KAYBUILDING',
                                                        'Kay Building'),
                                                       ('KAYHOUSEDURYARD',
                                                        'Kay House Duryard'),
                                                       ('KNIGHTLEY',
                                                        'Knightley'),
                                                       ('STRATEGYANDSECURITYINSTITUTE',
                                                        'Strategy and Security Institute'),
                                                       ('LAFROWDAHOUSE',
                                                        'Lafrowda House'),
                                                       ('LAVER', 'Laver'),
                                                       ('LAZENBY', 'Lazenby'),
                                                       ('LIBRARY', 'Library'),
                                                       ('LIVINGSYSTEMS',
                                                        'Living Systems'),
                                                       ('MAINRECEPTION',
                                                        'Main Reception'),
                                                       ('MARYHARRISMEMORIALCHAPEL',
                                                        'Mary Harris Memorial Chapel'),
                                                       ('NEWMAN', 'Newman'),
                                                       ('NORTHCOTEHOUSE',
                                                        'Northcote House'),
                                                       ('OLDLIBRARY',
                                                        'Old Library'),
                                                       ('PETERCHALKCENTRE',
                                                        'Peter Chalk Centre'),
                                                       ('PHYSICS', 'Physics'),
                                                       ('QUEENS', "Queen's"),
                                                       ('REDCOT', 'Redcot'),
                                                       ('REEDHALL',
                                                        'Reed Hall'),
                                                       ('REEDMEWSWELLBEINGCENTRE',
                                                        'Reed Mews Wellbeing Centre'),
                                                       ('ROBOROUGH',
                                                        'Roborough'),
                                                       ('RUSSELLSEALFITNESSCENTRE',
                                                        'Russell Seal Fitness Centre'),
                                                       ('SIRCHRISTOPHERONDAATJEDEVONCRICKETCENTRE',
                                                        'Sir Christopher Ondaatje Devon' +
                                                        'Cricket Centre'),
                                                       ('SIRHENRYWELLCOMEBUILDING' +
                                                        'FORMOODDISORDERSRESEARCH',
                                                        'Sir Henry Wellcome Building' +
                                                        ' for Mood Disorders Research'),
                                                       ('SPORTSPARK',
                                                        'Sports Park'),
                                                       ('STDAVIDSRETAILSERVICES',
                                                        "St David's Retail Services"),
                                                       ('STREATHAMCOURT',
                                                        'Streatham Court'),
                                                       ('STREATHAMFARM',
                                                        'Streatham Farm'),
                                                       ('STUDENTHEALTHCENTRE',
                                                        'Student Health Centre'),
                                                       ('SOUTHWESTINSTITUTEOFTECHNOLOGY',
                                                        'South West Institute of Technology'),
                                                       ('TENNISCENTRE',
                                                        'Tennis Centre'),
                                                       ('THORNLEA',
                                                        'Thornlea'),
                                                       ('UNIVERSITYRECEPTIONANDGREATHALL',
                                                        'University Reception and Great Hall'),
                                                       ('VICAMBLERSHORTGAMETRAININGCENTREGOLF',
                                                        'Vic Ambler Short Game' +
                                                        ' Training Centre (Golf)'),
                                                       ('WASHINGTONSINGER',
                                                        'Washington Singer'),
                                                       ('XFI', 'Xfi')], max_length=48)),
                ('room', models.CharField(max_length=10)),
                ('lights', models.CharField(choices=[
                 ('OFF', 'Off'), ('AUTO', 'Automatic')], max_length=4)),
                ('windows', models.CharField(choices=[
                 ('CLOSE', 'Closed'), ('AUTO', 'Automatic')], max_length=5)),
                ('no_litter', models.BooleanField()),
                ('sockets_off', models.BooleanField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
