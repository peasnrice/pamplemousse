from django import forms
from models import Pamplesneak
from django.contrib.auth.models import User

class PamplesneakForm(forms.ModelForm):
    class Meta:
        model = Pamplesneak
        fields = ['game_name','number_of_players','word_bank_size']
        labels = {'number_of_players': ('max number of players'),}

class MessageSender(forms.Form):

    word = forms.CharField()

    #players = forms.ChoiceField(choices=players.items(), widget=forms.RadioSelect())
    #player_query = dict(User.objects.values_list('id', 'username'))
    #player = forms.ChoiceField(choices=player_query.items(), widget=forms.RadioSelect())

    def __init__(self, players, *args, **kwargs):
        super(MessageSender, self).__init__(*args, **kwargs)
        #now we add each question individually
        self.fields['players'] = forms.ChoiceField(choices=players.items(), widget=forms.RadioSelect())
