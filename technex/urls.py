from django.conf.urls.defaults import *
from technex.app import views
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail
from technex.app.models import College

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

college_name = College.objects.all()

college_info = {
    'queryset': college_name,
    'template_name': 'index.html',
}


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
    url(r'^home/$', list_detail.object_list, college_info),
	url(r'^events/$' , views.serialize_to_json),
    url(r'^eventinfo/$' , direct_to_template, {'template': 'eventinfo.html'}),
    url(r'^eventspanel/$' , direct_to_template, {'template': 'eventspanel.html'}),
)
