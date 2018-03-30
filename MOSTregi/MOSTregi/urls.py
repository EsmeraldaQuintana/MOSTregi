# MOSTregi/urls

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.auth import views as auth_views

from . import views
from users import views as users_views

urlpatterns = [
    re_path(r'^favicon.ico$',
        RedirectView.as_view(
            url=staticfiles_storage.url('img/favicon/favicon.ico'),
            permanent=False),
        name="favicon"
    ),
    re_path(r'^$', TemplateView.as_view(template_name='home.html')),
    path('home/', TemplateView.as_view(template_name='home.html')),
    re_path(r'^admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', users_views.signup.as_view(), name='signup'),
    path('events/', include('events.urls', 'events')),
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
