from django.db import models

class Estado(models.Model):
    name = models.CharField(max_length=30)
    acronym = models.CharField(max_length=2)
    def __unicode__(self):
        return self.acronym

class Cidade(models.Model):
    name = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado)
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

class Fonte(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=150)
    estrela1 = models.IntegerField(default=0)
    estrela2 = models.IntegerField(default=0)
    estrela3 = models.IntegerField(default=0)
    estrela4 = models.IntegerField(default=0)
    estrela5 = models.IntegerField(default=0)

    def __unicode__(self):
        return self.nome

class News(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    pub_date = models.DateTimeField('date published')
    source = models.CharField(max_length=200)
    bias = models.BooleanField(default=False)
    fonte = models.ForeignKey(Fonte)
    
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

    def get_all_politicians(self):
        return self.relevant_news.all()

class Politician(models.Model):
    name = models.CharField(max_length=100, default='')    
    party = models.ForeignKey(Party)
    relevant_news = models.ManyToManyField(News, blank=True, related_name="relevant_news")
    foto_url = models.CharField(max_length=300, default='')
    cargo = models.CharField(max_length=50, default='')
    cidade = models.CharField(max_length=50, default='')
    telefone = models.CharField(max_length=20, default='')
    wikipedia = models.CharField(max_length=300, default='')
    youtube = models.CharField(max_length=300, default='')
    twitter = models.CharField(max_length=300, default='')
    facebook = models.CharField(max_length=300, default='')

    estrela1 = models.IntegerField(default=0)
    estrela2 = models.IntegerField(default=0)
    estrela3 = models.IntegerField(default=0)
    estrela4 = models.IntegerField(default=0)
    estrela5 = models.IntegerField(default=0)

    # reviews = models.ManyToManyField(Review, blank=True, related_name="reviews")

    def __unicode__(self):
        return self.name
    def get_relevant_news(self):
        return self.relevant_news.all()
    def is_relevant_news(self, news):
        return news in self.get_relevant_news()
    def add_relevant_news(self, news):
        self.relevant_news.add(news)
    def remove_relevant_news(self, news):
        self.relevant_news.remove(news)
    def get_total_estrelas(self):
        return self.estrela1+self.estrela2+self.estrela3+self.estrela4+self.estrela5
    def estrelaspercent(self, num):
        if self.get_total_estrelas() is not 0:
            return int(100*(1+num)/float(1+self.get_total_estrelas()))
        else:
            return 0

    # def get_reviews(self):
    #     return self.reviews.all()
    # def add_review(self, review):
    #     self.reviews.add(review)
    # def remove_review(self, review):
    #     self.reviews.remove(news)


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    news_liked = models.ManyToManyField(News, blank=True, related_name="news_liked")
    politicians_favorited = models.ManyToManyField(Politician, blank=True)
    news_upvoted = models.ManyToManyField(News, blank=True, related_name="news_upvoted")
    news_downvoted = models.ManyToManyField(News, blank=True, related_name="news_downvoted")
    # reviews_upvoted = models.ManyToManyField(Review, blank=True, related_name="reviews_upvoted")
    # reviews_downvoted = models.ManyToManyField(Review, blank=True, related_name="reviews_downvoted")
    # reviews_feitas = models.ManyToManyField(Review, blank=True, related_name="reviews_feitas")


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

    def get_reviews(self):
        return self.reviews_feitas.all()
    def add_review(self, review):
        self.reviews_feitas.add(review)
    def remove_review(self, review):
        self.reviews_feitas.remove(news)

    # def upvote_review(self, review):
    #     if (self in review.reviews_upvoted.all()):
    #         self.reviews_upvoted.remove(news)
    #     if (self in news.reviews_downvoted.all()):
    #         self.reviews_downvoted.remove(news)
    #     self.reviews_upvoted.add(news)
    #     return

    # def downvote_review(self, review):
    #     if (self in news.reviews_upvoted.all()):
    #         self.reviews_upvoted.remove(news)
    #     if (self in news.reviews_downvoted.all()):
    #         self.reviews_downvoted.remove(news)
    #     self.reviews_downvoted.add(news)
    #     return

    # def undo_upvote_review(self, review):
    #     if (self in news.reviews_upvoted.all()):
    #         self.reviews_upvoted.remove(news)
    #     if (self in news.reviews_downvoted.all()):
    #         self.reviews_downvoted.remove(news)
    #     return

    # def undo_downvote_review(self, review):
    #     if (self in news.reviews_upvoted.all()):
    #         self.reviews_upvoted.remove(news)
    #     if (self in news.reviews_downvoted.all()):
    #         self.reviews_downvoted.remove(news)
    #     return

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

class Review(models.Model):
    titulo = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    texto = models.CharField(max_length=10000)
    user = models.ForeignKey(User)
    politico = models.ForeignKey(Politician)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    numestrelas = models.IntegerField(default=0)
    users_upvoted = models.ManyToManyField(User, blank=True, related_name="users_upvoted")
    users_downvoted = models.ManyToManyField(User, blank=True, related_name="users_downvoted")

    def __unicode__(self):
        return self.titulo
    def utilidade(self):
        if (self.upvote + self.downvote) == 0:
            return 0
        else:
            return 1 + 100*self.upvote/float(self.downvote)

    def isnestrelas(self, val):
        return self.numestrelas == val
    @classmethod
    def get_model_fields(model):
        return model._meta.fields

    def upvote_review(self, user):
        if (user in self.users_upvoted.all()):
            self.users_upvoted.remove(user)
            self.upvote = self.upvote - 1
        if (user in self.users_downvoted.all()):
            self.users_downvoted.remove(user)
            self.downvote = self.downvote - 1
        self.users_upvoted.add(user)
        self.upvote = self.upvote + 1
        return

    def downvote_review(self, user):
        if (user in self.users_upvoted.all()):
            self.users_upvoted.remove(user)
            self.upvote = self.upvote - 1
        if (user in self.users_downvoted.all()):
            self.users_downvoted.remove(user)
            self.downvote = self.downvote - 1
        self.users_downvoted.add(user)
        self.downvote = self.downvote + 1
        return

    def undo_upvote_review(self, user):
        if (user in self.users_upvoted.all()):
            self.users_upvoted.remove(user)
            self.upvote = self.upvote - 1
        if (user in self.users_downvoted.all()):
            self.users_downvoted.remove(user)
            self.downvote = self.downvote - 1
        return

    def undo_downvote_review(self, user):
        if (user in self.users_upvoted.all()):
            self.users_upvoted.remove(user)
            self.upvote = self.upvote - 1
        if (user in self.users_downvoted.all()):
            self.users_downvoted.remove(user)
            self.downvote = self.downvote - 1
        return