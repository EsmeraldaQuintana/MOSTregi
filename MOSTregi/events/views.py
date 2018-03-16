# django imports
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import loader, TemplateDoesNotExist
from django.utils import timezone

# project imports
from .models import BookingRequest
from .forms import BookingRequestForm

def show_detail(request, pk):
    event = event = get_object_or_404(BookingRequest, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def list_all(request):
    events = BookingRequest.objects.all().order_by('-date_time_received')
    return render(request, 'events/event_list.html', {'events': events})

def new(request):
    if request.method == "POST":
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            post = form.save(request.POST)
            post.save()
            #return render(request, 'events/event_detail.html', {'event': post})
            return redirect('events:show_detail', pk=post.pk)
            #return redirect(reverse("events:confirm"), pk=post.pk)
        else:
            print("form not valid, form errors: %s, form is bound: %s" % (form.errors.as_data(), form.is_bound))
            data=request.POST.get('date_request')
            print(data)
    else:
        form = BookingRequestForm
    return render(request, 'events/new.html', {'form': form})

def edit(request, pk):
    event = get_object_or_404(BookingRequest, pk=pk)
    if request.method == "POST":
        form = BookingRequestForm(request.POST, instance=event)
        if form.is_valid():
            post = form.save(request.POST)
            post.save()
            return redirect('events:show_detail', pk=post.pk)
        else:
            print("form not valid, form errors: %s, form is bound: %s" % (form.errors.as_data(), form.is_bound))
            data=request.POST.get('date_request')
            print(data)
    else:
        form = BookingRequestForm
    return render(request, 'events/new.html', {'form': form})

def events_landing(request):
    html = "<html><body><h1> landing page </h1></body></html>"
    return HttpResponse(html)

# =============================================
#  code graveyard
# =============================================
#def events_list(request):
#    events = demo_form.objects.all().order_by('date_request')
#    return render_to_response('events/events_list.html', {'events': events})

#def admin(request):
#    return HttpResponseRedirect("admin/")

#def fetchHTML(request, title):
#    #print("In fetch HTML with", title)
#    if title.endswith("/"):
#        title = title[:-1]
#        #print("Found /, fixed to", title)
#    title += '.html'
#    try:
#        t = loader.get_template(title)
#        return render_to_response(title)
#    except TemplateDoesNotExist:
#        print("Template %s not found." % title)
#        raise Http404

#def redirect_and_add_slash(request, capture):
#    capture += '/'
#    #print("redirecting to ", capture)
#    return redirect(capture)

#def testCatch(request, capture="empty"):
#    print("========================================")
#    print("=========================================")
#    html = "<html><body> <h1> in events/views <br> Captured: ( %s )</h1> </body></html>" % capture
#    return HttpResponse(html)
