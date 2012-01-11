"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.template import Context

import settings
import documents.urls
import binder.templatetags.menu as menu_tag

class BinderTest(TestCase):
    def test_front_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        g = response.context['global']
        self.assertEqual("/", g['path'])
        self.assertEqual(settings.APP_TITLE, g['app_title'])
        
        main_menu = g['main_menu']
        self.assertEqual("Home", main_menu[0].title)
        self.assertEqual("front_page", main_menu[0].url_name)
        self.assertEqual("Documents", main_menu[1].title)
        self.assertEqual(documents.urls.urlpatterns[0].name,
            main_menu[1].url_name)
        self.assertEqual("Users", main_menu[2].title)
        self.assertEqual('/users', main_menu[2].url_name)
        
    def test_menu_tag_with_named_route(self):
        context = Context({'global':{'path':'/'}})
        self.assertEqual('<li class="selected"><a href="/">Home</a></li>',
            menu_tag.menu_item(context, 'front_page', 'Home'))

        context = Context({'global':{'path':'/foo'}})
        self.assertEqual('<li ><a href="/">Home</a></li>',
            menu_tag.menu_item(context, 'front_page', 'Home'))

    def test_menu_tag_with_uri(self):
        context = Context({'global':{'path':'/foo'}})
        self.assertEqual('<li ><a href="/">Home</a></li>',
            menu_tag.menu_item(context, '/', 'Home'))
        self.assertEqual('<li ><a href="/home">Home</a></li>',
            menu_tag.menu_item(context, '/home', 'Home'))