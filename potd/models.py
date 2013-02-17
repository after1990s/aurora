# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#

from django.db import models

class potd(models.Model):

    photo   = models.ForeignKey('aurora.Photo')
    date    = models.DateField(auto_now_add = True)

    def __unicode__(self):

        if len(self.photo.title):
            return 'POTD on %s (%s)' % (self.date, self.photo.title)
        else:
            return 'POTD on %s (%s)' % (self.date, self.photo.id)
