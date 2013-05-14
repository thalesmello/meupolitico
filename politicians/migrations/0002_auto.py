# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field politicians_favorited on 'User'
        db.create_table(u'politicians_user_politicians_favorited', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'politicians.user'], null=False)),
            ('politician', models.ForeignKey(orm[u'politicians.politician'], null=False))
        ))
        db.create_unique(u'politicians_user_politicians_favorited', ['user_id', 'politician_id'])


    def backwards(self, orm):
        # Removing M2M table for field politicians_favorited on 'User'
        db.delete_table('politicians_user_politicians_favorited')


    models = {
        u'politicians.news': {
            'Meta': {'object_name': 'News'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'politician': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['politicians.Politician']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
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
            'news_liked': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['politicians.News']", 'symmetrical': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'politicians_favorited': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['politicians.Politician']", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['politicians']