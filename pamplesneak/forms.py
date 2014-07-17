from django import forms
from models import Pamplesneak

class PamplesneakForm(forms.ModelForm):
    class Meta:
        model = Pamplesneak
        fields = ['game_name','number_of_players','word_bank_size']
        labels = {'number_of_players': ('max number of players'),}