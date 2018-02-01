#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'user')

    user = PrimaryKeyRelatedField(read_only=True, source='user.username')
