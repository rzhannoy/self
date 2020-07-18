from tastypie import http
from tastypie.resources import ModelResource
from tastypie.exceptions import ImmediateHttpResponse


class BaseResource(ModelResource):
    def get_schema(self, request, **kwargs):
        return http.HttpForbidden()

    def raise_error(self, request, message='invalid_request'):
        raise ImmediateHttpResponse(self.create_response(request, {
            'message': message,
        }, http.HttpBadRequest))

    def serialize_obj(self, request, obj, extra_data=None, **kwargs):
        bundle = self.build_bundle(obj=obj, request=request)

        if extra_data:
            bundle.data.update(extra_data)

        return self.full_dehydrate(bundle, **kwargs)

    def serialize_collection(self, request, collection):
        serialized = []
        for obj in collection:
            serialized.append(self.serialize_obj(request, obj, for_list=True))

        return serialized

    @property
    def model_class(self):
        return self._meta.object_class.__name__
