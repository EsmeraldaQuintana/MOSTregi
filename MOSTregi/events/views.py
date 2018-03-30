# django imports
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required

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
@permission_required('events.add_BookingRequest', raise_exception=True)
def new(request):
    if request.method == "POST":
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('events:show_detail', pk=post.pk)
        else:
            print("form not valid, form errors: %s, form is bound: %s" % (form.errors.as_data(), form.is_bound))
            data=request.POST.get('date_request')
            print(data)
    else:
        form = BookingRequestForm
    return render(request, 'events/new.html', {'form': form})

@login_required(login_url='/login/')
@permission_required('events.delete_BookingRequest', raise_exception=True)
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
@permission_required('events.change_BookingRequest', raise_exception=True)
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
