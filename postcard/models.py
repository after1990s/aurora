# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#

from django.db import models
    
class PostcardRequest(models.Model):

    photo       = models.ForeignKey('aurora.Photo')
    name        = models.TextField(blank = True)
    address     = models.TextField()
    contact     = models.TextField(blank = True)
    comment     = models.TextField(blank = True)
    sent        = models.BooleanField(default = False)

