from django.db import models
from players.models import Player
from tournaments.models import Tournament

class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player1 = models.ForeignKey(Player, related_name='player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='player2', on_delete=models.CASCADE)
    result = models.CharField(max_length=10, blank=True, null=True)  # 'player1', 'player2', 'draw'
