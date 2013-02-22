# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#

from django.core.paginator import Paginator
from django.shortcuts import render
from django.conf import settings
from django.http import Http404

from aurora.models import Photo

def homepage(request):
    photos = Photo.objects.filter(published = True)[:settings.AURORA_GALLERY_PAGE_SIZE * 2]
    return render(request, 'gallery/homepage.html', {
            'photos': photos,
        }
        )

def homepage_imagelist(request, page):
    photos_all = Photo.objects.filter(published = True)
    p = Paginator(photos_all, settings.AURORA_GALLERY_PAGE_SIZE)
    try:
        photos = p.page(page)
    except:
        raise Http404

    return render(request, 'gallery/homepage_list.html', {
            'photos': photos,
            }
            )



def single(request, photo_id):
    try:
        photo = Photo.objects.get(published = True, id=photo_id)
    except Photo.DoesNotExist:
        raise Http404
    if not photo.published:
        raise Http404

    return render(request, 'gallery/single.html', {
            'photo': photo,
        }
        )
