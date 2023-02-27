from django.db import models
from django.core.validators import MinValueValidator
import uuid


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    points = models.PositiveIntegerField()

    def __str__(self):
        return self.username
