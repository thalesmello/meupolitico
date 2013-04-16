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
		
class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=20)
	def __unicode__(self):
		return self.username