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

class DeleteEvent(TestCase):
    def test_shows_logged_in(self):
        print("events > test_delete > test_shows_logged_in: ", end="")
        response = self.client.get('/')
        user = User.objects.create_superuser(username='pinotnoir', email="fake@fake.com", password='pinotnoir')
        if not self.client.login(username='pinotnoir', password='pinotnoir'):
            self.fail("Could not log in!")
        self.assertTrue(response.status_code != 404)
        html = response.content.decode('utf8')
        self.assertTrue(("Logged in." in html) or ("not logged in" in html))
        print("OK")
