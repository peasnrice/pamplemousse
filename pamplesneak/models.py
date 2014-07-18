from django.db import models
from django.contrib.auth.models import User
from userprofile.models import PamplesneakInfo
from django.template.defaultfilters import slugify
import random

class Pamplesneak(models.Model):
    game_name = models.CharField(max_length = 32)
    slug = models.SlugField(default="Mr-slug-will-change-on-creation")
    number_of_players = models.IntegerField(default = 2)
    word_bank_size = models.IntegerField(default = 5)
    active = models.BooleanField(default=True)
    def getCurrentPlayers(self):
        players_in_game = PamplesneakInfo.objects.filter(current_game=self).count()
        return players_in_game
    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.game_name)
        super(Pamplesneak, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.game_name

class Player(models.Model):
    game = models.ForeignKey('Pamplesneak')
    name = models.CharField(max_length=64, null=True, blank=True)
    nick = models.CharField(max_length=64, null=True, blank=True)
    def __unicode__(self):
        return self.name

class GameWord(models.Model):
    game = models.ForeignKey('Pamplesneak')
    player = models.ForeignKey('Player')
    word = models.CharField(max_length=45)
    def __unicode__(self):
        return self.word
