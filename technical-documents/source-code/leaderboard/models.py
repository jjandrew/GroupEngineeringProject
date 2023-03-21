""" Outlines the models to be used by the signUp app. """
from datetime import datetime
from django.db import models
from submission.models import building_choices


class BuildingModel(models.Model):
    """ A model for a room in order to calculate environmental statistics

    Args:
        models.Model: The building model object to store the data for.
    """
    # Each of the data fields to be stored for a given building
    name = models.CharField(choices=building_choices, max_length=48)

    stats_since = models.DateField(
        default=datetime.today().strftime('%Y-%m-%d'))
    co2 = models.FloatField(default=0)
    number_submissions = models.IntegerField(default=0)

    last_done = models.DateTimeField(default='2023-01-01 00:00:00 +0000')
