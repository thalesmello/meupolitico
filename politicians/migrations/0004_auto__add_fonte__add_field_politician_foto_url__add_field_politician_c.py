# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fonte'
        db.create_table(u'politicians_fonte', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('estrela1', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('estrela2', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('estrela3', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('estrela4', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('estrela5', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'politicians', ['Fonte'])

        # Adding field 'Politician.foto_url'
        db.add_column(u'politicians_politician', 'foto_url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300),
                      keep_default=False)

        # Adding field 'Politician.cargo'
        db.add_column(u'politicians_politician', 'cargo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Politician.cidade'
        db.add_column(u'politicians_politician', 'cidade',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Politician.telefone'
        db.add_column(u'politicians_politician', 'telefone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Adding field 'Politician.wikipedia'
        db.add_column(u'politicians_politician', 'wikipedia',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300),
                      keep_default=False)

        # Adding field 'Politician.youtube'
        db.add_column(u'politicians_politician', 'youtube',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300),
                      keep_default=False)

        # Adding field 'Politician.twitter'
        db.add_column(u'politicians_politician', 'twitter',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300),
                      keep_default=False)

        # Adding field 'Politician.facebook'
        db.add_column(u'politicians_politician', 'facebook',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300),
                      keep_default=False)

        # Adding field 'Politician.estrela1'
        db.add_column(u'politicians_politician', 'estrela1',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Politician.estrela2'
        db.add_column(u'politicians_politician', 'estrela2',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Politician.estrela3'
        db.add_column(u'politicians_politician', 'estrela3',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Politician.estrela4'
        db.add_column(u'politicians_politician', 'estrela4',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Politician.estrela5'
        db.add_column(u'politicians_politician', 'estrela5',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Removing M2M table for field relevant_news on 'Politician'
        db.delete_table('politicians_politician_relevant_news')


    def backwards(self, orm):
        # Deleting model 'Fonte'
        db.delete_table(u'politicians_fonte')

        # Deleting field 'Politician.foto_url'
        db.delete_column(u'politicians_politician', 'foto_url')

        # Deleting field 'Politician.cargo'
        db.delete_column(u'politicians_politician', 'cargo')

        # Deleting field 'Politician.cidade'
        db.delete_column(u'politicians_politician', 'cidade')

        # Deleting field 'Politician.telefone'
        db.delete_column(u'politicians_politician', 'telefone')

        # Deleting field 'Politician.wikipedia'
        db.delete_column(u'politicians_politician', 'wikipedia')

        # Deleting field 'Politician.youtube'
        db.delete_column(u'politicians_politician', 'youtube')

        # Deleting field 'Politician.twitter'
        db.delete_column(u'politicians_politician', 'twitter')

        # Deleting field 'Politician.facebook'
        db.delete_column(u'politicians_politician', 'facebook')

        # Deleting field 'Politician.estrela1'
        db.delete_column(u'politicians_politician', 'estrela1')

        # Deleting field 'Politician.estrela2'
        db.delete_column(u'politicians_politician', 'estrela2')

        # Deleting field 'Politician.estrela3'
        db.delete_column(u'politicians_politician', 'estrela3')

        # Deleting field 'Politician.estrela4'
        db.delete_column(u'politicians_politician', 'estrela4')

        # Deleting field 'Politician.estrela5'
        db.delete_column(u'politicians_politician', 'estrela5')

        # Adding M2M table for field relevant_news on 'Politician'
        db.create_table(u'politicians_politician_relevant_news', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('politician', models.ForeignKey(orm[u'politicians.politician'], null=False)),
            ('news', models.ForeignKey(orm[u'politicians.news'], null=False))
        ))
        db.create_unique(u'politicians_politician_relevant_news', ['politician_id', 'news_id'])


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