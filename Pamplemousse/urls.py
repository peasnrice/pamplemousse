from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'Pamplemousse.views.home', name='home'),
    (r'^pampleaccounts/logout/$', 'django.contrib.auth.views.logout',
     {'next_page': '/'}),
    url(r'^favicon\.ico$', RedirectView.as_view(url='static/assets/ico/favicon.ico')),
    url(r'^accounts/', include('allauth.urls')), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pampleprofile/', include('userprofile.urls')),
    url(r'^pamplesneak/', include('pamplesneak.urls')),
    url(r'^pamplegames/', include('pamplegames.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)
