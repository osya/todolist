# pylint: disable=C0103
# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 21:17
from __future__ import unicode_literals

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_auto_20170715_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 8, 3, 0, 17, 32, 880478)),
        ),
    ]
