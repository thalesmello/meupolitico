# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Party'
        db.create_table(u'politicians_party', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'politicians', ['Party'])

        # Adding model 'Politician'
        db.create_table(u'politicians_politician', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['politicians.Party'])),
        ))
        db.send_create_signal(u'politicians', ['Politician'])

        # Adding model 'News'
        db.create_table(u'politicians_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('politician', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['politicians.Politician'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'politicians', ['News'])

        # Adding model 'User'
        db.create_table(u'politicians_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'politicians', ['User'])

        # Adding M2M table for field news_liked on 'User'
        db.create_table(u'politicians_user_news_liked', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'politicians.user'], null=False)),
            ('news', models.ForeignKey(orm[u'politicians.news'], null=False))
        ))
        db.create_unique(u'politicians_user_news_liked', ['user_id', 'news_id'])


    def backwards(self, orm):
        # Deleting model 'Party'
        db.delete_table(u'politicians_party')

        # Deleting model 'Politician'
        db.delete_table(u'politicians_politician')

        # Deleting model 'News'
        db.delete_table(u'politicians_news')

        # Deleting model 'User'
        db.delete_table(u'politicians_user')

        # Removing M2M table for field news_liked on 'User'
        db.delete_table('politicians_user_news_liked')


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
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['politicians']