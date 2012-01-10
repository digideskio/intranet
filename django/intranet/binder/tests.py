"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import settings

class BinderTest(TestCase):
    def test_front_page(self):
        response = self.client.get('/')
        self.assertContains(response,
            "Welcome to the %s" % settings.APP_TITLE,
            msg_prefix=response.content)
