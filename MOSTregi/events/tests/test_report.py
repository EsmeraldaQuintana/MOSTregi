# python imports
import datetime
import unittest
import re

# django imports
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.test import tag

# project imports
from ..views import new
from ..forms import BookingRequestForm

class ReportEvents(TestCase):
    @tag('unfinished')
    def test_can_report_event_list(self):
        print("events > test_delete > test_can_report_event_list: ", end="")
        # go to events/new/
        response = self.client.get('/events/new/')
        self.assertTrue(response.status_code != 404)
        # enter new event, with name field Sadface DeleteMeSon
        response = self.client.post('/events/new/',
                                    data={'name': 'Sadface DeleteMeSon',
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
        # go to events list views
        # click "download list"
        # check if that file has "Sadface DeleteMeSon"
        # if it doesn't, fail!
        # self.fail("Finish the test!")
        print("OK")
