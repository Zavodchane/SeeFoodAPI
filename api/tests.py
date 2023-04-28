from django.test import TestCase
import requests


class TestApi(TestCase):
    def test_POST(self):
        files = {'photo': open('img.jpg', 'rb')}
        response = requests.post(url='http://127.0.0.1:8000/',
                                 files=files)
        self.assertIn("name_dish", response.content.decode())
        self.assertIn("recipe_dish", response.content.decode())

    def test_GET(self):
        response = requests.get(url='http://127.0.0.1:8000/')
        self.assertIn('null', response.content.decode())
