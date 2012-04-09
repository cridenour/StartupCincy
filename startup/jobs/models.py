from django.db import models
from startup.startups.models import Company

class Job(models.Model):
    title = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    company_website = models.CharField(max_length=64, null=True)
    startup = models.ForeignKey(Company, related_name='jobs', blank=True, null=True)
    location = models.CharField(max_length=64)
    post_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    about_company = models.TextField()
    description = models.TextField()
    responsibilities = models.TextField()
    requirements = models.TextField()
    apply_link = models.URLField(max_length=255)

    def __unicode__(self):
        return "%s at %s (%s)" % (self.title, self.company, self.location)
    