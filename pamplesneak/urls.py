from django.conf.urls import patterns, url, include
from pamplesneak import views
from pamplesneak.api import PamplesneakResource
pamplesneak_resource = PamplesneakResource()

urlpatterns = patterns('',
    url(r'^$', views.pamplesneak, name='pamplesneak'),
    url(r'^pampleplay/$', views.pampleplay, name='pampleplay'),
    url(r'^pampleref/$', views.pampleref, name='pampleref'),
    url(r'^pamplewatch/$', views.pamplewatch, name='pamplewatch'),
    url(r'^pampleplay/create$', views.creategame, name='creategame'),
    url(r'^pampleplay/(?P<game_id>\d+)/(?P<slug>[-\w\d]+)/$', views.joingame, name='joingame'),
    (r'^api/', include(pamplesneak_resource.urls)),
)