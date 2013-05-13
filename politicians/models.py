from django.db import models

class Estado(models.Model):
    name = models.CharField(max_length=30)
    acronym = models.CharField(max_length=2)
    def __unicode__(self):
        return self.acronym

class Cidade(models.Model):
    name = models.CharField(max_length=50)
    cidade = models.ForeignKey(Estado)
    acronym = models.CharField(max_length=55)
    def __unicode__(self):
        return self.acronym

class Cargo(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Party(models.Model):
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=10)
    def __unicode__(self):
        return self.acronym

class Politician(models.Model):
    name = models.CharField(max_length=100)
    foto_url = models.CharField(max_length=100)
    party = models.ForeignKey(Party)
    cargo = models.ForeignKey(Cargo)
    cidade = models.ForeignKey(Cidade)
    telefone = models.CharField(max_length=20)
    wikipedia = models.CharField(max_length=80)
    youtube = models.CharField(max_length=80)
    twitter = models.CharField(max_length=80)
    facebook = models.CharField(max_length=80)
    estrela1 = models.IntegerField(default=0)
    estrela2 = models.IntegerField(default=0)
    estrela3 = models.IntegerField(default=0)
    estrela4 = models.IntegerField(default=0)
    estrela5 = models.IntegerField(default=0)
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
