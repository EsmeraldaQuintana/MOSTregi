from django.test import TestCase
from django.urls import resolve
from MOSTregi.views import index
from django.template.loader import render_to_string

class IndexTest(TestCase):
    print(" . . IndexTest")

    def test_root_url_resolves_to_index_view(self):
        print(" . . running test_root_url_resolves_to_index_view: ", end="")
        found = resolve('/')
        self.assertEqual(found.func, index)
        print("OK")

    def test_index_HTML_template(self):
        print(" . . test_index_HTML_template: ", end="")
        response = self.client.get('/')
        html = response.content.decode('utf8')
        #print(html)
        self.assertTrue(html.strip().startswith('<html>'))
    #    self.assertIn('<script type=\"text/javascript\" src=\"{% static \'/js/jquery-3.3.1.js\' %}\"></script>', html)
    #    self.assertIn('{% load staticfiles %}', html)
        #self.assertIn("load staticfiles", html)
        #self.assertIn('{% load bootstrap3 %}', html)
        #self.assertIn('{% bootstrap_css %}', html)
        #self.assertIn('{% bootstrap_javascript %}', html)
        #self.assertIn('{% bootstrap_messages %}', html)
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response, 'index.html')
        print("OK")
