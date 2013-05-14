# -*- coding: utf-8 -*-

from django.test import LiveServerTestCase
from selenium import webdriver
from time import sleep

from politicians.models import Politician, User

class PoliticiansTest(LiveServerTestCase):
    fixtures = ['politicians.json']
    browser = None

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(5)
        super(PoliticiansTest, cls).setUpClass()

    def setUp(self):
        ### Felipe: inserting the user directly because there's no registration
        ### and because I don't understand your fixture/json stuff
        user = User(username='felipe',password='awesomeness.py revived')
        user.save()
        user = User(username='caio', password='caio')
        user.save()
        ###

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        super(PoliticiansTest, cls).tearDownClass()

    def test_can_access_the_homepage(self):
        # The user opens his web browser, and goes to the homepage
        self.browser.get(self.live_server_url)

        # The user sees if the page contains the information in hp_data
        hp_data = {'header_title': u'Meu Político'}
        for id, value in hp_data.iteritems():
            element = self.browser.find_element_by_id(id)
            self.assertIn(value, element.text)

    def test_can_see_links_on_homepage(self):
        # The user opens his web browser, and goes to the homepage
        self.browser.get(self.live_server_url)

        # The user sees if the page contains the expected links
        links = {'/politicians/': u'Políticos', '/news/': u'Notícias'}
        for relative_url, text in links.iteritems():
            element = self.browser.find_element_by_link_text(text)
            link = self.live_server_url + relative_url
            self.assertEquals(link, element.get_attribute('href'))

    def test_can_navigate_from_homepage_to_politicians_list_page(self):
        # The user opens his web browser, and goes to the homepage
        self.browser.get(self.live_server_url)

        # The user sees if he can reach the politicians list page
        self.browser.find_element_by_link_text(u'Políticos').click()
        self.assertEquals(self.live_server_url + '/politicians/', self.browser.current_url)

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
        self.assertEquals(self.live_server_url + '/politicians/' + str(politician.id) + '/', self.browser.current_url)

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

    def test_can_login(self):
        self.browser.get(self.live_server_url+'/login/')
        self.browser.find_element_by_id('login_username').send_keys('felipe')
        self.browser.find_element_by_id('login_password').send_keys('awesomeness.py revived')
        self.browser.find_element_by_id('login_button').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(u'Bem vindo, felipe', body.text)

    def test_no_like_buttons_when_not_logged(self):
        self.browser.get(self.live_server_url+'/news/')
        try:
            self.browser.find_element_by_name('like_button')
            assert 0
        except:
            pass
        try:
            self.browser.find_element_by_name('unlike_button')
            assert 0
        except:
            pass
        
    def test_user_sees_like_buttons(self):
        self.browser.get(self.live_server_url+'/login/')
        self.browser.find_element_by_id('login_username').send_keys('felipe')
        self.browser.find_element_by_id('login_password').send_keys('awesomeness.py revived')
        self.browser.find_element_by_id('login_button').click()
        self.browser.get(self.live_server_url+'/news/')
        assert len(self.browser.find_elements_by_name('like_button'))==5
        ct=0
        for el in self.browser.find_elements_by_name('count'):
            if "0 likes" in el.text:
                ct=ct+1    
        assert ct==5
        
    def test_user_changes_like_status(self):
        self.browser.get(self.live_server_url+'/login/')
        self.browser.find_element_by_id('login_username').send_keys('felipe')
        self.browser.find_element_by_id('login_password').send_keys('awesomeness.py revived')
        self.browser.find_element_by_id('login_button').click()
        self.browser.get(self.live_server_url+'/news/')
        self.browser.get(self.live_server_url+'/news/')
        ct0=0
        ct1=0
        for el in self.browser.find_elements_by_name('count'):
            if "0 likes" in el.text:
                ct0=ct0+1
            elif "1 likes" in el.text:
                ct1=ct1+1
        assert ct0==4 and ct1==1
        button = self.browser.find_elements_by_css_selector('input[type="submit"]')[0]
        button.click()
        ct0=0
        ct1=0
        for el in self.browser.find_elements_by_name('count'):
            if "0 likes" in el.text:
                ct0=ct0+1
            elif "1 likes" in el.text:
                ct1=ct1+1
        assert ct0==5 and ct1==0
        pass

    def test_user_searches_news(self):
        self.browser.get(self.live_server_url)
        el = self.browser.find_element_by_link_text('Procurar noticias')
        el.click()
        keywords = self.browser.find_element_by_name('keywords')
        keywords.send_keys('critica royalties')
        time = self.browser.find_element_by_name('time')
        for option in time.find_elements_by_tag_name('option'):
            if option.text == 'Nesta semana':
                option.click()
        submit = self.browser.find_element_by_css_selector('input[type="submit"]')
        submit.click()
        
        assert self.browser.find_element_by_xpath("//*[contains(.,'No results')]")
        self.browser.back()

        keywords = self.browser.find_element_by_name('keywords')
        keywords.clear()
        keywords.send_keys('critica royalties')
        time = self.browser.find_element_by_name('time')
        for option in time.find_elements_by_tag_name('option'):
            if option.text == 'Qualquer data':
                option.click()
        submit = self.browser.find_element_by_css_selector('input[type="submit"]')
        submit.click()

        assert self.browser.find_element_by_xpath("//*[contains(.,'critica Secretaria da Micro')]")
        assert self.browser.find_element_by_xpath("//*[contains(.,'Dilma detalha vetos')]")

    def test_user_changes_tendencioso_status(self):
        self.browser.get(self.live_server_url+'/login/')
        self.browser.find_element_by_id('login_username').send_keys('caio')
        self.browser.find_element_by_id('login_password').send_keys('caio')
        self.browser.find_element_by_id('login_button').click()
        self.browser.get(self.live_server_url+'/news/')
        self.browser.get(self.live_server_url+'/news/')
        
        ctZero = 0
        ct = 0
        for el in self.browser.find_elements_by_name('rating'):
            if "Grau de tendenciosidade: 0" in el.text:
                ctZero = ctZero + 1
            else:
                ct = ct + 1
        assert ctZero == 5
        assert ct == 0
        button = self.browser.find_elements_by_name('upvote_button')[0]
        button.click()
        ctZero = 0
        ctNeg = 0
        ctPos = 0
        for el in self.browser.find_elements_by_name('rating'):
            if "Grau de tendenciosidade: 0" in el.text:
                ctZero = ctZero + 1
            elif "Grau de tendenciosidade: 1" in el.text:
                ctPos = ctPos + 1
            else:
                ctNeg = ctNeg + 1
        assert ctZero == 4
        assert ctPos == 1
        assert ctNeg == 0
        button = self.browser.find_elements_by_name('downvote_button')[1]
        button.click()
        ctZero = 0
        ctNeg = 0
        ctPos = 0
        for el in self.browser.find_elements_by_name('rating'):
            if "Grau de tendenciosidade: 0" in el.text:
                ctZero = ctZero + 1
            elif "Grau de tendenciosidade: -1" in el.text:
                ctNeg = ctNeg + 1
            else:
                ctPos = ctPos + 1
        assert ctZero == 3 and ctNeg == 1 and ctPos == 1
        pass