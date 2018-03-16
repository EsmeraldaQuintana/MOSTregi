# MOSTregi/urls

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from . import views


urlpatterns = [
    re_path(r'^favicon.ico$',
        RedirectView.as_view(
            url=staticfiles_storage.url('img/favicon/favicon.ico'),
            permanent=False),
        name="favicon"
    ),
    re_path(r'^admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('events/', include('events.urls', 'events')),
    re_path(r'^(.*[^/])$', views.redirect_and_add_slash),
    re_path(r'^([a-zA-Z/]{0,50})$', views.fetchHTML),
    #re_path(r'admin/?', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]

# =============================================
#  code graveyard
# =============================================
# from django.conf import settings
# from os import listdir, walk
# from os.path import *
#
# def files_from_dir(directory):
#     result = []
#     for root, directories, filenames in walk(directory):
#         for directory in directories:
#             print()
#         for filename in filenames:
#             result.append(filename)
#     return result
#
# def files_from_list_of_dir(dir_list):
#     result = []
#     if not dir_list:
#         return result
#     for folder in dir_list:
#         print("calling files_from_dir on ", folder)
#         result.extend(files_from_dir(folder))
#     return result

# what we actually want to do is generate a list of static files that end in .html
# and if (w/e).html fits it, call views.fetchHTML
