from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

# Pull in class views
from StartupCincy.pages.views import *

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', HomePage.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
