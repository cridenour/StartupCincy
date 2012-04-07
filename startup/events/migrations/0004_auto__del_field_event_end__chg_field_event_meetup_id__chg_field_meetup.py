# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Event.end'
        db.delete_column('events_event', 'end')

        # Changing field 'Event.meetup_id'
        db.alter_column('events_event', 'meetup_id', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Adding index on 'Event', fields ['meetup_id']
        db.create_index('events_event', ['meetup_id'])

        # Changing field 'MeetupGroups.meetup_id'
        db.alter_column('events_meetupgroups', 'meetup_id', self.gf('django.db.models.fields.CharField')(max_length=64))


    def backwards(self, orm):
        
        # Removing index on 'Event', fields ['meetup_id']
        db.delete_index('events_event', ['meetup_id'])

        # User chose to not deal with backwards NULL issues for 'Event.end'
        raise RuntimeError("Cannot reverse this migration. 'Event.end' and its values cannot be restored.")

        # Changing field 'Event.meetup_id'
        db.alter_column('events_event', 'meetup_id', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'MeetupGroups.meetup_id'
        db.alter_column('events_meetupgroups', 'meetup_id', self.gf('django.db.models.fields.IntegerField')())


    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imported': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True'}),
            'meetup_id': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'where': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'who': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'events.meetupgroups': {
            'Meta': {'object_name': 'MeetupGroups'},
            'auto_feature': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'auto_post': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'group_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meetup_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['events']
