#!/usr/bin/env python
# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#
# URL dispatcher for the potd module of aurora project

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'potd.views.potd_homepage'),

)
