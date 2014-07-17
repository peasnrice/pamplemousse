from django.db import models
from django.contrib.auth.models import User
from userprofile.models import PamplesneakInfo

class Pamplesneak(models.Model):
    game_name = models.CharField(max_length = 32)
    number_of_players = models.IntegerField(default = 2)
    word_bank_size = models.IntegerField(default = 5)
    active = models.BooleanField(default=True)
    def getCurrentPlayers(self):
        players_in_game = PamplesneakInfo.objects.filter(current_game=self).count()
        return players_in_game


