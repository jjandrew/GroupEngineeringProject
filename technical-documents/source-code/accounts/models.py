""" The models to be used by the accounts section. """
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """ A model that sets all the required fields for a user such as their email,
    points and if they are a valid user.

    Args:
        AbstractUser: The AbstractUser object that represents the custom user
            which is being created.
    """
    # Each of the data fields stored on a user
    points = models.IntegerField(default=0)

    email = models.EmailField(unique=True, null=False)

    last_submission = models.DateField(default="2023-01-01")

    streak = models.PositiveIntegerField(default=0)

    daily_task = models.IntegerField(default=0)

    last_daily_task = models.DateField(default="2023-01-01")
