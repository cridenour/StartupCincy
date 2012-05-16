from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

# Pull in class views
from startup.startups.views import *
from startup.events.views import *
from startup.jobs.views import *
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', HomePage.as_view()),
    url(r'^events$', EventsListing.as_view()),
    url(r'^events/import$', FindNewEvents.as_view()),
    url(r'^events/add$', TemplateView.as_view(template_name='events_add.html')),

    url(r'^startups$', Startups.as_view()),
    url(r'^startups/add$', TemplateView.as_view(template_name='startups_add.html')),
    url(r'^startup/(?P<permalink>.+)$',Startup.as_view()),

    url(r'^jobs$', JobList.as_view()),
    url(r'^jobs/add$', TemplateView.as_view(template_name='jobs_add.html')),
    url(r'^job/(?P<id>\d+)$',JobDetail.as_view()),

    url(r'^about$', TemplateView.as_view(template_name='about.html')),

    url(r'^email-test', TemplateView.as_view(template_name='email.html')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
