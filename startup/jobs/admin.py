from jobs.models import Job
from django.contrib import admin

class JobAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Company Information', {'fields': ['company', 'location', 'about_company','company_website', 'startup', 'logo']}),
        ('Details', {'fields': ['title', 'description', 'responsibilities', 'requirements', 'apply_link']})
    ]

admin.site.register(Job, JobAdmin)