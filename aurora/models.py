# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#
# Models for aurora project.

from django.db import models
from django.conf import settings

class Photo(models.Model):

    title       = models.CharField(max_length = 255, blank = True)
    description = models.TextField(blank = True)
    datetime    = models.DateTimeField()
    license     = models.ForeignKey('License', default = 1)
    tags        = models.ManyToManyField('Tag', blank = True)
    #defaultImage= models.ForeignKey('storage.PhotoStorage')
    published   = models.BooleanField(default = True)
    featured    = models.BooleanField(default = False)
    notes       = models.TextField(blank = True)
    uuid        = models.CharField(max_length = 100)

    def __unicode__(self):
        if len(self.title):
            return "%s" % (self.title)
        else
            return "Photo %s" % (self.id)

class License(models.Model):

    title       = models.CharField(max_length = 100)
    url         = models.CharField(max_length = 255, blank = True)

    def __unicode__(self):
        return "%s" % (self.title)

class Tag(models.Model):

    title       = models.CharField(max_length = 255)

    def __unicode__(self):
        return "%s" % (self.title)

class Collection(models.Model):

    title       = models.CharField(max_length = 255)
    photos      = models.TextField()    # comma separated id's

admin.site.register(Photo)
admin.site.register(License)
admin.site.register(Tag)
admin.site.register(Collection)

