# pylint: disable=C0103
# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 19:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 15, 22, 45, 18, 412538)),
        ),
    ]
