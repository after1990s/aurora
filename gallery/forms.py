# -*- coding: utf8 -*-
# Copyright 2013 by Weisi Dai <multiple1902@gmail.com>
# Released under MIT License
#

from django import forms

from postcard.models import PostcardRequest

class PostcardRequestForm(forms.ModelForm):

    name = forms.CharField(
                required=False,
                label='',
                widget=forms.TextInput(attrs={'class': 'input-block-level',
                                              'placeholder': '我叫 ...',
    }))
    address = forms.CharField(
                required=True,
                label='',
                widget=forms.Textarea(attrs={'class': 'input-block-level',
                                             'rows': '2',
                                             'placeholder': '我的郵政地址是 ... （必填）',
    }))
    contact = forms.CharField(
                required=False,
                label='',
                widget=forms.TextInput(attrs={'class': 'input-block-level',
                                              'placeholder': '我的電話或者郵箱是 ...',
    }))
    comment = forms.CharField(
                required=False,
                label='',
                widget=forms.TextInput(attrs={'class': 'input-block-level',
                                              'placeholder': '還有要補充的 ...',
    }))
    

    class Meta:
        model = PostcardRequest
        fields = ['name', 'address', 'contact', 'comment']
