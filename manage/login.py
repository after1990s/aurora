# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#
# Access control for the manage module of aurora project

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.conf import settings

from forms import LoginForm

AUTHENTICATED_COOKIE = 'aurora_authenticated'
ILLEGAL_ACCESS = HttpResponseRedirect('http://www.people.com.cn/')
LOGIN_PAGE = HttpResponseRedirect('/login')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print "T: %s, S: %s" % (settings.AURORA_PASSWORD, form['Password'].value())
        if settings.AURORA_PASSWORD == form['Password'].value():
            request.session[AUTHENTICATED_COOKIE] = True
            return HttpResponseRedirect('/')
        else:
            return ILLEGAL_ACCESS

    form = LoginForm()
    return render(request, 'manage/login.html', {
        'form': form,
        })

def login_required(f):
    def wrap(request, *args, **kwargs):
        if AUTHENTICATED_COOKIE not in request.session.keys():
            return LOGIN_PAGE
        return f(request, *args, **kwargs)
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap



