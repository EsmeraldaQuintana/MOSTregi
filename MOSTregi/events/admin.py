from django.contrib import admin

# Register your models here.

from .models import BookingRequest, demo_form

# register the Entry model with the admin interface
admin.site.register(demo_form)
admin.site.register(BookingRequest)
