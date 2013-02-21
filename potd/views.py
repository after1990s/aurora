# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#

from django.shortcuts import render
from django.conf import settings
from django.http import Http404

from aurora.models import Photo

def homepage(request):
    photos = Photo.objects.filter(published = True, featured = True)[:settings.AURORA_POTD_PAGE_SIZE]
    return render(request, 'potd/homepage.html', {
            'photos': photos,
        }
        )
