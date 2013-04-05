# -*- coding: utf-8 -*-

from django.test import LiveServerTestCase
from selenium import webdriver

from politicians.models import Politician

class PoliticiansTest(LiveServerTestCase):
    fixtures = ['politicians.json']

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()

    def test_can_access_the_homepage(self):
        # The user opens his web browser, and goes to the homepage
        self.browser.get(self.live_server_url)

        # The user sees if the page contains the information in hp_data
        hp_data = {'header_title': u'Meu Político', 'heading_text': u'Meu Político'}
        for id, value in hp_data.iteritems():
            element = self.browser.find_element_by_id(id)
            self.assertIn(value, element.text)

    def test_can_see_links_on_homepage(self):
        # The user opens his web browser, and goes to the homepage
        self.browser.get(self.live_server_url)

        # The user sees if the page contains the expected links
        links = {'/politicians/': u'Lista de Políticos', '/news/': u'Lista de Notícias'}
        for relative_url, text in links.iteritems():
            element = self.browser.find_element_by_link_text(text)
            link = self.live_server_url + relative_url
            self.assertEquals(link, element.get_attribute('href'))

    def test_can_navigate_from_homepage_to_politicians_list_page(self):
        # The user opens his web browser, and goes to the homepage
        self.browser.get(self.live_server_url)

        # The user sees if he can reach the politicians list page
        element = self.browser.find_element_by_link_text(u'Lista de Políticos')
        element.click()

        # The user sees if the page contains the a heading with certain text
        element = self.browser.find_element_by_id('heading_text')
        self.assertIn(u'Meu Político', element.text)
        self.assertIn(u'Políticos', element.text)

    def test_can_access_a_politicians_list_page(self):
        # The user opens his web browser, and goes to the politicians page
        self.browser.get(self.live_server_url + '/politicians/')

        # The user sees if the page contains the a heading with certain text
        element = self.browser.find_element_by_id('heading_text')
        self.assertIn(u'Meu Político', element.text)
        self.assertIn(u'Políticos', element.text)

        # The user sees if it contain all the information expected from database
        politicians_list = Politician.objects.all()
        for politician in politicians_list:
            element = self.browser.find_element_by_link_text(politician.name)
            link = self.live_server_url + '/politicians/' + str(politician.id) + '/'
            self.assertEquals(link, element.get_attribute('href'))


    def test_can_navigate_from_politicians_list_page_to_politician_profile(self):
        # The user opens his web browser, and goes to the homepage
        self.browser.get(self.live_server_url + '/politicians/')

        # The user sees if he can reach the politicians list page
        politician = Politician.objects.all()[0]
        element = self.browser.find_element_by_link_text(politician.name)
        element.click()

        # The user sees if the page contains the a heading with certain text
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(politician.name, body.text)

    def test_can_access_a_politician_profile(self):
        politician = Politician.objects.all()[0]

        # The user opens his web browser, and goes to the politicians page
        self.browser.get(self.live_server_url + '/politicians/' + str(politician.id))

        # The user sees if the page contains the a heading with certain text
        element = self.browser.find_element_by_id('heading_text')
        self.assertIn(u'Meu Político', element.text)
        self.assertIn(u'Perfil do Político', element.text)

        # The user sees if it contain all the information expected from database
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(politician.name, body.text)
        self.assertIn(politician.party.acronym, body.text)
        self.assertIn(u'Notícias', body.text)
