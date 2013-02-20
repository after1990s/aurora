#!/usr/bin/env python
# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#
# Template context processors for the front-end of aurora project

from django.conf import settings

def site(request):
    return {
            'AURORA_SITE_NAME': settings.AURORA_SITE_NAME,
            'AURORA_GALLERY_URL': settings.AURORA_GALLERY_URL,
            'AURORA_MEDIA_PUB_URL': settings.AURORA_MEDIA_PUB_URL,

            'AURORA_POSTFIX_POTD': settings.AURORA_POSTFIX_POTD,
            'AURORA_POSTFIX_GALLERY_THUMB': settings.AURORA_POSTFIX_GALLERY_THUMB,
            'AURORA_POSTFIX_GALLERY_DISPLAY': settings.AURORA_POSTFIX_GALLERY_DISPLAY,
            'AURORA_THUMB_WIDTH': settings.AURORA_THUMB_WIDTH,

            'AURORA_FOOTER': settings.AURORA_FOOTER,
            'AURORA_GA_POTD': settings.AURORA_GA_POTD,
            'AURORA_GA_GALLERY': settings.AURORA_GA_GALLERY,
           }
