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
    @tag('unfinished')
    def test_shows_logged_in(self):
        print("events > test_delete > test_shows_logged_in: ", end="")
        response = self.client.get('/')
        self.assertTrue(response.status_code != 404)
        html = response.content.decode('utf8')
        self.assertTrue(html.contains("Logged in") or html.contains("Not logged in."))
        print("OK")
