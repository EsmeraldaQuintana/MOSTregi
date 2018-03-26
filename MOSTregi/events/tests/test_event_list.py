# python imports
import datetime
import unittest
import re

# django imports
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

# project imports
from ..views import new
from ..forms import BookingRequestForm

class EventListTest(TestCase):
    def test_all_list(self):
        print("events > test_list > test_all_list: ", end="")
        response = self.client.post('/events/new/',
                                    data={'name': 'person1',
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
                                                 'school': 'Personschoolversity',
                                                },
                                    follow=True)
        self.assertTrue(response.status_code != 404)
        response = self.client.post('/events/new/',
                                    data={'name': 'person2',
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
                                                 'school': 'Personschoolversity',
                                                },
                                    follow=True)
        self.assertTrue(response.status_code != 404)
        response = self.client.post('/events/new/',
                                    data={'name': 'person3',
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
                                                 'school': 'Personschoolversity',
                                                },
                                    follow=True)
        self.assertTrue(response.status_code != 404)
        response = self.client.get('/events/all/')
        self.assertTrue(response.status_code != 404)
        html = response.content.decode('utf8')
        self.assertTrue(response.status_code != 404)
        self.assertTemplateUsed(response, 'events/event_list.html')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">', html)
        self.assertIn('<link rel="stylesheet" href="/static/css/index.css">', html)
        self.assertIn('<script type="text/javascript" src="/static/js/jquery-3.3.1.js"></script>', html)
        self.assertIn('<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertIn('person1', html)
        self.assertIn('person2', html)
        self.assertIn('person3', html)
        print("OK")
