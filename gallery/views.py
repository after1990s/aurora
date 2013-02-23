# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#

from django.core.paginator import Paginator
from django.shortcuts import render
from django.conf import settings
from django.http import Http404, HttpResponse

from aurora.models import Photo
from postcard.models import PostcardRequest
from forms import PostcardRequestForm

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
        return HttpResponse('')

    return render(request, 'gallery/homepage_list.html', {
            'photos': photos,
            }
            )

def single(request, photo_id):
    try:
        photo = Photo.objects.get(published=True, id=photo_id)
    except Photo.DoesNotExist:
        raise Http404
    if not photo.published:
        raise Http404

    return render(request, 'gallery/single.html', {
            'photo': photo,
        }
        )

def postcard(request, photo_id):
    try:
        photo = Photo.objects.get(published=True, id=photo_id)
    except Photo.DoesNotExist:
        raise Http404
    if not photo.published:
        raise Http404
    if not photo.postcard > 0:
        raise Http404

    if request.method != 'POST':
        form = PostcardRequestForm()
        form.photo = photo
        return render(request, 'gallery/postcard_form.html', {
                'form': form,
                'photo': photo,
            }
            )
    else:
        form = PostcardRequestForm(request.POST)
        if form.is_valid():
            pr = PostcardRequest()
            pr.photo = photo
            pr.name = form.cleaned_data["name"]
            pr.address = form.cleaned_data["address"]
            pr.contact = form.cleaned_data["contact"]
            pr.comment = form.cleaned_data["comment"]
            pr.save()
            
            photo.postcard = photo.postcard - 1
            photo.save()
            return render(request, 'gallery/postcard_succ.html', {
                    'form': form,
                    'photo': photo,
                }
                )
        return render(request, 'gallery/postcard_form.html', {
                'form': form,
                'photo': photo,
            }
            )
