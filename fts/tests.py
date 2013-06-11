# -*- coding: utf-8 -*-

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import timedelta

from politicians.models import Politician, User, News

class PoliticiansTest(LiveServerTestCase):
    fixtures = ['politicians.json']
    browser = None

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(5)
        super(PoliticiansTest, cls).setUpClass()

    def setUp(self):
        self.user = User.objects.all()[0]
        pass

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

        # The user sees if it contain all the information expected from database
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(politician.name, body.text)
        self.assertIn(politician.party.acronym, body.text)
        self.assertIn(u'Notícias', body.text)

    def execute_login(self):
        self.browser.get(self.live_server_url+'/login/')
        self.browser.find_element_by_id('login_username').send_keys(self.user.username)
        self.browser.find_element_by_id('login_password').send_keys(self.user.password)
        self.browser.find_element_by_id('login_button').click()

    def test_can_login(self):
        self.browser.get(self.live_server_url+'/login/')

        el = self.browser.find_element_by_id('login_header')
        if not el.is_displayed():
            unhide = self.browser.find_element_by_id('collapse_btn')
            unhide.click()
        el = self.browser.find_element_by_id('login_message')
        self.assertEquals(u'Você não está logado.', el.text)

        self.execute_login()

        el = self.browser.find_element_by_id('login_header')
        if not el.is_displayed():
            unhide = self.browser.find_element_by_id('collapse_btn')
            unhide.click()
        el = self.browser.find_element_by_id('login_message')
        self.assertEquals(u'Bem vindo, '+self.user.username, el.text)

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
        self.execute_login()
        self.browser.get(self.live_server_url+'/news/')
        news = News.objects.all()
        assert len(self.browser.find_elements_by_name('like_button'))==news.count()
        ct=0
        for el in self.browser.find_elements_by_name('count'):
            if "0 likes" in el.text:
                ct=ct+1    
        assert ct==5

    def test_user_changes_like_status(self):
        self.execute_login()
        self.browser.get(self.live_server_url+'/news/')
        news = News.objects.all()
        ct0=0
        ct1=0
        for el in self.browser.find_elements_by_name('count'):
            if "0 likes" in el.text:
                ct0=ct0+1
            elif "1 likes" in el.text:
                ct1=ct1+1
        assert ct0==news.count()
        assert ct1==0
        button = self.browser.find_elements_by_name('like_button')[0]
        button.click()
        ct0=0
        ct1=0
        for el in self.browser.find_elements_by_name('count'):
            if "0 likes" in el.text:
                ct0=ct0+1
            elif "1 likes" in el.text:
                ct1=ct1+1
        assert ct0==news.count()-1
        assert ct1==1
        pass

    def test_user_searches_news(self):
        self.browser.get(self.live_server_url)
        el = self.browser.find_element_by_id('news_search_btn')
        if not el.is_displayed():
            unhide = self.browser.find_element_by_id('collapse_btn')
            unhide.click()
        el = self.browser.find_element_by_id('news_search_btn')
        el.click()

        found_news = []
        for news in News.objects.all():
            if 'critica' in news.title:
                found_news.append(news.title)
            news.pub_date = news.pub_date - timedelta(days=8)
            news.save()

        keywords = self.browser.find_element_by_name('keywords')
        keywords.send_keys('critica')
        time = self.browser.find_element_by_name('time')
        for option in time.find_elements_by_tag_name('option'):
            if option.text == 'Nesta semana':
                option.click()
        submit = self.browser.find_element_by_id('search_news')
        submit.click()

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(u'Nenhuma notícia cadastrada.', body.text)
        self.browser.back()

        keywords = self.browser.find_element_by_name('keywords')
        keywords.clear()
        keywords.send_keys('critica')
        time = self.browser.find_element_by_name('time')
        for option in time.find_elements_by_tag_name('option'):
            if option.text == 'Qualquer data':
                option.click()
        submit = self.browser.find_element_by_id('search_news')
        submit.click()
        body = self.browser.find_element_by_tag_name('body')

        for news in found_news:
            self.assertIn(news, body.text)

    def test_user_changes_tendencioso_status(self):
        self.execute_login()

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

    def test_bias(self):
        news_set = News.objects.all().order_by('-pub_date')[:5]
        obj1 = news_set[1]
        obj2 = news_set[2]
        obj1.bias = True
        obj1.save()
        obj2.bias = True
        obj2.save()
        self.browser.get(self.live_server_url+'/news/')
        news0 = self.browser.find_element_by_css_selector('#bias0')
        news1 = self.browser.find_element_by_css_selector('#bias1')
        news2 = self.browser.find_element_by_css_selector('#bias2')
        news3 = self.browser.find_element_by_css_selector('#bias3')
        news4 = self.browser.find_element_by_css_selector('#bias4')

        self.assertIn(u'Confiavel', news0.text)
        self.assertIn(u'Tendenciosa', news1.text)
        self.assertIn(u'Tendenciosa', news2.text)
        self.assertIn(u'Confiavel', news3.text)
        self.assertIn(u'Confiavel', news4.text)
        # self.assertIn(element, )
        pass
