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
    birthDate = models.DateField(default=timezone.now)
    homeTown = models.CharField(max_length=100)


class Parent(Person):
    work = models.CharField(max_length=100)
    baseSalary = models.DecimalField(max_digits=8, decimal_places=2, 
        validators=[MinValueValidator(0.00),
            MaxValueValidator(99999999.99),
        ]
    )
    children = models.ManyToManyField(
        Person,
        related_name='parents',
        blank=True,
        null=True
    )


