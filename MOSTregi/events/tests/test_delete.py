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

class DeleteEvent(TestCase):
    # @tag('unfinished')
    def test_can_delete_after_submission(self):
        print("events > test_delete > test_can_delete_after_submission: ", end="")
        # go to events/new/
        response = self.client.get('/events/new/')
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
        # added_event_pk holds the primarykey of the event just added
        added_event_pk = re.search(r"(?<=/events/show_detail/)(([0-9]+)(?=/))",
                             response.request['PATH_INFO']).group(0)
        html = response.content.decode('utf8')
        delete_url = re.search(r"(/events/delete/[0-9]+/)", html).group(0)
        pk = re.search(r"(?<=/events/delete/)(([0-9]+)(?=/))",html).group(0)
        if pk != added_event_pk:
            print("%s != %s" % (pk, added_event_pk))
            self.fail("Form entry deleted is not the same as the entry submitted!")
        response = self.client.get(delete_url, follow=True)
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
        self.assertTemplateUsed(response, 'events/event_detail.html')
        html = response.content.decode('utf8')
        new_pk = re.search(r"(?<=/events/delete/)(([0-9]+)(?=/))",html).group(0)
        if new_pk != added_event_pk:
            print("%s != %s" % (new_pk, added_event_pk))
            self.fail("Form entry deleted is not the same as the entry submitted!")
        print("OK")
