# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Job.logo'
        db.alter_column('jobs_job', 'logo', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))


    def backwards(self, orm):
        
        # Changing field 'Job.logo'
        db.alter_column('jobs_job', 'logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))


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
            'logo': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'requirements': ('django.db.models.fields.TextField', [], {}),
            'responsibilities': ('django.db.models.fields.TextField', [], {}),
            'startup': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'jobs'", 'null': 'True', 'to': "orm['startups.Company']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'startups.company': {
            'Meta': {'object_name': 'Company'},
            'blog': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75', 'blank': 'True'}),
            'employees': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'founded': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'homepage': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'overview': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'permalink': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['jobs']
