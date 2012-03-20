# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Company'
        db.create_table('startups_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('permalink', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('homepage', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True)),
            ('blog', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('employees', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('founded', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
            ('overview', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('startups', ['Company'])

        # Adding model 'CompanyPeople'
        db.create_table('startups_companypeople', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='people', to=orm['startups.Company'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('permalink', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('startups', ['CompanyPeople'])


    def backwards(self, orm):
        
        # Deleting model 'Company'
        db.delete_table('startups_company')

        # Deleting model 'CompanyPeople'
        db.delete_table('startups_companypeople')


    models = {
        'startups.company': {
            'Meta': {'object_name': 'Company'},
            'blog': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75', 'blank': 'True'}),
            'employees': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'founded': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'homepage': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'overview': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'permalink': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        },
        'startups.companypeople': {
            'Meta': {'object_name': 'CompanyPeople'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'people'", 'to': "orm['startups.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'permalink': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['startups']
