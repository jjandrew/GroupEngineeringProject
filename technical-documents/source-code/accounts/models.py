""" Creates the class for creating a custom user. """
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """ A model that sets all the required fields for a customuser, incl if
    they have moderator status, their email, points and if they are a valid
    user.

    Args:
        AbstractUser (AbstractUser): The user object that is going to have its
            fields set.
    """
    points = models.IntegerField(default=0)
    email = models.EmailField(unique=True, null=False)
    last_submission = models.DateField(default="2023-01-01")
    streak = models.PositiveIntegerField(default=0)
