from django.db import models
from django.contrib.auth.models import AbstractUser

class Gambler(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    birthdate = models.DateTimeField(null = True)
    password = models.CharField(max_length=128, default='')
    username = models.CharField(max_length=150, unique=True, default='')
    is_staff = models.BooleanField(default=False)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    gambles = models.ManyToManyField('Gamble.Gamble', blank=True)
