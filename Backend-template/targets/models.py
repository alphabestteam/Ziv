from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


class Target(models.Model):
    name = models.CharField(max_length=100)
    attack_priority = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(10)])
    # Defined ranges for x and y axises
    latitude = models.DecimalField(decimal_places = 3, max_digits = 6, validators = [MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.DecimalField(decimal_places = 3, max_digits = 6, validators = [MinValueValidator(-180), MaxValueValidator(180)])
    enemy_organization = models.CharField(max_length = 100)
    target_goal = models.CharField(max_length = 100)
    was_target_destroyed = models.BooleanField(default = False)
    target_id = models.CharField(max_length = 4, unique = True, editable = False)


