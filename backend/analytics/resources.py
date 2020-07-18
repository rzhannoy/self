from django.conf.urls import url

from tastypie import fields
from tastypie.authentication import Authentication
from tastypie.utils import trailing_slash

from backend.resources import BaseResource
from backend.auth import BaseAuthorization

from .models import Hit


class HitResource(BaseResource):
    post_id = fields.IntegerField('post_id', null=True, blank=True)

    class Meta:
        queryset = Hit.objects.all()
        allowed_methods = []
        resource_name = 'hit'
        authentication = Authentication()
        authorization = BaseAuthorization()
        fields = ['type']

    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>{})/record{}$'.format(self._meta.resource_name, trailing_slash()), self.wrap_view('record'), name='api_record'),
        ]

    def record(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        meta = request.META
        data = self.deserialize(request, request.body)

        Hit.objects.record(**{
            'type_': data['type'],
            'ua': meta.get('HTTP_USER_AGENT', ''),
            'ip': meta.get('REMOTE_ADDR', ''),
            'post_id': data.get('post_id'),
        })

        return self.create_response(request, {'success': True})
