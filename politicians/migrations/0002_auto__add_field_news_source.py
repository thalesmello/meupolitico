# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.source'
        db.add_column(u'politicians_news', 'source',
                      self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'News.source'
        db.delete_column(u'politicians_news', 'source')


    models = {
        u'politicians.news': {
            'Meta': {'object_name': 'News'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'politician': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['politicians.Politician']"}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['politicians.Party']"})
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