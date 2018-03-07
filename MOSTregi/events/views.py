from django.shortcuts import render_to_response, redirect, render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import loader, TemplateDoesNotExist
from .models import demo_form
from .forms import demoForm

from django.utils import timezone

from django.urls import reverse


# the new event form view
def new(request):
    if request.method == "POST":
        form = demoForm(request.POST)
        if form.is_valid():
            post = form.save(request.POST)
            post.save()
            return redirect(reverse("events:confirm"))
        else:
            print("8=========D FORM NOT VALID")
            form = demoForm()
            return render(request, 'events/notvalid.html', {'form': form})
    else:
        form = demoForm()
    return render(request, 'events/new.html', {'form': form})

def confirm(request):
    return render_to_response('events/confirm.html')

def events_list(request):
    events = demo_form.objects.all().order_by('date_request')
    return render_to_response('events/events_list.html', {'events': events})

#def admin(request):
#    return HttpResponseRedirect("admin/")

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
    html = "<html><body> <h1> in events/views <br> Captured: ( %s )</h1> </body></html>" % capture
    return HttpResponse(html)
