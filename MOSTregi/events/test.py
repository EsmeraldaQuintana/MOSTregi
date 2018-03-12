# python imports
import datetime

# django imports
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

# project imports
from .views import new
from .forms import BookingRequestForm, current_hour

class AddEventPageTest(TestCase):
    def test_new_resolves_to_new_view(self):
        print("events/test.py > test_new_resolves_to_new_view: ", end="")
        found = resolve('/events/new/')
        self.assertEqual(found.func, new)
        print("OK")

    def test_new_template(self):
        print("events/test.py > test_new_template: ", end="")
        response = self.client.get('/events/new/')
        html = response.content.decode('utf8')
        self.assertTemplateUsed(response, 'events/new.html')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">', html)
        self.assertIn('<link rel="stylesheet" href="/static/css/index.css">', html)
        self.assertIn('<script type="text/javascript" src="/static/js/jquery-3.3.1.js"></script>', html)
        self.assertIn('<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        print("OK")

    def test_BookingRequestForm(self):
        print("events/test.py > test_BookingRequestForm:", end="")
        form_data = {'name': 'poo',
                     'email': 'poo@pooland.poo',
                     'telephone': '6463012333',
                     'date_request': datetime.date.today(),
                     'arrival_time': current_hour(),
                     'departure_time': current_hour(),
                     'number_attending': 1,
                     'school': 'p',
                    }
        form = BookingRequestForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())
        print("OK")

    def test_event_detail_template(self):
        print("events/test.py > test_event_detail_template: ", end="")
        response = self.client.get('/events/new/')
        response = self.client.post('/events/new/',
                                    data={'name': 'person',
                                                 'email': 'person@personcom.com',
                                                 'telephone': '6463012333',
                                                 'date_request': datetime.date.today(),
                                                 'arrival_time': current_hour(),
                                                 'departure_time': current_hour(addhours=1),
                                                 'number_attending': 1,
                                                 'school': 'p',
                                                })
        html = response.content.decode('utf8')
        self.assertTemplateUsed(response, 'events/event_detail.html')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">', html)
        self.assertIn('<link rel="stylesheet" href="/static/css/index.css">', html)
        self.assertIn('<script type="text/javascript" src="/static/js/jquery-3.3.1.js"></script>', html)
        self.assertIn('<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        print("OK")


    def test_form_saving(self):
        print("events/test.py > test_form_saving: ", end="")
        response = self.client.get('/events/new/')
        response = self.client.post('/events/new/',
                                    data={'name': 'person',
                                                 'email': 'person@personcom.com',
                                                 'telephone': '6463012333',
                                                 'date_request': datetime.date.today(),
                                                 'arrival_time': current_hour(),
                                                 'departure_time': current_hour(addhours=1),
                                                 'number_attending': 1,
                                                 'school': 'p',
                                                })
        self.assertTemplateUsed(response, 'events/event_detail.html')
        html = response.content.decode('utf8')
        self.assertIn('person', html)
        self.assertIn('person@personcom.com', html)
        self.assertIn('6463012333', html)
        self.assertIn('p', html)
        self.assertIn('1', html)
        print("OK")

# from django.apps import apps
# # from .admin import
#
# # for each django model, make sure it is registered in ./admin.py
#
# #class RegistrationModelTest(TestCase):
# #    def test_form_completeness(self):
# #       hasattr(self, ls)
#
# #class AdminSiteRegisterTest(TestCase):
# #    app = apps.get_app_config('events')
# #    for model in app.get_models():
# #        print(model.__name__)
#     #def test_nothing(self):
#        # self.fail("Test not finished...")
