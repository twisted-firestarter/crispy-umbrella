from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from .views import home_page

# Create your tests here.


class HomePageTest(TestCase):

    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertIs(found.func, home_page)


    def test_homepage_returns_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do Lists</title>', html)
        self.assertTrue(html.endswith('</html>'))