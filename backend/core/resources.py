from django.conf.urls import url

from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.utils import trailing_slash

from backend.resources import BaseResource
from backend.auth import DetailCreateAuthorization, BaseAuthorization

from .models import Message, Post, Subscriber


class MessageResource(BaseResource):
    class Meta:
        queryset = Message.objects.all()
        allowed_methods = ['post']
        resource_name = 'message'
        authentication = Authentication()
        authorization = DetailCreateAuthorization()
        excludes = ['is_processed']


class PostResource(BaseResource):
    class Meta:
        queryset = Post.objects.filter(is_hidden=False)
        allowed_methods = ['get']
        resource_name = 'post'
        detail_uri_name = 'slug'
        authentication = Authentication()
        authorization = Authorization()
        excludes = ['is_hidden']

    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>{})/(?P<slug>.+){}$'.format(self._meta.resource_name, trailing_slash()), self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
        ]


class SubscriberResource(BaseResource):
    class Meta:
        queryset = Subscriber.objects.all()
        allowed_methods = []
        resource_name = 'subscriber'
        authentication = Authentication()
        authorization = BaseAuthorization()
        fields = ['name', 'email']

    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>{})/register{}$'.format(self._meta.resource_name, trailing_slash()), self.wrap_view('register'), name='api_register'),
            url(r'^(?P<resource_name>{})/confirm{}$'.format(self._meta.resource_name, trailing_slash()), self.wrap_view('confirm'), name='api_confirm'),
        ]

    def register(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        data = self.deserialize(request, request.body)
        resp = Subscriber.objects.register(data)

        return self.create_response(request, resp)

    def confirm(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        data = self.deserialize(request, request.body)
        resp = Subscriber.objects.confirm(data)

        return self.create_response(request, resp)
