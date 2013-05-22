import feedparser
from dateutil import parser
from politicians.models import Politician, News

class FeedCrawler(object):
    def __init__(self, url):
        self.feeds = feedparser.parse(url)['entries']

    def relevant_field(self, fd):
        return fd['summary']

    def commit_to_db(self, politician, current_news_titles):
        add_count = 0
        for entry in filter(lambda fd: politician.name in self.relevant_field(fd), self.feeds):
            if not entry['title'] in current_news_titles:
                add_count += 1
                News.objects.create(politician=politician, title=entry['title'],
                    pub_date=parser.parse(entry['published']),
                    link=entry['link']
                )
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

    politicians = Politician.objects.all()
    add_count = 0
    current_news_titles = {}
    for politician in politicians:
        current_news_titles[politician.name] = map(lambda nw: nw.title, politician.news_set.all())

    for url in urls:
        if 'estadao' in url:
            feed_crawler = FeedCrawlerEstadao(url)
        else:
            feed_crawler = FeedCrawler(url)
        for politician in politicians:
            add_count+=feed_crawler.commit_to_db(politician, current_news_titles[politician.name])

    return add_count
