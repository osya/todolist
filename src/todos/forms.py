#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms


class addForm(forms.Form):
    title = forms.CharField(required=True, max_length=200)
    text = forms.CharField(widget=forms.Textarea)
