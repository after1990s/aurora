#!/usr/bin/env python
# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#
# URL dispatcher for the gallery module of aurora project

from django.conf.urls import patterns, include, url

urlpatterns = patterns('gallery',

    url(r'^$', 'views.homepage'),
    url(r'^photo/(?P<photo_id>\d+)$', 'views.single'),

    url(r'^api/homepage_list/(?P<page>\d+)$', 'views.homepage_imagelist'),
)
