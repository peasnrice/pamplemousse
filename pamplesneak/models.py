from django.db import models
from django.contrib.auth.models import User

class Pamplesneak(models.Model):
	game_name = models.CharField(max_length = 32)
	number_of_players = models.IntegerField(default = 2)
	word_bank_size = models.IntegerField(default = 5)

