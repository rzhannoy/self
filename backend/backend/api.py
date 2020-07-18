from tastypie.api import Api as TastypieApi
from tastypie.http import HttpForbidden

from analytics.resources import HitResource
from core.resources import MessageResource, PostResource, SubscriberResource


class Api(TastypieApi):
    def top_level(self, request, api_name=None):
        return HttpForbidden()


api = Api(api_name='api')

api.register(HitResource())
api.register(MessageResource())
api.register(PostResource())
api.register(SubscriberResource())
