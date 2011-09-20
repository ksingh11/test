from django.conf.urls.defaults import *
from technex.app import views
from django.views.generic.simple import redirect_to, direct_to_template
from django.contrib.auth.views import login, logout, password_reset, password_reset_confirm,\
    password_reset_done, password_change, password_change_done, password_reset_complete
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
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/profile/$', redirect_to, {'url': '/'}),
    url(r'^accounts/password/$', redirect_to, {'url': '/'}),
    url(r'^accounts/password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm),
    url(r'^accounts/password/reset/complete/$', password_reset_complete),
    url(r'^accounts/password/reset/$', password_reset),
    url(r'^accounts/password/reset/done/$', password_reset_done),
    url(r'^accounts/password/change/$', password_change),
    url(r'^accounts/password/change/done/$', password_change_done),
)
