from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=15)
    def __unicode__(self):
        return self.user.username

class PamplesneakInfo(models.Model):
    user = models.ForeignKey('UserProfile')
    current_game = models.ForeignKey('pamplesneak.Pamplesneak', related_name='pamplesneak_current_game', blank=True, null=True)
    previous_games = models.ManyToManyField('pamplesneak.Pamplesneak', related_name='pamplesneak_previous_games', blank=True, null=True)
    games_played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])