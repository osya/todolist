# pylint: disable=C0103
# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 17:29
from __future__ import unicode_literals

from django.db import migrations

import taggit_selectize.managers


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0009_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='tags',
            field=taggit_selectize.managers.TaggableManager(
                blank=True,
                help_text='A comma-separated list of tags.',
                through='taggit.TaggedItem',
                to='taggit.Tag',
                verbose_name='Tags'),
        ),
    ]
