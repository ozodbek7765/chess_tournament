from django.db import models
from players.models import Player

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    participants = models.ManyToManyField(Player)
