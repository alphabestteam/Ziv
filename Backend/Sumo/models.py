from django.db import models

class Sumo(models.Model):
    name = models.CharField(max_length=100, blank=True)
    birth_date = models.DateTimeField(null=True)
    weight = models.PositiveIntegerField(default=100)
    points = models.PositiveIntegerField(default=0)
