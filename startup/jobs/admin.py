from jobs.models import Job, EmployerProfile
from django.contrib import admin

class JobAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Company Information', {'fields': ['employer','company', 'location', 'about_company','company_website']}),
        ('Basic Information', {'fields': ['title', 'experience', 'salary', 'show_salary']}),
        ('Details', {'fields': ['description', 'responsibilities', 'requirements', 'apply_link']})
    ]

admin.site.register(Job, JobAdmin)
admin.site.register(EmployerProfile)