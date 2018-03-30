from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required

# UNFINISHED
# need to protect this page with "is superuser..."
class signup(generic.CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form } )
        else:
            return render(request, 'error.html', {'error': "Permission Denied. Please log in before attempting to create a new user."})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
            # form = self.form_class(request.POST)
            # if form.is_valid():
            #     return self.form_valid(form)
            # else:
            #     return self.form_invalid(self.form_class(request.POST))
        else:
            return render(request, 'error.html', {'error': "Permission Denied. Please log in before creating a new user."})

    def form_valid(self, form):
        self.object = form.save()
        employee_group = Group.objects.get(name='employee')
        self.object.save()
        self.object.groups.add(employee_group)
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
