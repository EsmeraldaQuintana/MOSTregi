
from django.shortcuts import render_to_response, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import loader, TemplateDoesNotExist

def index(request):
    return render_to_response('home.html')

def fetchHTML(request, title):
    #print("In fetch HTML with", title)
    if title.endswith("/"):
        title = title[:-1]
        #print("Found /, fixed to", title)
    title += '.html'
    try:
        t = loader.get_template(title)
        return render_to_response(title)
    except TemplateDoesNotExist:
        print("Template %s not found." % title)
        raise Http404

def redirect_and_add_slash(request, capture):
    capture += '/'
    #print("redirecting to ", capture)
    return redirect(capture)

def testCatch(request, capture="empty"):
    print("========================================")
    print("=========================================")
    html = "<html><body> <h1> Captured: ( %s )</h1> </body></html>" % capture
    return HttpResponse(html)
