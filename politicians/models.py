from django.db import models

class Party(models.Model):
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=10)
    def __unicode__(self):
        return self.acronym

class Politician(models.Model):
    name = models.CharField(max_length=100)
    party = models.ForeignKey(Party)
    def __unicode__(self):
        return self.name

class News(models.Model):
    politician = models.ForeignKey(Politician)
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.title

    @classmethod
    def get_model_fields(model):
        return model._meta.fields

    def get_likes_count(self):
        return len(self.news_liked.all())

    def does_user_like_me(self, user):
        return (user in self.news_liked.all())

    def get_news_rating(self):
        return (len(self.news_upvoted.all()) - len(self.news_downvoted.all()))

    def get_user_vote(self, user):
        if (user in self.news_upvoted.all()):
            return 1
        elif (user in self.news_downvoted.all()):
            return -1
        else:
            return 0

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    news_liked = models.ManyToManyField(News, blank=True, related_name="news_liked")
    politicians_favorited = models.ManyToManyField(Politician, blank=True)
    news_upvoted = models.ManyToManyField(News, blank=True, related_name="news_upvoted")
    news_downvoted = models.ManyToManyField(News, blank=True, related_name="news_downvoted")

    def __unicode__(self):
        return self.username

    def like_news(self,news):
        self.news_liked.add(news)

    def unlike_news(self,news):
        self.news_liked.remove(news)

    def upvote_news(self, news):
        if (self in news.news_upvoted.all()):
            self.news_upvoted.remove(news)
        if (self in news.news_downvoted.all()):
            self.news_downvoted.remove(news)
        self.news_upvoted.add(news)
        return

    def downvote_news(self, news):
        if (self in news.news_upvoted.all()):
            self.news_upvoted.remove(news)
        if (self in news.news_downvoted.all()):
            self.news_downvoted.remove(news)
        self.news_downvoted.add(news)
        return

    def undo_upvote_news(self, news):
        if (self in news.news_upvoted.all()):
            self.news_upvoted.remove(news)
        if (self in news.news_downvoted.all()):
            self.news_downvoted.remove(news)
        return

    def undo_downvote_news(self, news):
        if (self in news.news_upvoted.all()):
            self.news_upvoted.remove(news)
        if (self in news.news_downvoted.all()):
            self.news_downvoted.remove(news)
        return

    def favorite_politician(self,politician_id):
        try:
            politician = Politician.objects.get(pk=politician_id)
            self.politicians_favorited.add(politician)
        except KeyError, Politician.DoesNotExist:
            pass

    def unfavorite_politician(self,politician_id):
        try:
            politician = Politician.objects.get(pk=politician_id)
            self.politicians_favorited.remove(politician)
        except KeyError, Politician.DoesNotExist:
            pass

    def has_favorited(self, politician):
        return politician in self.politicians_favorited.all()

    def favorited_politicians(self):
        return self.politicians_favorited.all()

