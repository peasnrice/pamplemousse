from django.db import models
from django.contrib.auth.models import User
from userprofile.models import PamplesneakInfo
from django.template.defaultfilters import slugify
import random
import datetime

class Pamplesneak(models.Model):
    game_name = models.CharField(max_length = 32)
    slug = models.SlugField(default="Mr-slug-will-change-on-creation")
    number_of_players = models.IntegerField(default = 2)
    word_bank_size = models.IntegerField(default = 5)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
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
    game = models.ForeignKey('Pamplesneak', related_name='pamplesneak_game')
    user = models.ForeignKey(User, related_name='pamplesneak_user')
    name = models.CharField(max_length=64, null=True, blank=True)
    nick = models.CharField(max_length=64, null=True, blank=True)
    succesful_sneaks = models.IntegerField(default=0)
    failed_sneaks = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name

class GameWord(models.Model):
    game = models.ForeignKey('Pamplesneak')
    player = models.ForeignKey('Player', null=True, blank=True)
    word = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.word