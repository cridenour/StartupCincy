from django.db import models

import urllib2
from crunchbase import getCompany
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

class Company(models.Model):
    name = models.CharField(max_length=255)
    permalink = models.CharField(max_length=255, default='', blank=True, unique=True)
    homepage = models.URLField(default='', blank=True, null=True)
    blog = models.URLField(default='', blank=True, null=True)
    twitter = models.CharField(max_length=255, default=None, blank=True, null=True)
    employees = models.IntegerField(default=None, blank=True, null=True)
    founded = models.IntegerField(default=0, blank=True, null=True)
    email = models.EmailField(default='', blank=True, null=True)
    phone = models.CharField(max_length=20, default='', blank=True, null=True)
    overview = models.TextField(default='', blank=True, null=True)
    logo = models.ImageField(null=True, default=None, blank=True, upload_to='logo-cache')

    def crunchbase_url(self):
        return u'http://www.crunchbase.com/company/' + self.permalink

    def update(self):
        cb = getCompany(self.permalink)

        self.name = cb[u'name']
        self.permalink = cb[u'permalink']
        self.homepage = cb[u'homepage_url']
        self.blog = cb[u'blog_url']
        self.twitter = cb[u'twitter_username']

        self.employees = cb[u'number_of_employees']
        self.founded = cb[u'founded_year']

        self.email = cb[u'email_address']
        self.phone = cb[u'phone_number']

        self.overview = cb[u'overview']

        # Download logo, store it.
        logo_url = u'http://www.crunchbase.com/' + cb[u'image'][u'available_sizes'][0][1]

        img_temp = NamedTemporaryFile()
        img_temp.write(urllib2.urlopen(logo_url).read())
        img_temp.flush()

        self.logo.save(self.permalink + '.jpg', File(img_temp))

        self.save()

    def __unicode__(self):
        return "%s" % self.name

    def get_permalink(self):
        return "/startup/%s" % self.permalink

    class Meta:
        verbose_name_plural = "Companies"

class CompanyPeople(models.Model):
    company = models.ForeignKey(Company, related_name='people')
    name = models.CharField(max_length=255)
    permalink = models.CharField(max_length=255)
    title = models.CharField(max_length=64)

    def update(self):
        pass

    def __unicode__(self):
        return "%s - %s" % (self.name, self.title)

    class Meta:
        verbose_name_plural = "Key Company People"