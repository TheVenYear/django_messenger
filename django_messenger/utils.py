from django.utils.deprecation import MiddlewareMixin
from rest_framework.renderers import BaseRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    base_response = exception_handler(exc, context)
    response = None
    # Now add the HTTP status code to the response.
    if base_response is not None:
        response = Response(data={'__context': {'messages': base_response.data}}, status=base_response.status_code)

    return response


class ApiRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = {
            'messages': None,
            'data': None,
            'status_code': None
        }

        if renderer_context is not None:
            response['status_code'] = renderer_context['response'].status_code
            try:
                context = renderer_context['response'].data['__context']
                response['messages'] = context['messages']
                renderer_context['response'].status_code = 200
            except (TypeError, KeyError):
                response['data'] = data

        return super(ApiRenderer, self).render(response, accepted_media_type, renderer_context)
