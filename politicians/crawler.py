import feedparser
from dateutil import parser
from politicians.models import Politician, News, Fonte

class FeedCrawler(object):
    def __init__(self, url, source, politicians, current_news_titles):
        self.feeds = feedparser.parse(url)['entries']
        self.source = source
        self.politicians = politicians
        self.news_titles = current_news_titles

    def relevant_field(self, fd):
        return fd['summary']

    def commit_to_db(self):
        add_count = 0
        for entry in self.feeds:
            if not entry['title'] in self.news_titles:
                polits = filter(lambda p: p.name in self.relevant_field(entry), self.politicians)
                if polits:
                    add_count += 1
                    news = News.objects.create(title=entry['title'],
                        pub_date=parser.parse(entry['published']),
                        link=entry['link'],
                        source=self.source,
                        fonte=Fonte.objects.create()
                    )
                    for politician in polits:
                        politician.add_relevant_news(news)
        return add_count

class FeedCrawlerEstadao(FeedCrawler):
    def relevant_field(self, fd):
        # Estadao is not mainstream, it uses a different field with
        # the most comprehensive text
        return fd['content'][0]['value']


def add_news_to_db():
    add_count = 0
    urls = ['http://feeds.folha.uol.com.br/poder/rss091.xml',
            'http://noticias.terra.com.br/rss/Controller?channelid=058251a77fb05310VgnVCM4000009bf154d0RCRD&ctName=atomo-noticia&lg=pt-br',
            'http://br.noticias.yahoo.com/rss/politica-economica',
            'http://g1.globo.com/dynamo/politica/mensalao/rss2.xml',
            'http://brasileconomico.ig.com.br/rss/politica',
            'http://blogs.estadao.com.br/radar-politico/feed/']

    sources = ['Folha de Sao Paulo',
               'Terra Noticias',
               'Yahoo Noticias',
               'G1',
               'Brasil Economico',
               'Estadao']

    politicians = Politician.objects.all()
    add_count = 0
    current_news_titles = []
    for politician in politicians:
        current_news_titles.append(
            map(lambda nw: nw.title, politician.relevant_news.all()))

    # A hacker's way of flattening a list of lists (of scrum of scrums)
    news_titles = [item for sublist in current_news_titles for item in sublist]

    for url, source in zip(urls,sources):
        if 'estadao' in url:
            feed_crawler = FeedCrawlerEstadao(url, source, politicians, news_titles)
        else:
            feed_crawler = FeedCrawler(url, source, politicians, news_titles)
        add_count += feed_crawler.commit_to_db()

    return add_count
