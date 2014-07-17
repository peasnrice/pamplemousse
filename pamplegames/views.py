from django.shortcuts import render_to_response, RequestContext

def pamplegames(request):
    args = {}
    return render_to_response('pamplegames/pamplegames.html', args, context_instance=RequestContext(request))