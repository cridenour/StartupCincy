from django.contrib import admin

from startup.events.models import Event, MeetupGroups

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start', 'approved', 'featured']
    list_editable = ['approved', 'featured']

class MeetupGroupsAdmin(admin.ModelAdmin):
    list_display = ['name','enabled', 'auto_post', 'auto_feature']
    readonly_fields = ['meetup_id']

admin.site.register(Event, EventAdmin)
admin.site.register(MeetupGroups, MeetupGroupsAdmin)