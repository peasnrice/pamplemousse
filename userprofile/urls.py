from django.conf.urls import patterns, url, include
from userprofile import views
from tastypie.api import Api
from userprofile.api import UserProfileResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(UserProfileResource())

urlpatterns = patterns('',
    url(r'^$', views.user_profile, name='userprofile'),
    (r'^api/', include(v1_api.urls)),
)