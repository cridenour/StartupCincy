from django.db import models
from django.db.models.signals import post_save
from django.contrib.localflavor.us.models import PhoneNumberField, USStateField

from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    company_website = models.CharField(max_length=64, null=True)
    company_linkedin_id = models.IntegerField(null=True)
    location = models.CharField(max_length=64)
    experience = models.CommaSeparatedIntegerField(max_length=32)
    salary = models.CommaSeparatedIntegerField(max_length=128)
    show_salary = models.BooleanField()
    post_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    about_company = models.TextField()
    description = models.TextField()
    responsibilities = models.TextField()
    requirements = models.TextField()
    apply_link = models.URLField(max_length=255)
    employer = models.ForeignKey(User)

    def __unicode__(self):
        return "%s at %s (%s)" % (self.title, self.company, self.location)

    def get_absolute_url(self):
        return "/jobs/%i" % self.id
    