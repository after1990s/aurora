# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#

from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')
