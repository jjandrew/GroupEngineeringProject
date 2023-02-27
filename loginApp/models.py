from django.db import models
from django.core.validators import MinValueValidator


class User(models.Model):
    username = models.CharField(max_length=50)
    points = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.username
