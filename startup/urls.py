from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

# Pull in class views
from startup.startups.views import *
from startup.events.views import *
from startup.jobs.views import *

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', HomePage.as_view()),
    url(r'^events$', EventsListing.as_view()),
    url(r'^events/import$', FindNewEvents.as_view()),

    url(r'^startups$', Startups.as_view()),
    url(r'^startup/(?P<permalink>.+)$',Startup.as_view()),

    url(r'^jobs$', JobList.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
