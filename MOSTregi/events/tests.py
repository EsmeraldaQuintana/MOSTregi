from django.test import TestCase


# Create your tests here.

from django.apps import apps
# from .admin import 

# for each django model, make sure it is registered in ./admin.py

from .models import registration

#class RegistrationModelTest(TestCase):
#    def test_form_completeness(self):
#       hasattr(self, ls)

class AdminSiteRegisterTest(TestCase):   
    app = apps.get_app_config('events')
    for model in app.get_models():
        print(model.__name__)
    #def test_nothing(self):
       # self.fail("Test not finished...")
