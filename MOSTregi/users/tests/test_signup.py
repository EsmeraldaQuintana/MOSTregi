# python imports
import re

# django imports
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.test import tag

# project imports
#from users.models import Token

class SignUpTest(TestCase):
    @tag('unfinished')
    def test_can_see_signup(self):
        print("MOSTregi/test.py > test_can_see_signup: ", end="")
        response = self.client.get('/signup/')
        self.assertTrue(response.status_code == 200)
        #self.assertTemplateUsed(response, 'home.html')
        print("OK")
