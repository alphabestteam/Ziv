from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Person(models.Model):
    id = models.IntegerField(
        primary_key=True,
        editable=False,
        validators=[
            MinValueValidator(100000000),
            MaxValueValidator(999999999),
        ],
    )
    name = models.CharField(max_length=100)
    birth_date = models.DateField(default=timezone.now)
    city = models.CharField(max_length=100)
