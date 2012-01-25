# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Company.employees'
        db.alter_column('startups_company', 'employees', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Company.twitter'
        db.alter_column('startups_company', 'twitter', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))


    def backwards(self, orm):
        
        # Changing field 'Company.employees'
        db.alter_column('startups_company', 'employees', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Company.twitter'
        db.alter_column('startups_company', 'twitter', self.gf('django.db.models.fields.CharField')(max_length=255))


    models = {
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
            'permalink': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'})
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
