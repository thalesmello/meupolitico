# -*- coding: utf-8 -*-

from django.test import TestCase
from django.utils import timezone
from politicians.models import *
from crawler import *

class PartyModelTest(TestCase):
    def test_creating_a_new_party_and_saving_it_to_the_database(self):
        # start by creating a new Party object with its "name" and "acronym" set
        party = Party()
        party.name = "Partido dos Iteanos Bitolados"
        party.acronym = "PIB"

        # check we can save it to the database
        party.save()

        # now check we can find it in the database again
        all_parties_in_database = Party.objects.all()
        self.assertEquals(len(all_parties_in_database), 1)
        only_party_in_database = all_parties_in_database[0]
        self.assertEquals(only_party_in_database, party)

        # and check that it's saved its two attributes: name and acronym
        self.assertEquals(only_party_in_database.name, party.name)
        self.assertEquals(only_party_in_database.acronym, party.acronym)

class PoliticianModelTest(TestCase):
    def test_politician_objects_are_named_after_their_names(self):
        p = Politician()
        name = u"João"
        p.name = name
        self.assertEquals(name, unicode(p))

class NewsModelTest(TestCase):
    def test_verbose_name_for_pub_date(self):
        for field in News.get_model_fields():
            if field.name ==  'pub_date':
                self.assertEquals('date published', field.verbose_name)

    def test_user_likes_news(self):
        user = User.objects.create(username="Zezinho", password="senhaDoZezinho")
        party = Party.objects.create()
        polit = Politician.objects.create(party=party)
        news = News.objects.create(title="titulo inutil", politician=polit, pub_date=timezone.now())

        #User will like news
        user.like_news(news)
        count_likes = news.get_likes_count()
        self.assertEquals(count_likes, 1)
        self.assertTrue(news.does_user_like_me(user))

        #User count is still 1
        user.like_news(news)
        count_likes = news.get_likes_count()
        self.assertEquals(count_likes, 1)


class CrawlerTest(TestCase):
    def test_crawler(self):
        party = Party.objects.create()
        polit = Politician.objects.create(name='Dilma', party=party)
        add_news_to_db()
        second = add_news_to_db()
        self.assertEquals(second, 0)
