# django imports
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context

# project imports
from .models import BookingRequest
from .forms import BookingRequestForm

def show_detail(request, pk):
    event = event = get_object_or_404(BookingRequest, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def list_all(request):
    events = BookingRequest.objects.all().order_by('-date_time_received')
    return render(request, 'events/event_list.html', {'events': events})

@login_required(login_url='/login/')
def list_mine(request):
    events = BookingRequest.objects.filter(user=request.user).order_by('-date_time_received')
    return render(request, 'events/event_list.html', {'events': events})

@login_required(login_url='/login/')
@permission_required('events.add_bookingrequest', raise_exception=True)
def new(request):
    if request.method == "POST":
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            email_template = get_template('events/confirmation_email.txt')
            email_message = email_template.render({'event': post})
            send_mail('Subject Test',
                      email_message,
                      'from@mostregi.net',
                      [post.email],
                      fail_silently=False )
            return redirect('events:show_detail', pk=post.pk)
        else:
            print("form not valid, form errors: %s, form is bound: %s" % (form.errors.as_data(), form.is_bound))
            data=request.POST.get('date_request')
            print(data)
    else:
        form = BookingRequestForm
    return render(request, 'events/new.html', {'form': form})

def delete_all(self):
    try:
        BookingRequest.objects.all().delete()
        return redirect('events:list_all')
    except BookingRequest.DoesNotExist:
        return render(request, 'error.html', {'error': "Forms already deleted."})

@login_required(login_url='/login/')
@permission_required('events.delete_bookingrequest', raise_exception=True)
def delete(request, pk):
    if not request.user.is_authenticated:
        return render(request, 'error.html', {'error': "Permission Denied. Please log in before deleting."})
    try:
        event = BookingRequest.objects.get(pk=pk)
        deletetion_collector = event.delete()
        form = BookingRequestForm
        # INCOMPLETE: we want to give confirmation of delete, then add a new form.
        return redirect('events:list_all')
    except BookingRequest.DoesNotExist:
        return render(request, 'error.html', {'error': "Form already deleted."})

@login_required(login_url='/login/')
@permission_required('events.change_bookingrequest', raise_exception=True)
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
        form = BookingRequestForm(instance=event)
    return render(request, 'events/new.html', {'form': form})

def events_landing(request):
    html = "<html><body><h1> landing page </h1></body></html>"
    return HttpResponse(html)
