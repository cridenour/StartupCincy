from django.db import models
from startup.events.utils import get_meetup_group_id

class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    start = models.DateTimeField()
    where = models.CharField(max_length=255)
    who = models.CharField(max_length=128)
    meetup_id = models.CharField(blank=True, default=None, null=True, db_index=True, max_length=64)
    link = models.URLField(default=None, null=True)
    approved = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    imported = models.DateTimeField(blank=True, auto_now_add=True)

    def __unicode__(self):
        return self.title

class MeetupGroups(models.Model):
    name = models.CharField(max_length=128)
    group_url = models.URLField(help_text='Paste the URL to the group here. ID will be pulled from the API using this.')
    meetup_id = models.CharField(db_index=True, max_length=64)
    enabled = models.BooleanField(default=True, db_index=True, help_text='Continue to pull events from this groups?')
    auto_post = models.BooleanField(default=False, help_text='Can these events skip moderation?')
    auto_feature = models.BooleanField(default=False, help_text='Can these events be featured automatically?')

    def save(self, force_insert=False, force_update=False, using=None):

        meetup_id = get_meetup_group_id(self.group_url)
        if meetup_id is not False:
            self.meetup_id = meetup_id

        return super(MeetupGroups, self).save(force_insert, force_update, using)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Meetup Group'