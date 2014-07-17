from django.conf.urls import patterns, url, include
from pamplesneak import views

urlpatterns = patterns('',
    url(r'^$', views.pamplesneak, name='pamplesneak'),
)