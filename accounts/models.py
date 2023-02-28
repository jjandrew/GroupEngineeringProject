from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    is_mod = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    points = models.IntegerField(default=0)