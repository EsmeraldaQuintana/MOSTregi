from django.contrib import admin

# Register your models here.

from .models import registration, demo_form

# register the Entry model with the admin interface
admin.site.register(demo_form)
admin.site.register(registration)
