# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#
# The special hush (hash) function used to generate storage paths

import hashlib

from django.conf import settings

from models import PhotoStorage

def aurora_hush(photo):
    token = settings.AURORA_HUSH_SALT + photo.uuid
    return hashlib.sha512(token).hexdigest()[:settings.AURORA_HUSH_LENGTH]

