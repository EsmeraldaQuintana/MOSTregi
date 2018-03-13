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

urlpatterns = [
    path('new/', views.new, name="new"),
    re_path(r'edit/(?P<pk>\d+)/', views.edit, name="edit"),
    re_path(r'show_detail/(?P<pk>\d+)/', views.show_detail, name="show_detail")
    #re_path(r'^([a-zA-Z/]{0,50})$', views.testCatch),
]
