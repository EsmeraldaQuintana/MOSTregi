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
from django.core import mail

# project imports
from ..views import new
from ..forms import BookingRequestForm

class EmailTest(TestCase):
    def test_send_email(self):
        print("events > test_email > test_send_email: ", end="")
        mail.send_mail(
            'TEST SUBJECT',
            'Test message.',
            'from@MOSTregi.new', ['to@tnotregi.net'],
            fail_silently=False,
        )
        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)
        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'TEST SUBJECT')
        print("OK")
