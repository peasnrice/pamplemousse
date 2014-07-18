from dajax.core import Dajax
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.template.loader import render_to_string
from pamplesneak.models import GameWord, Player
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
    game_words = GameWord.objects.filter(game=game_id).filter(player=player_id).order_by('created')
    player_words = ""
    if not game_words:
        player_word = ""
    else:
        player_word = game_words[0].word

    dajax = Dajax()
    render = render_to_string('pamplesneak/playerword.html', {'player_word': player_word})
    dajax.assign('#player_word', 'innerHTML', render)
    return dajax.json()

@dajaxice_register
def randomizeWord(request):
    random_word = random.choice(WORDS)
    return simplejson.dumps({'random_word':random_word})

@dajaxice_register
def wordSuccess(request, game_id, player_id):
    game_words = GameWord.objects.filter(game=game_id).filter(player=player_id).order_by('created')[0]
    game_words.player=None
    game_words.save()

    player = Player.objects.get(id=player_id)
    player.succesful_sneaks += 1
    player.save()

    game_words = GameWord.objects.filter(game=game_id).filter(player=player_id).order_by('created')
    player_words = ""
    if not game_words:
        player_word = ""
    else:
        player_word = game_words[0].word

    dajax = Dajax()
    render = render_to_string('pamplesneak/playerword.html', {'player_word': player_word})
    dajax.assign('#player_word', 'innerHTML', render)
    return dajax.json()

@dajaxice_register
def wordFail(request, game_id, player_id):
    game_words = GameWord.objects.filter(game=game_id).filter(player=player_id).order_by('created')[0]
    game_words.player=None
    game_words.save()

    player = Player.objects.get(id=player_id)
    player.failed_sneaks += 1
    player.save()

    game_words = GameWord.objects.filter(game=game_id).filter(player=player_id).order_by('created')
    player_words = ""
    if not game_words:
        player_word = ""
    else:
        player_word = game_words[0].word

    dajax = Dajax()
    render = render_to_string('pamplesneak/playerword.html', {'player_word': player_word})
    dajax.assign('#player_word', 'innerHTML', render)

    return dajax.json()

@dajaxice_register
def refreshInGameStats(request, game_id, player_id):
    players = Player.objects.filter(game=game_id).order_by('-succesful_sneaks')
    
    dajax = Dajax()
    render = render_to_string('pamplesneak/ingamestats.html', {'players': players})
    dajax.assign('#ingame_stats', 'innerHTML', render)
    return dajax.json()