from django.contrib import admin

from startups.models import Company, CompanyPeople

class CompanyPeopleInline(admin.TabularInline):
    model = CompanyPeople

class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        CompanyPeopleInline
    ]

admin.site.register(Company, CompanyAdmin)
