# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#
# URL dispatcher middleware for aurora project.

from django.conf import settings
from django.utils.cache import patch_vary_headers

AURORA_URLS_MAPPING = {
    'AURORA_POTD': 'potd.urls',
    'AURORA_GALLERY': 'gallery.urls',
}

class AuroraAppDispatcherMiddleware:

    def process_request(self, request):
        try:
            module = request.META["HTTP_X_AURORA_MODULE"]
            request.urlconf = AURORA_URLS_MAPPING[module]
        except KeyError:
            pass

    def process_response(self, request, response):
        if getattr(request, "urlconf", None):
            patch_vary_headers(response, ["HTTP_X_AURORA_MODULE"])
        return response
