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


class BookingRequestFormTest(TestCase):
    def test_BookingRequest_form(self):
        print("events > test_form > test_BookingRequestForm: ", end="")
        form_data = {'name': 'poo',
                     'email': 'poo@pooland.poo',
                     'telephone': '6463012333',
                     'date_request': datetime.date.today(),
                     'arrival_time_hour': '07',
                     'arrival_time_minute': '30',
                     'arrival_time_meridiem': 'p.m.',
                     'departure_time_hour': '3',
                     'departure_time_minute': '30',
                     'departure_time_meridien': 'a.m',
                     'number_attending': 1,
                     'school': 'p',
                    }
        form = BookingRequestForm(data=form_data)
        self.assertTrue(form.is_valid())
        print("OK")
