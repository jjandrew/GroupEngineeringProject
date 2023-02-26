from django.db import models


class User(models.Model):
    username = models.CharField(max_length=150)
    points = models.IntegerField()

    def __str__(self):
        return self.username
