from django.shortcuts import render_to_response, RequestContext, get_object_or_404
from pamplesneak.models import Pamplesneak, Player, GameWord
from pamplesneak.forms import PamplesneakForm, MessageSender
from userprofile.models import UserProfile, PamplesneakInfo
from django.contrib.auth.decorators import login_required
import random

word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()

class GameInfo():
   def __init__(self, game_id, game_name, slug, active_players, max_players, word_bank_size, active):
      self.id = game_id
      self.game_name = game_name
      self.slug = slug
      self.active_players = active_players
      self.max_players = max_players
      self.word_bank_size = word_bank_size
      self.active = active

def getActiveGames():
    games = Pamplesneak.objects.filter(active=True)
    games_list = [] 
    for game in games:
        gi = GameInfo(game.id,
            game.game_name, 
            game.slug,
            game.getCurrentPlayers(), 
            game.number_of_players, 
            game.word_bank_size,
            game.active)
        games_list.append(gi)
    return games_list    

@login_required
def pamplesneak(request):
    if request.method == "POST":
        form = MessageSender(data=request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            player_id = form.cleaned_data['player']
            
            player = Player.objects.get(id=player_id)

            new_word = GameWord(word=word, player=player, game=player.game)
            new_word.save()
    else:
        form = MessageSender()  



    args = {}
    args['form'] = form
    return render_to_response('pamplesneak/pamplesneak.html', args, context_instance=RequestContext(request))

def pampleplay(request):
    games_list = getActiveGames()
    args = {}
    args['games_list'] = games_list
    return render_to_response('pamplesneak/play.html', args, context_instance=RequestContext(request))

def pampleref(request):
    args = {}
    return render_to_response('pamplesneak/ref.html', args, context_instance=RequestContext(request))

def pamplewatch(request):
    args = {}
    return render_to_response('pamplesneak/watch.html', args, context_instance=RequestContext(request))

@login_required
def joingame(request, game_id, slug):
    game = get_object_or_404(Pamplesneak, pk=game_id)
    user = request.user
    word_list = []
    for i in range(0,game.word_bank_size):
        word_list.append(random.choice(WORDS))

    player = Player.objects.filter(game=game).get(name=user.username)

    if not player:
        new_player = Player(game=game, name=user.username)
        new_player.save()
        player = new_player

    user_profile = UserProfile.objects.get(user=user)
    pample_info = PamplesneakInfo.objects.get(user=user_profile)

    pample_info.current_game = player
    pample_info.previous_games.add(player)
    pample_info.save()

    if request.method == "POST":
        form = MessageSender(data=request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            player_id = form.cleaned_data['player']
            
            player = Player.objects.get(id=player_id)

            new_word = GameWord(word=word, player=player, game=player.game)
            new_word.save()

            args = {}
            args['form'] = form
            args['word'] = random.choice(WORDS)
            args['word_list'] = word_list
            args['word_bank_size'] = game.word_bank_size
            args['game'] = game
            args['player'] = player
            return render_to_response('pamplesneak/ingame.html', args, context_instance=RequestContext(request))
    else:
        form = MessageSender()  

    args = {}
    args['form'] = form
    args['word'] = random.choice(WORDS)
    args['word_list'] = word_list
    args['word_bank_size'] = game.word_bank_size
    args['game'] = game
    args['player'] = player
    return render_to_response('pamplesneak/ingame.html', args, context_instance=RequestContext(request))

@login_required
def creategame(request):
    if request.method == 'POST':
        form = PamplesneakForm(data=request.POST)
        if form.is_valid():
            save_game = form.save(commit=False)
            save_game.active = True
            save_game.save()
            games_list = getActiveGames()
            args = {}
            args['games_list'] = games_list
            args['word'] = random.choice(WORDS)
            return render_to_response('pamplesneak/play.html', args, context_instance=RequestContext(request))
    else:
        form = PamplesneakForm()
    args = {}
    args['form'] = form
    return render_to_response('pamplesneak/create.html', args, context_instance=RequestContext(request))