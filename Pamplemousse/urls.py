from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'Pamplemousse.views.home', name='home'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
     {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include('userprofile.urls')),
)
