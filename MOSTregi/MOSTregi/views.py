from django.shortcuts import render_to_response
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.template import loader

def index(request):
    return render_to_response('index.html')

def fetchHTML(request, title): 
    title += '.html'
    try:
        # print("Attempting to get template %s" % title)
        t = loader.get_template(title)
        # print("Return on get_template: %s" % t)
        return render_to_response(title)
    except TemplateDoesNotExist:
        raise Http404
