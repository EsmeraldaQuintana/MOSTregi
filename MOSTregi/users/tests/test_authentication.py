# python imports
import datetime
import unittest
import re

# django imports
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.test import tag
from django.contrib.auth import get_user_model

# project imports
#from users.models import Token

# User = get_user_model()

class UserModelTest(TestCase):
    @tag('unfinished')
    def test_user_is_valid_with_email_only(self):
        self.fail('finish the test!')
        print("users > test_authentication > test_user_is_valid_with_email_only: ", end="")
        user = User(email='a@b.com')
        user.full_clean()  # should not raise
        print('OK')

    @tag('unfinished')
    def test_email_is_primary_key(self):
        print("users > test_authentication > test_email_is_primary_key: ", end="")
        self.fail('finish the test!')
        user = User(email='a@b.com')
        self.assertEqual(user.pk, 'a@b.com')
        print('OK')

class TokenModelTest(TestCase):
    @tag('unfinished')
    def test_links_user_with_auto_generated_uid(self):
        print("users > test_authentication > test_links_user_with_auto_generated_uid: ", end="")
        self.fail('finish the test!')
        token1 = Token.objects.create(email='a@b.com')
        token2 = Token.objects.create(email='a@b.com')
        self.assertNotEqual(token1.uid, token2.uid)
        print("OK")

class SignupFormTest(TestCase):
    # @tag('unfinished')
    def test_form_saving(self):
        print("users > test_authentication > test_form_saving: ", end="")
        response = self.client.get('/signup/')
        self.assertTrue(response.status_code != 404)
        response = self.client.post('/signup/',
                                    data={'name': 'testuser',
                                          'password1': 'fakepass1',
                                          'password2': 'fakepass1',
                                         },
                                    follow=True)
        self.assertTrue(response.status_code != 404)
        print("OK")
