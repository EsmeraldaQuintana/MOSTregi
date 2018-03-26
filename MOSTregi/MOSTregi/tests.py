from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

class LandingPageTest(TestCase):
    def test_root_url_resolves_to_index_view(self):
        print("MOSTregi/test.py > test_root_url_resolves_to_index_view: ", end="")
        response = self.client.get('')
        self.assertTrue(response.status_code == 200)
        self.assertTemplateUsed(response, 'home.html')
        print("OK")

    def test_home_template(self):
        print("MOSTregi/test.py > test_home_template: ", end="")
        response = self.client.get('/home/')
        self.assertTrue(response.status_code == 200)
        html = response.content.decode('utf8')
        self.assertTemplateUsed(response, 'home.html')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">', html)
        self.assertIn('<link rel="stylesheet" href="/static/css/index.css">', html)
        self.assertIn('<script type="text/javascript" src="/static/js/jquery-3.3.1.js"></script>', html)
        self.assertIn('<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        print("OK")

    def test_can_travel_to_events_urls(self):
        print("MOSTregi/test.py > test_can_travel_to_events_urls: ", end="")
        response = self.client.get('/events/')
        self.assertTrue(response.status_code == 200)
        print("OK")
