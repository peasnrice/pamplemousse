from django import forms
from models import Pamplesneak
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import FormActions

class PamplesneakForm(forms.ModelForm):
    class Meta:
        model = Pamplesneak
        fields = ['game_name','number_of_players','word_bank_size']
        labels = {'number_of_players': ('max number of players'),}

class MessageSender(forms.Form):

    player_query = dict(User.objects.values_list('id', 'username'))

    word = forms.CharField()
    player = forms.ChoiceField(choices=player_query.items(), widget=forms.RadioSelect())