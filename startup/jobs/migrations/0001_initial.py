# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Job'
        db.create_table('jobs_job', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('company_website', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('post_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('about_company', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('responsibilities', self.gf('django.db.models.fields.TextField')()),
            ('requirements', self.gf('django.db.models.fields.TextField')()),
            ('apply_link', self.gf('django.db.models.fields.URLField')(max_length=255)),
        ))
        db.send_create_signal('jobs', ['Job'])


    def backwards(self, orm):
        
        # Deleting model 'Job'
        db.delete_table('jobs_job')


    models = {
        'jobs.job': {
            'Meta': {'object_name': 'Job'},
            'about_company': ('django.db.models.fields.TextField', [], {}),
            'apply_link': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'company_website': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'requirements': ('django.db.models.fields.TextField', [], {}),
            'responsibilities': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['jobs']
