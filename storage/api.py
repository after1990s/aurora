# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#
# API for storage module of aurora project

from django.conf import settings

from aurora.models import Photo
from hush import aurora_hush

from PIL import Image
import os

def create_new_photo_storage(photo, f):
    photo.extension = photo.extension.lower()
    dir_ = '%s/%s' % (settings.MEDIA_ROOT, photo.id)
    path_ = '%s/%s.%s' % (settings.MEDIA_ROOT, photo.id, photo.extension)
    if not os.path.isdir(dir_):
        os.makedirs(dir_)

    dst = open(path_, 'wb+')
    for chunk in f.chunks():
        dst.write(chunk)
    dst.close()

    try:
        photo.datetime = Image.open(path_)._getexif()[36867].replace(':','-', 2)
    except:
        pass

    photo.hush = aurora_hush(photo)
    photo.width, photo.height = Image.open(path_).size
    photo.save()

    make_symlink_photo(photo)
    return True

def make_symlink_photo(photo):
    dir_ = '%s' % (settings.AURORA_MEDIA_PUB_ROOT)
    photo_path = '%s/%s.%s' % (settings.AURORA_MEDIA_ROOT_REF, 
                                  photo.id, 
                                  photo.extension.lower())
    symlink_path = '%s/%s.%s' % (settings.AURORA_MEDIA_PUB_ROOT, 
                                 photo.hush, 
                                 photo.extension.lower())
    if not os.path.isdir(dir_):
        os.makedirs(dir_)

    os.symlink(photo_path, symlink_path)
    try: # TODO: change to if-else
        pass
    except:
        pass

