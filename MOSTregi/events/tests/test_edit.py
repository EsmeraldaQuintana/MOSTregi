# python imports
import datetime
import unittest
import re

# django imports
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.test import tag
from django.contrib.auth.models import User

# project imports
from ..views import new
from ..forms import BookingRequestForm


class EditEvent(TestCase):
    def test_can_edit_after_submission(self):
        print("events > test_edit > test_can_edit_after_submission: ", end="")
        response = self.client.get('/events/new/')
        user = User.objects.create_superuser(username='pinotnoir', email="fake@fake.com", password='pinotnoir')
        if not self.client.login(username='pinotnoir', password='pinotnoir'):
            self.fail("Could not log in!")
        self.assertTrue(response.status_code != 404)
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
                                                 'school': 'Personschoolversity',
                                                },
                                    follow=True)
        self.assertTrue(response.status_code != 404)
        first_pk = re.search(r"(?<=/events/show_detail/)(([0-9]+)(?=/))",
                             response.request['PATH_INFO']).group(0)
        html = response.content.decode('utf8')
        edit_url = re.search(r"(/events/edit/[0-9]+/)", html).group(0)
        pk = re.search(r"(?<=/events/edit/)(([0-9]+)(?=/))",html).group(0)
        # print("first pk, from event detail:", first_pk)
        # print("pk, from edit link:", pk)
        # check that we are editing the object we just saved
        if pk != first_pk:
            print("%s != %s" % (pk, first_pk))
            self.fail("Form entry edited is not the same as the entry submitted!")
        response = self.client.get(edit_url, follow=True)
        self.assertTrue(response.status_code != 404)
        html = response.content.decode('utf8')
        self.assertTemplateUsed(response, 'events/new.html')
        response = self.client.post(response.request['PATH_INFO'],
                                    data={'name': 'personface',
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
        self.assertTemplateUsed(response, 'events/event_detail.html')
        html = response.content.decode('utf8')
        new_pk = re.search(r"(?<=/events/edit/)(([0-9]+)(?=/))",html).group(0)
        if new_pk != first_pk:
            print("%s != %s" % (new_pk, first_pk))
            self.fail("Form entry edited is not the same as the entry submitted!")
        print("OK")
