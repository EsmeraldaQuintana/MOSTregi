# django imports
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

# local imports
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.events_landing, name="events_landing"),
    path('new/', views.new, name="new"),
    re_path(r'edit/(?P<pk>\d+)/', views.edit, name="edit"),
    re_path(r'delete/(?P<pk>\d+)/', views.delete, name="delete"),
    path('delete_all/', views.delete_all, name="delete_all"),
    re_path(r'show_detail/(?P<pk>\d+)/', views.show_detail, name="show_detail"),
    path('all/', views.list_all, name="list_all"),
    path('all/mine/', views.list_mine, name="list_mine"),
    #re_path(r'^([a-zA-Z/]{0,50})$', views.testCatch),
]
