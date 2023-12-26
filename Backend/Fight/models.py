from django.db import models
from Sumo.models import Sumo
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Fight(models.Model):
    challenging_sumo = models.ForeignKey(Sumo, on_delete=models.CASCADE, related_name='challenging_sumo', related_query_name='challenging_sumo_fight')
    opponent_sumo = models.ForeignKey(Sumo, on_delete=models.CASCADE, related_name='opponent_sumo', related_query_name='opponent_sumo_fight')
    date = models.DateTimeField()
    winner = models.ForeignKey(Sumo, on_delete=models.CASCADE, related_name='winner', null=True, blank=True)
    fight_rank = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    def validations(self):
        if self.challenging_sumo == self.opponent_sumo:
            raise ValidationError("Challenging sumo and opponent sumo must be different.")




