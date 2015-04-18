from django.conf.urls import patterns, include, url
from django.contrib import admin


# admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simply_good_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # from exercise: url(r'^$', 'signups.views.home', name='home'),
    #for signups
    # url(r'^$', include('signups.urls', namespace='signups')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'simply_good_django.views.home', name='home'),

    #urls for registering
    url(r'^register/$', 'simply_good_django.views.register', name='register'),
    url(r'^register_success/$', 'simply_good_django.views.register_success', name='register_success'),
    # url(r'^register_error/$', 'simply_good_django.views.register_error', name='register_error'),

    # authentication urls
    url(r'^login/$', 'simply_good_django.views.login', name='login'),
    url(r'^authenticate/$', 'simply_good_django.views.authenticate', name='authenticate'),
    url(r'^logout/$', 'simply_good_django.views.logout', name='logout'),
    url(r'^login_success/$', 'simply_good_django.views.login_success', name='login_success'),
    url(r'^login_invalid/$', 'simply_good_django.views.login_invalid', name='login_invalid'),

    #for users
    url(r'^profile/', include('userprofile.urls')),
    url(r'^diary/', include('diary.urls')),
)
