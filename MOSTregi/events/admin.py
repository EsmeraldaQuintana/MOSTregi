from django.contrib import admin

# Register your models here.

from .models import registration

# register the Entry model with the admin interface
admin.site.register(registration)
