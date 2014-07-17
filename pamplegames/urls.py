from django.conf.urls import patterns, url, include
from pamplegames import views

urlpatterns = patterns('',
    url(r'^$', views.pamplegames, name='pamplegames'),
)