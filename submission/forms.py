from django import forms

building_choices = ((1, "Alexander"),
                    (2, "Amory"),
                    (3, "Bill Douglas Cinema Museum"),
                    (4, "Business School Building:One"),
                    (5, "Byrne House"),
                    (6, "Catholic Chaplaincy"),
                    (7, "Centre for Resillience in Environment, Water and Waste"),
                    (8, "Clayden"),
                    (9, "Clydesdale House"),
                    (10, "Cornwall House"),
                    (11, "Cornwall House Swimming Pool"),
                    (12, "Devonshire House"),
                    (13, "Digital Humanities Lab"),
                    (14, "Exeter Northcott Theatre"),
                    (15, "Estate Service Centre"),
                    (16, "Family Centre (Owlets)"),
                    (17, "Forum"),
                    (18, "Geoffrey Pope"),
                    (19, "Great Hall and University Reception"),
                    (20, "Harrison"),
                    (21, "Mathematical Sciences"),
                    (22, "Hatherly"),
                    (23, "Henry Wellcome Building for Biocatalysis"),
                    (24, "Hope Hall"),
                    (25, "Innovation Centre Phase 1 and 2"),
                    (26, "Institute of Arab and Islamic Studies"),
                    (27, "INTO International Study Centre"),
                    (28, "Kay Building"),
                    (29, "Kay House Duryard"),
                    (30, "Knightley"),
                    (31, "Strategy and Security Institute"),
                    (32, "Lafrowda House"),
                    (33, "Laver"),
                    (34, "Lazenby"),
                    (35, "Library"),
                    (36, "Living Systems"),
                    (37, "Main Reception"),
                    (38, "Mary Harris Memorial Chapel"),
                    (39, "Newman"),
                    (40, "Northcote House"),
                    (41, "Old Library"),
                    (42, "Peter Chalk Centre"),
                    (43, "Physics"),
                    (44, "Queen’s"),
                    (45, "Redcot"),
                    (46, "Reed Hall"),
                    (47, "Reed Mews Wellbeing Centre"),
                    (48, "Roborough"),
                    (49, "Russell Seal Fitness Centre"),
                    (50, "Sir Christopher Ondaatje Devon Cricket Centre"),
                    (51, "Sir Henry Wellcome Building for Mood Disorders Research"),
                    (52, "Sports Park"),
                    (53, "St David’s Retail Services"),
                    (54, "Streatham Court"),
                    (55, "Streatham Farm"),
                    (56, "Student Health Centre"),
                    (57, "South West Institute of Technology"),
                    (58, "Tennis Centre"),
                    (59, "Thornlea"),
                    (60, "University Reception and Great Hall"),
                    (61, "Vic Ambler Short Game Training Centre (Golf)"),
                    (62, "Washington Singer"),
                    (63, "Xfi")
                    )


lights_choices = ((1, "Off"),
                  (2, "Automatic"),
                  )

windows_choices = ((1, "Closed"),
                   (2, "Automatic"),
                   )


class RoomInputForm(forms.Form):
    building = forms.MultipleChoiceField(
        choices=building_choices)
    room_number = forms.CharField(label='Room Number', max_length=100)
    lights = forms.MultipleChoiceField(
        choices=lights_choices, label="Lights")
    windows = forms.MultipleChoiceField(
        choices=windows_choices, label="Windows")
    plug_sockets = forms.BooleanField(label="Plug sockets off:")
    litter = forms.BooleanField(label="Litter removed")
