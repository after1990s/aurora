# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#
from django import forms

from aurora.models import Photo, License, Tag

class LoginForm(forms.Form):
    Password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'password',
            'class': 'input-block-level',
        }
    ), label='')


class PhotoForm(forms.Form):
    title = forms.CharField(
                max_length=255, 
                required=False,
                widget=forms.TextInput(attrs={'class': 'input-block-level',
    }))
    description = forms.CharField(
                      max_length=255, 
                      required=False,
                      widget=forms.Textarea(
                                 attrs={'class': 'input-block-level',
                                        'rows': '2',
    }))
    license = forms.ModelChoiceField(
                  required=True,
                  queryset=License.objects.all(),
                  initial=License.objects.get(id=1),
                  widget=forms.Select(
                             attrs={'class': 'input-block-level',
                                    'rows': '2',
    }))
    published = forms.BooleanField(
                    initial=True,
                    required=False,
    )
    featured = forms.BooleanField(
                    initial=False,
                    required=False,
    )
    photo = forms.ImageField()
    notes = forms.CharField(
                required=False,
                widget=forms.Textarea(
                           attrs={'class': 'input-block-level',
                                  'rows': '2',
    }))
    postcard = forms.IntegerField(
                   initial=0,
                   required=True,
                   widget=forms.TextInput(attrs={'class': 'input-block-level',
    }))


class EditPhotoForm(PhotoForm):
    photo = forms.ImageField(required = False)
