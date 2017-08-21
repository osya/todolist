#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django_markdown.widgets import MarkdownWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from taggit_selectize.widgets import TagSelectize

from todos.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'text', 'tags',)
        widgets = {
            'tags': TagSelectize(),
            'test': MarkdownWidget,
        }

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                'title', 'text', 'tags',
                ButtonHolder(
                        Submit('create', 'Create', css_class='btn btn-default')
                )
        )
