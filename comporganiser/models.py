from django.db import models

class Stations(models.Model):
	name = models.CharField(max_length=128)
	slug = models.SlugField

class Games(models.Model):
	name = models.CharField(max_length=32)
	max_players = models.IntegerField()
