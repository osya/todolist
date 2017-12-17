#!/usr/bin/env python
# -*- coding: utf-8 -*-
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, Submit
from django import forms
from django_markdown.widgets import MarkdownWidget
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
            FormActions(
                Submit('create', 'Create'),
                HTML('<a href="{% url "todos:list" %}{% query_builder request %}">Go Back</a>')
            )
        )
