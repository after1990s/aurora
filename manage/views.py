# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#

from django.shortcuts import render

from login import login_required

@login_required
def homepage(request):
    return render(request, 'manage/homepage.html', {
            'page_title': 'Home',
            'NAV_HOME_CLASS': 'active',
        }
        )
