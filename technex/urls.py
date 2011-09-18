from django.conf.urls.defaults import *
from technex.app import views
from django.views.generic.simple import direct_to_template
from technex.app.models import College

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'technex.views.home', name='home'),
    # url(r'^technex/', include('technex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.index),
	url(r'^events/$' , views.serialize_to_json),
    url(r'^eventinfo/$' , direct_to_template, {'template': 'eventinfo.html'}),
    url(r'^eventspanel/$' , direct_to_template, {'template': 'eventspanel.html'}),
)
