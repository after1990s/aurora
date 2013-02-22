# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

from storage.api import create_new_photo_storage

from aurora.models import Photo, License, Tag

from login import login_required
from forms import PhotoForm, EditPhotoForm

import datetime
import uuid
import os

@login_required
def photo_all(request, page="1"):
    photo_list = Photo.objects.all()
    paginator = Paginator(photo_list, settings.AURORA_MANAGE_PAGE_SIZE)
    try:
        photos = paginator.page(page)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    return _photo_list(request, photos, '/photo')

def _photo_list(request, photos, url_prefix):

    return render(request, 'manage/photo-list.html', {
            'NAV_PHOTO_CLASS': 'active',
            'photos': photos,
            'url_prefix': url_prefix,
        })

@login_required
def photo_add(request):
    form = PhotoForm()
    errmsg = ""
    succ = False
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            p = Photo()
            p.title = form.cleaned_data['title']
            p.description = form.cleaned_data['description']
            p.datetime = datetime.datetime.now()
            p.uuid = str(uuid.uuid4())
            p.license = form.cleaned_data['license']
            p.published = form.cleaned_data['published']
            p.featured = form.cleaned_data['featured']
            p.extension = os.path.splitext(form.cleaned_data['photo'].name)[1][1:]
            p.save()

            p.set_tags(request.POST.getlist('tags'))

            create_new_photo_storage(photo=p, 
                f=request.FILES['photo'])
            
            succ = p.id

        else:
            errmsg = form.errors

    return render(request, 'manage/photo-add.html', {
            'NAV_PHOTO_CLASS': 'active',
            'form': form,
            'errmsg': errmsg,
            'succ': succ,
            'all_tags': get_all_tags(),
        }
        )

@login_required
def photo_edit(request, photo_id):
    print "POST: %s" % request.POST
    photo = Photo.objects.get(id=photo_id)
    form = EditPhotoForm()
    errmsg = ""
    succ = False
    if request.method == "POST":
        form = EditPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            p = photo
            p.title = form.cleaned_data['title']
            p.description = form.cleaned_data['description']
            p.datetime = datetime.datetime.now()
            p.uuid = str(uuid.uuid4())
            p.license = form.cleaned_data['license']
            p.published = form.cleaned_data['published']
            p.featured = form.cleaned_data['featured']
            p.save()

            p.set_tags(request.POST.getlist('tags'))

            if 'photo' in request.FILES.keys():
                p.extension = os.path.splitext(form.cleaned_data['photo'].name)[1][1:]
                create_new_photo_storage(photo=p, 
                    f=request.FILES['photo'])
            
            succ = p.id

        else:
            errmsg = form.errors
    else:
        form.fields["title"].initial = photo.title
        form.fields["description"].initial = photo.description
        form.fields["license"].initial = photo.license
        form.fields["published"].initial = photo.published
        form.fields["featured"].initial = photo.featured
    

    return render(request, 'manage/photo-edit.html', {
            'NAV_PHOTO_CLASS': 'active',
            'form': form,
            'errmsg': errmsg,
            'succ': succ,
            'tags': photo.tags.all(),
            'all_tags': get_all_tags(),
        }
        )

def get_all_tags():
    tags = Tag.objects.all()
    str_tags = map(lambda x: '"%s"' % x, tags)
    return ", ".join(str_tags)
