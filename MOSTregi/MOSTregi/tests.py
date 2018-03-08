from django.test import TestCase
from django.urls import resolve
from MOSTregi.views import index
from django.http import HttpRequest

# in MOSTregi/MOSTregi/test.py

class HomePageTest(TestCase):

    def test_root_url_resolves_to_index_view(self):
        print(" . . running test_root_url_resolves_to_index_view: ", end="")
        found = resolve('/')
        self.assertEqual(found.func, index)
        print("OK")

    def check_index_HTML_template(self):
        print(" . . check_index_HTML_template: ", end="")
        response = self.client.get('/')
        html.response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<script type="text/javascript" src="{% static \'/js/jquery-3.3.1.js\' %}"></script>')
        self.assertIn('{% load staticfiles %}')
        self.assertIn('{% load bootstrap3 %}')
        self.assertIn('{% bootstrap_css %}')
        self.assertIn('{% bootstrap_javascript %}')
        self.assertIn('{% bootstrap_messages %}')
        self.assertTrue(html.strip().endswith('</html>'))
        print("OK")
