# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#

from django.contrib import admin
from aurora.models import Photo, License, Tag, Collection

admin.site.register(Photo)
admin.site.register(License)
admin.site.register(Tag)
admin.site.register(Collection)

