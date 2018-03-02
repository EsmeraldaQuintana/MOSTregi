from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect
from django.template import loader, TemplateDoesNotExist

def index(request):
    return render_to_response('index.html')

def admin(request):
    return HttpResponseRedirect("admin/")

def fetchHTML(request, title):
    title += '.html'
    try:
        t = loader.get_template(title)
        return render_to_response(title)
    except TemplateDoesNotExist:
        raise Http404
