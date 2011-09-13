from django.conf.urls.defaults import *
from technex.app import views
from django.views.generic.simple import direct_to_template

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
    url(r'^register/$', views.register),
	url(r'^home$', views.home),
	url(r'^$', direct_to_template, {'template': 'index.html'}),
	url(r'^robotics$', direct_to_template, {'template': 'robotics.html'}),
	url(r'^workshops$', direct_to_template, {'template': 'workshops.html'}),
	url(r'^extreme_engg$', direct_to_template, {'template': 'extreme_engg.html'}),
	url(r'^modex"$', direct_to_template, {'template': 'modex.html'}),
)
