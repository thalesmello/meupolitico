import feedparser
from dateutil import parser
from politicians.models import Politician, News

def add_news_to_db():
    folha_feeds = feedparser.parse('http://feeds.folha.uol.com.br/poder/rss091.xml')['entries']
    for politician in Politician.objects.all():
        for entry in filter(lambda feed: politician.name in feed['summary'], folha_feeds):
            # print entry['title'].encode('utf-8')
            News.objects.create(politician=politician, title=entry['title'],
                pub_date=parser.parse(entry['published']))
    add_count = 0
    folha_feeds = feedparser.parse('http://feeds.folha.uol.com.br/poder/rss091.xml')['entries']
    for politician in Politician.objects.all():
        print politician.name
        current_news_titles = map(lambda nw: nw.title, politician.news_set.all())
        for entry in filter(lambda feed: politician.name in feed['summary'], folha_feeds):
            if not entry['title'] in current_news_titles:
                add_count += 1
                News.objects.create(politician=politician, title=entry['title'],
                    pub_date=parser.parse(entry['published']))
    return add_count
