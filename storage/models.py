# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#

from django.db import models

class PhotoStorage(models.Model):

    photo       = models.ForeignKey('aurora.Photo')
    versionStr  = models.CharField(max_length = 20, default = '0', db_index = True)
    hush        = models.CharField(max_length = 128) # 128 for sha512 digest
    extension   = models.CharField(max_length = 10)
    
