from django.shortcuts import render_to_response, RequestContext

def pamplesneak(request):
    args = {}
    return render_to_response('pamplesneak/pamplesneak.html', args, context_instance=RequestContext(request))