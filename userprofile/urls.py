__author__ = 'Monique Tucker'

from django.conf.urls import patterns, include, url

from userprofile import views

urlpatterns = patterns('',
    url(r'^$', views.user_profile, name='userprofile'),
    # url(r'^$', views.list_api, name='list_api'),

)