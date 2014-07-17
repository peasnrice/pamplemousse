from django.conf.urls import patterns, url, include
from pamplesneak import views

urlpatterns = patterns('',
    url(r'^$', views.pamplesneak, name='pamplesneak'),
    url(r'^pampleplay/$', views.pampleplay, name='pampleplay'),
    url(r'^pampleref/$', views.pampleref, name='pampleref'),
    url(r'^pamplewatch/$', views.pamplewatch, name='pamplewatch'),
    url(r'^pampleplay/create$', views.creategame, name='creategame'),
    url(r'^pampleplay/(?P<game_id>\d+)/$', views.joingame, name='joingame'),
)