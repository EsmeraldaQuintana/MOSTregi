# python imports
import datetime
import unittest
import re

# django imports
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.test import tag
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# project imports
from ..views import new
from ..forms import BookingRequestForm


class AddEventPageTest(TestCase):
    def test_new_resolves_to_new_view(self):
        print("events > test_AddEventPage > test_new_resolves_to_new_view: ", end="")
        found = resolve('/events/new/')
        self.assertEqual(found.func, new)
        print("OK")

    def test_new_template(self):
        print("events > test_AddEventPage > test_new_template: ", end="")
        response = self.client.get('/events/new/')
        self.assertTrue(response.status_code != 404)
        html = response.content.decode('utf8')
        self.assertTemplateUsed(response, 'events/new.html')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">', html)
        self.assertIn('<link rel="stylesheet" href="/static/css/index.css">', html)
        self.assertIn('<script type="text/javascript" src="/static/js/jquery-3.3.1.js"></script>', html)
        self.assertIn('<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        print("OK")

    def test_event_detail_template(self):
        print("events > test_AddEventPage > test_event_detail_template: ", end="")
        response = self.client.get('/events/new/')
        self.assertTrue(response.status_code != 404)
        user = User.objects.create_superuser(username='pinotnoir', email="fake@fake.com", password='pinotnoir')
        if not self.client.login(username='pinotnoir', password='pinotnoir'):
            self.fail("Could not log in!")
        response = self.client.post('/events/new/',
                                    data={'name': 'person',
                                                 'email': 'person@personcom.com',
                                                 'telephone': '6463012333',
                                                 'date_request': datetime.date(2018, 3, 13),
                                                 'arrival_time_hour': '07',
                                                 'arrival_time_minute': '30',
                                                 'arrival_time_meridiem': 'p.m.',
                                                 'departure_time_hour': '3',
                                                 'departure_time_minute': '30',
                                                 'departure_time_meridien': 'a.m',
                                                 'number_attending': 1,
                                                 'school': 'Peopleveristy',
                                                },
                                    follow=True)
        # note to self: post(..., follow=True) means follow the redirect
        self.assertTrue(response.status_code != 404)
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
        print("events > test_AddEventPage > test_form_saving: ", end="")
        response = self.client.get('/events/new/')
        self.assertTrue(response.status_code != 404)
        user = User.objects.create_superuser(username='pinotnoir', email="fake@fake.com", password='pinotnoir')
        if not self.client.login(username='pinotnoir', password='pinotnoir'):
            self.fail("Could not log in!")
        response = self.client.post('/events/new/',
                                    data={'name': 'person',
                                                 'email': 'person@personcom.com',
                                                 'telephone': '6463012333',
                                                 'date_request': datetime.date(2018, 3, 26),
                                                 'arrival_time_hour': '06',
                                                 'arrival_time_minute': '30',
                                                 'arrival_time_meridiem': 'a.m.',
                                                 'departure_time_hour': '3',
                                                 'departure_time_minute': '30',
                                                 'departure_time_meridiem': 'p.m.',
                                                 'number_attending': 1,
                                                 'school': 'Peopleveristy',
                                                },
                                    follow=True)
        self.assertTrue(response.status_code != 404)
        self.assertTemplateUsed(response, 'events/event_detail.html')
        html = response.content.decode('utf8')
        self.assertIn('person@personcom.com', html)
        self.assertIn('6463012333', html)
        self.assertIn('March 26, 2018', html)
        self.assertIn('6:30 a.m. - 3:30 p.m.', html)
        self.assertIn('1', html)
        self.assertIn('Peopleveristy', html)
        print("OK")
