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
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name