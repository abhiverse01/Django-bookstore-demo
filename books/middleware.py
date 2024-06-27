# books/middleware.py
from django.utils.deprecation import MiddlewareMixin

class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print('Request URL: ', request.path)