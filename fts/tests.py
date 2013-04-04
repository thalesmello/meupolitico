# -*- coding: utf-8 -*-

from django.test import LiveServerTestCase
from selenium import webdriver

class PoliticiansTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_access_the_homepage(self):
        # The user opens his web browser, and goes to the homepage
        self.browser.get(self.live_server_url + '/politicians')

        # User sees if the page contain the information in hp_data
        hp_data = {'header_title': u'Meu Político', 'heading_text': u'Meu Político'}
        for id, value in hp_data.iteritems():
            element = self.browser.find_element_by_id(id)
            self.assertIn(value, element.text)