from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'Pamplemousse.views.home', name='home'),
    (r'^pampleaccounts/logout/$', 'django.contrib.auth.views.logout',
     {'next_page': '/'}),
    url(r'^pampleaccounts/', include('allauth.urls')), 
    url(r'^pampleadmin/', include(admin.site.urls)),
    url(r'^pampleprofile/', include('userprofile.urls')),
    url(r'^pamplesneak/', include('pamplesneak.urls')),
    url(r'^pamplegames/', include('pamplegames.urls')),
)
