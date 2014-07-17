from django.shortcuts import render_to_response, RequestContext

# Returns Home Page from url /
def home(request):
    args = {}
    return render_to_response('index.html', args, context_instance=RequestContext(request)) 
