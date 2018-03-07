"""MOSTregi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

app_name = 'events'

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('new', views.new, name="new"),
    re_path(r'^([a-zA-Z/]{0,50})$', views.testCatch),
]

from django.conf import settings
from os import listdir, walk
from os.path import *

def files_from_dir(directory):
    result = []
    for root, directories, filenames in walk(directory):
        for directory in directories:
            print()
        for filename in filenames:
            result.append(filename)
    return result

def files_from_list_of_dir(dir_list):
    result = []
    if not dir_list:
        return result
    for folder in dir_list:
        print("calling files_from_dir on ", folder)
        result.extend(files_from_dir(folder))
    return result

# what we actually want to do is generate a list of static files that end in .html
# and if (w/e).html fits it, call views.fetchHTML
