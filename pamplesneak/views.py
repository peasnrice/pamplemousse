from django.shortcuts import render_to_response, RequestContext
from pamplesneak.models import Pamplesneak
from pamplesneak.forms import PamplesneakForm
from userprofile.models import PamplesneakInfo
from django.contrib.auth.decorators import login_required

class GameInfo():
   def __init__(self, game_id, game_name, active_players, max_players, word_bank_size, active):
      self.id = game_id
      self.game_name = game_name
      self.active_players = active_players
      self.max_players = max_players
      self.word_bank_size = word_bank_size
      self.active = active

def pamplesneak(request):
    args = {}
    return render_to_response('pamplesneak/pamplesneak.html', args, context_instance=RequestContext(request))

def pampleplay(request):
    games = Pamplesneak.objects.filter(active=True)
    games_list = [] 
    for game in games:
        gi = GameInfo(game.id,
            game.game_name, 
            game.getCurrentPlayers(), 
            game.number_of_players, 
            game.word_bank_size,
            game.active)
        games_list.append(gi)
    args = {}
    args['games_list'] = games_list
    return render_to_response('pamplesneak/play.html', args, context_instance=RequestContext(request))

def pampleref(request):
    args = {}
    return render_to_response('pamplesneak/ref.html', args, context_instance=RequestContext(request))

def pamplewatch(request):
    args = {}
    return render_to_response('pamplesneak/watch.html', args, context_instance=RequestContext(request))

def joingame(request):
    args = {}
    return render_to_response('pamplesneak/ingame.html', args, context_instance=RequestContext(request))

@login_required
def creategame(request):
    if request.method == 'POST':
        form = PamplesneakForm(data=request.POST)
        if form.is_valid():
            save_game = form.save(commit=False)
            save_game.active = True
            save_game.save()
            user = request.user
            pi = PamplesneakInfo.objects.get(user=user)
            pi.currentgame = save_game
            pi.save()
    else:
        form = PamplesneakForm()
    args = {}
    args['form'] = form
    return render_to_response('pamplesneak/create.html', args, context_instance=RequestContext(request))