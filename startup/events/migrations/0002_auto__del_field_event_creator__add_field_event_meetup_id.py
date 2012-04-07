# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Event.creator'
        db.delete_column('events_event', 'creator_id')

        # Adding field 'Event.meetup_id'
        db.add_column('events_event', 'meetup_id', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True), keep_default=False)

        # Adding index on 'MeetupGroups', fields ['enabled']
        db.create_index('events_meetupgroups', ['enabled'])

        # Adding index on 'MeetupGroups', fields ['meetup_id']
        db.create_index('events_meetupgroups', ['meetup_id'])


    def backwards(self, orm):
        
        # Removing index on 'MeetupGroups', fields ['meetup_id']
        db.delete_index('events_meetupgroups', ['meetup_id'])

        # Removing index on 'MeetupGroups', fields ['enabled']
        db.delete_index('events_meetupgroups', ['enabled'])

        # User chose to not deal with backwards NULL issues for 'Event.creator'
        raise RuntimeError("Cannot reverse this migration. 'Event.creator' and its values cannot be restored.")

        # Deleting field 'Event.meetup_id'
        db.delete_column('events_event', 'meetup_id')


    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imported': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'meetup_id': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
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
            'meetup_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['events']
