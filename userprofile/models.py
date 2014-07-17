from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=32, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    def __unicode__(self):
        return self.user.username

class PamplesneakInfo(models.Model):
    user = models.OneToOneField(UserProfile)
    current_game = models.ForeignKey('pamplesneak.Player', related_name='player_current_game', blank=True, null=True)
    previous_games = models.ManyToManyField('pamplesneak.Player', related_name='player_previous_games', blank=True, null=True)
    games_played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    def __unicode__(self):
        return self.user.user.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
User.profile = property(lambda u: PamplesneakInfo.objects.get_or_create(user=UserProfile.objects.get_or_create(user=u)[0])[0])