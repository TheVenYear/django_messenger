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
        response = Response({'data': None, 'messages': base_response.data})
        response['messages'] = base_response.data

    return response


class ApiRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = {
            'error': False,
            'message': 'Success',
            'data': data
        }

        return super(ApiRenderer, self).render(response, accepted_media_type, renderer_context)


class ResponseCustomMiddleware(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
        super(ResponseCustomMiddleware, self).__init__(*args, **kwargs)

    def process_template_response(self, request, response):
        if not response.is_rendered and isinstance(response, Response):
            if isinstance(response.data, dict):
                message = response.data.get('messages', None)
                if 'data' not in response.data:
                    response.data = {'data': response.data}
                response.data.setdefault('messages', message)

                response.data.setdefault('status_code', response.status_code)
        return response
