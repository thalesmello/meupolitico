# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.bias'
        db.add_column(u'politicians_news', 'bias',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'News.bias'
        db.delete_column(u'politicians_news', 'bias')


    models = {
        u'politicians.fonte': {
            'Meta': {'object_name': 'Fonte'},
            'estrela1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'estrela2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'estrela3': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'estrela4': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'estrela5': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'politicians.news': {
            'Meta': {'object_name': 'News'},
            'bias': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'politicians.party': {
            'Meta': {'object_name': 'Party'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'politicians.politician': {
            'Meta': {'object_name': 'Politician'},
            'cargo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'cidade': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'estrela1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'estrela2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'estrela3': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'estrela4': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'estrela5': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'facebook': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300'}),
            'foto_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['politicians.Party']"}),
            'telefone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'twitter': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300'}),
            'wikipedia': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300'}),
            'youtube': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300'})
        },
        u'politicians.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news_downvoted': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'news_downvoted'", 'blank': 'True', 'to': u"orm['politicians.News']"}),
            'news_liked': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'news_liked'", 'blank': 'True', 'to': u"orm['politicians.News']"}),
            'news_upvoted': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'news_upvoted'", 'blank': 'True', 'to': u"orm['politicians.News']"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'politicians_favorited': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['politicians.Politician']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['politicians']