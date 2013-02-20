#!/usr/bin/env python
# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#
# URL dispatcher for the manage module of aurora project

from django.conf.urls import patterns, include, url

urlpatterns = patterns('manage',

    url(r'^$', 'views.homepage'),

    url(r'^photo$', 'photo.photo_all'),
    url(r'^photo/page/(?P<page>\d+)$', 'photo.photo_all'),

    url(r'^photo/add$', 'photo.photo_add'),
    url(r'^photo/edit/(?P<photo_id>\d+)$', 'photo.photo_edit'),

    url(r'^login$', 'login.login'),

)
