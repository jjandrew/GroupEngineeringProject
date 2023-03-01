from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """ A model that sets all the required fields for a user, incl if they
    have moderator status, their email, points and if they are a valid user.
    """
    is_mod = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    points = models.IntegerField(default=0)
    email = models.EmailField(unique=True, null=False)
