from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    permalink = models.CharField(max_length=255, default='', blank=True, unique=True)
    homepage = models.URLField(default='', blank=True)
    blog = models.URLField(default='', blank=True)
    twitter = models.CharField(max_length=255, default=None, blank=True, null=True)
    employees = models.IntegerField(default=None, blank=True, null=True)
    founded = models.IntegerField(default=0, blank=True)
    email = models.EmailField(default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    overview = models.TextField(default='', blank=True)
    logo = models.ImageField(null=True, default=None, blank=True, upload_to='logo-cache')

    def crunchbase_url(self):
        return u'http://www.crunchbase.com/company/' + self.permalink

    def update(self):
        pass

class CompanyPeople(models.Model):
    company = models.ForeignKey(Company, related_name='people')
    name = models.CharField(max_length=255)
    permalink = models.CharField(max_length=255)
    title = models.CharField(max_length=64)

    def update(self):
        pass
