from django.db import models
from Fight.models import Fight
from Sumo.models import Sumo

class Gamble(models.Model):
    fight_id = models.ForeignKey(Fight, on_delete=models.CASCADE, related_name='fight_id')
    assumed_winner = models.ForeignKey(Sumo, on_delete=models.CASCADE, related_name='assumed_winner', blank=True, null=True)
    bet_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
