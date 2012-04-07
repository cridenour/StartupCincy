from jobs.models import Job
from django.contrib import admin

class JobAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Company Information', {'fields': ['company', 'location', 'about_company','company_website']}),
        ('Basic Information', {'fields': ['title']}),
        ('Details', {'fields': ['description', 'responsibilities', 'requirements', 'apply_link']})
    ]

admin.site.register(Job, JobAdmin)