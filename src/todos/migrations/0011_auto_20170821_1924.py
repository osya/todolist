# pylint: disable=C0103
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-21 16:24
from __future__ import unicode_literals

from django.db import migrations

import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0010_auto_20170811_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='_text_rendered',
        ),
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
