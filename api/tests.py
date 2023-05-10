from django.test import TestCase
import requests


class TestApi(TestCase):
    def test_post(self):
        files = {'photo': open('test.png', 'rb')}
        response = requests.post(url='http://127.0.0.1:8000/',
                                 files=files)
        self.assertIn("name_dish", response.content.decode())
        self.assertIn("recipe_dish", response.content.decode())

    def test_get(self):
        response = requests.get(url='http://127.0.0.1:8000/')
        self.assertIn('null', response.content.decode())
