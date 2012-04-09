import urllib2
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from startups.models import Company, CompanyPeople
from crunchbase import getCompany

# Given a permalink to a company, attempt to create a version in our database
def createCompany(permalink):
    cb = getCompany(permalink)

    c = Company()

    c.name = cb[u'name']
    c.permalink = cb[u'permalink']
    c.homepage = cb[u'homepage_url']
    c.blog = cb[u'blog_url']
    c.twitter = cb[u'twitter_username']

    c.employees = cb[u'number_of_employees']
    c.founded = cb[u'founded_year']

    c.email = cb[u'email_address']
    c.phone = cb[u'phone_number']

    c.overview = cb[u'overview']

    # Download logo, store it.


    try:
        logo_url = u'http://www.crunchbase.com/' + cb[u'image'][u'available_sizes'][0][1]

        img_temp = NamedTemporaryFile()
        img_temp.write(urllib2.urlopen(logo_url).read())
        img_temp.flush()

        c.logo.save(permalink + '.jpg', File(img_temp))

    except:
        pass

    c.save()

    # Save the people
    for p in cb[u'relationships']:
        if not p[u'is_past']:
            cp = CompanyPeople()
            cp.company = c
            cp.title = p[u'title']
            cp.name = ' '.join([p[u'person'][u'first_name'], p[u'person'][u'last_name']])
            cp.permalink = p[u'person'][u'permalink']

            cp.save()

from django.conf import settings
import os
import re
from csv import DictReader
def runImport(filename):
    import_folder = os.path.join(settings.PROJECT_PATH, 'startups/imports/')

    file = open(os.path.join(import_folder, filename))
    data = DictReader(file)

    for company in data:
        if str(company.get('CrunchBase')) is not '':
            cbase = str(company.get('CrunchBase'))
            res = re.search(r'http:\/\/www.crunchbase.com\/company\/(.+)', cbase)

            if res is not None:
                perma = res.group(1)

                if len(Company.objects.filter(permalink=perma)) < 1:
                    createCompany(perma)