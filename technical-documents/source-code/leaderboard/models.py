""" Creates the class for creting building models. """
from datetime import datetime
from django.db import models
from submission.models import building_choices


class BuildingModel(models.Model):
    """ A model for a room in order to calculate environmental statistics.

    Args:
        models.Model (Model): The django Model object used to create the
            fields and attributes for each building.
    """
    # Each of the fields to be included in the building models.
    name = models.CharField(choices=building_choices, max_length=48)

    stats_since = models.DateField(
        default=datetime.today().strftime('%Y-%m-%d'))

    co2 = models.FloatField(default=0)

    number_submissions = models.IntegerField(default=0)

    last_done = models.DateTimeField(default='2023-01-01 00:00:00 +0000')

    f_name = models.CharField(max_length=60, default="")

    norm_co2 = models.FloatField(default=0)
