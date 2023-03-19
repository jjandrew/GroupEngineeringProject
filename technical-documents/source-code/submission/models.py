from django.db import models

# The choices of every room as a constant
building_choices = (('ALEXANDER', 'Alexander'),
                    ('AMORY', 'Amory'),
                    ('BILLDOUGLASCINEMAMUSEUM', 'Bill Douglas Cinema Museum'),
                    ('BUSINESSSCHOOLBUILDINGONE', 'Business School Building:One'),
                    ('BYRNEHOUSE', 'Byrne House'),
                    ('CATHOLICCHAPLAINCY', 'Catholic Chaplaincy'),
                    ('CENTREFORRESILLIENCEINENVIRONMENT,WATERANDWASTE',
                     'Centre for Resillience in Environment, Water and Waste'),
                    ('CLAYDEN', 'Clayden'),
                    ('CLYDESDALEHOUSE', 'Clydesdale House'),
                    ('CORNWALLHOUSE', 'Cornwall House'),
                    ('CORNWALLHOUSESWIMMINGPOOL', 'Cornwall House Swimming Pool'),
                    ('DEVONSHIREHOUSE', 'Devonshire House'),
                    ('DIGITALHUMANITIESLAB', 'Digital Humanities Lab'),
                    ('EXETERNORTHCOTTTHEATRE', 'Exeter Northcott Theatre'),
                    ('ESTATESERVICECENTRE', 'Estate Service Centre'),
                    ('FAMILYCENTREOWLETS', 'Family Centre (Owlets)'),
                    ('FORUM', 'Forum'),
                    ('GEOFFREYPOPE', 'Geoffrey Pope'),
                    ('GREATHALLANDUNIVERSITYRECEPTION',
                     'Great Hall and University Reception'),
                    ('HARRISON', 'Harrison'),
                    ('MATHEMATICALSCIENCES', 'Mathematical Sciences'),
                    ('HATHERLY', 'Hatherly'),
                    ('HENRYWELLCOMEBUILDINGFORBIOCATALYSIS',
                     'Henry Wellcome Building for Biocatalysis'),
                    ('HOPEHALL', 'Hope Hall'),
                    ('INNOVATIONCENTREPHASE1AND2',
                     'Innovation Centre Phase 1 and 2'),
                    ('INSTITUTEOFARABANDISLAMICSTUDIES',
                     'Institute of Arab and Islamic Studies'),
                    ('INTOINTERNATIONALSTUDYCENTRE',
                     'INTO International Study Centre'),
                    ('KAYBUILDING', 'Kay Building'), ('KAYHOUSEDURYARD',
                                                      'Kay House Duryard'),
                    ('KNIGHTLEY', 'Knightley'),
                    ('STRATEGYANDSECURITYINSTITUTE',
                     'Strategy and Security Institute'),
                    ('LAFROWDAHOUSE', 'Lafrowda House'),
                    ('LAVER', 'Laver'),
                    ('LAZENBY', 'Lazenby'),
                    ('LIBRARY', 'Library'),
                    ('LIVINGSYSTEMS', 'Living Systems'),
                    ('MAINRECEPTION', 'Main Reception'),
                    ('MARYHARRISMEMORIALCHAPEL', 'Mary Harris Memorial Chapel'),
                    ('NEWMAN', 'Newman'),
                    ('NORTHCOTEHOUSE', 'Northcote House'),
                    ('OLDLIBRARY', 'Old Library'),
                    ('PETERCHALKCENTRE', 'Peter Chalk Centre'),
                    ('PHYSICS', 'Physics'),
                    ('QUEENS', "Queen's"),
                    ('REDCOT', 'Redcot'),
                    ('REEDHALL', 'Reed Hall'),
                    ('REEDMEWSWELLBEINGCENTRE', 'Reed Mews Wellbeing Centre'),
                    ('ROBOROUGH', 'Roborough'),
                    ('RUSSELLSEALFITNESSCENTRE', 'Russell Seal Fitness Centre'),
                    ('SIRCHRISTOPHERONDAATJEDEVONCRICKETCENTRE',
                     'Sir Christopher Ondaatje Devon Cricket Centre'),
                    ('SIRHENRYWELLCOMEBUILDINGFORMOODDISORDERSRESEARCH',
                     'Sir Henry Wellcome Building for Mood Disorders Research'),
                    ('SPORTSPARK', 'Sports Park'),
                    ('STDAVIDSRETAILSERVICES', "St David's Retail Services"),
                    ('STREATHAMCOURT', 'Streatham Court'),
                    ('STREATHAMFARM', 'Streatham Farm'),
                    ('STUDENTHEALTHCENTRE', 'Student Health Centre'),
                    ('SOUTHWESTINSTITUTEOFTECHNOLOGY',
                     'South West Institute of Technology'),
                    ('TENNISCENTRE', 'Tennis Centre'),
                    ('THORNLEA', 'Thornlea'),
                    ('UNIVERSITYRECEPTIONANDGREATHALL',
                     'University Reception and Great Hall'),
                    ('VICAMBLERSHORTGAMETRAININGCENTREGOLF',
                     'Vic Ambler Short Game Training Centre (Golf)'),
                    ('WASHINGTONSINGER', 'Washington Singer'),
                    ('XFI', 'Xfi')
                    )

# The choices for the lights options
lights_choices = (("OFF", "Off"),
                  ("AUTO", "Automatic"),
                  ("ON", "On"),
                  )

# The choices for the window options
windows_choices = (("CLOSE", "Closed"),
                   ("AUTO", "Automatic"),
                   ("OPEN", "Open"),
                   )


class ImageSubmission(models.Model):
    """ A model containing all the required fields for the successfull
    submission of a room.
    """
    building = models.CharField(choices=building_choices, max_length=48)
    room = models.CharField(max_length=100)
    lights_status = models.CharField(choices=lights_choices, max_length=4)
    windows_status = models.CharField(
        choices=windows_choices, max_length=5)
    litter_items = models.PositiveIntegerField(default=0)

    # Uploads image to the media/images folder when in dev mode
    image = models.ImageField(upload_to='images')
    user = models.CharField(max_length=100)
    date = models.DateField()


class RoomModel(models.Model):
    """A model for a room in order to calculate environmental statistics"""
    building = models.CharField(choices=building_choices, max_length=48)
    name = models.CharField(max_length=100)
    number_lights_on = models.PositiveIntegerField(default=0)
    number_windows_open = models.PositiveIntegerField(default=0)
    litter_items = models.PositiveIntegerField(default=0)
    number_submissions = models.PositiveIntegerField(default=0)
    last_done = models.DateTimeField()
