from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from userprofile.models import UserProfile

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['id','username']
        allowed_methods = ['get']

class UserProfileResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'userprofile'