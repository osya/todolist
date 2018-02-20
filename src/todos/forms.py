#!/usr/bin/env python
# -*- coding: utf-8 -*-
from crispy_forms.bootstrap import FieldWithButtons, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Field, Layout, Submit
from django import forms
from django.urls import reverse
from django_markdown.widgets import MarkdownWidget
from taggit_selectize.widgets import TagSelectize

from todos.models import Todo


class SearchForm(forms.Form):
    query = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_action = reverse('todos:list')
        self.helper.form_class = 'navbar-form navbar-left'
        self.helper.attrs = {'role': 'search'}
        self.helper.form_method = 'GET'
        self.helper.layout = Layout(FieldWithButtons(Field('query', autofocus='autofocus'), Submit('', 'Search')))


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = (
            'title',
            'text',
            'tags',
        )
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
                HTML('<a href="{% url "todos:list" %}{% query_builder request %}">Go Back</a>')))
