# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#
# Shared models for aurora project.

from django.db import models
from django.conf import settings

class Photo(models.Model):

    title       = models.CharField(max_length = 255, blank = True)
    description = models.TextField(blank = True) # in reStructuredText form
    datetime    = models.DateTimeField()
    license     = models.ForeignKey('License', default = 1)
    tags        = models.ManyToManyField('Tag', blank = True)
    published   = models.BooleanField(default = True)
    featured    = models.BooleanField(default = False)
    notes       = models.TextField(blank = True)
    uuid        = models.CharField(max_length = 100)

    hush        = models.CharField(max_length = 128) # 128 for sha512 digest
    extension   = models.CharField(max_length = 10)

    height      = models.IntegerField(default=0)
    width       = models.IntegerField(default=0)

    postcard    = models.IntegerField(default=0)

    class Meta:
        ordering = ["-id"]

    def __unicode__(self):
        if len(self.title):
            return "%s" % (self.title)
        else:
            return "Photo %s" % (self.id)

    def description_html(self):
        return self.description # TODO: change to docutils later

    def thumb_height(self):
        return self.height * settings.AURORA_THUMB_WIDTH / self.width

    def set_tags(self, tag_list):
        for tag in self.tags.all():
            self.tags.remove(tag)
        for str_tag in tag_list:
            try:
                tag = Tag.objects.get(title=str_tag)
            except:
                tag = Tag(title=str_tag)
                tag.save()
            self.tags.add(tag)
        self.save()

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
    urlPart     = models.CharField(max_length = 255)
    photos      = models.TextField()    # comma separated id's
