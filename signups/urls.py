from django.conf.urls import patterns, url

from signups import views

urlpatterns = patterns('',
    url(r'^$', 'signups.views.home', name='home'),
)



