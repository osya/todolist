#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from todos.models import Todo


class addForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'text', 'created_at']
