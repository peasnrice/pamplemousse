from tastypie.resources import ModelResource
from pamplesneak.models import Pamplesneak

class PamplesneakResource(ModelResource):
    class Meta:
        queryset = Pamplesneak.objects.all()
        resource_name = 'pamplesneak'