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
    bias = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.title

    @classmethod
    def get_model_fields(model):
        return model._meta.fields

    def get_likes_count(self):
        return len(self.user_set.all())

    def does_user_like_me(self, user):
        return (user in self.user_set.all())
        
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    news_liked = models.ManyToManyField(News)
    
    def __unicode__(self):
        return self.username
    
    def like_news(self,news):
        self.news_liked.add(news)
        
    def unlike_news(self,news):
        self.news_liked.remove(news)
