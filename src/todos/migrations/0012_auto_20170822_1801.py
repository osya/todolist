# pylint: disable=C0103
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-22 15:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0011_auto_20170821_1924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ('-created_at', )},
        ),
    ]
