from dajax.core import Dajax
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.template.loader import render_to_string
from pamplesneak.models import GameWord
import random

word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()

@dajaxice_register
def refresh_words(request, word_bank_size):
    word_list = []
    for i in range(0,word_bank_size):
        word_list.append(random.choice(WORDS))

    dajax = Dajax()
    render = render_to_string('pamplesneak/wordbox.html', {'word_list': word_list})
    dajax.assign('#words_box', 'innerHTML', render)
    return dajax.json()

@dajaxice_register
def refreshWord(request, game_id, player_id):
    game_word = GameWord.objects.filter(game=game_id, player=player_id)
    player_word = game_word[0].word
    dajax = Dajax()
    render = render_to_string('pamplesneak/playerword.html', {'player_word': player_word})
    dajax.assign('#player_word', 'innerHTML', render)
    return dajax.json()

@dajaxice_register
def randomizeWord(request):
    dajax = Dajax()
    random_word = random.choice(WORDS)
    render = render_to_string('pamplesneak/playerword.html', {'random_word': random_word})
    dajax.assign('#player_word', 'innerHTML', render)
    return dajax.json()