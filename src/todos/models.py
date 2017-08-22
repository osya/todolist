from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django_markdown.models import MarkdownField
from taggit_selectize.managers import TaggableManager


class TodoQuerySet(models.QuerySet):
    def list(self, query_dict={}):
        queryset = self.order_by('-created_at')
        tags = query_dict.get('tags')
        if tags:
            tags = tags.split(',')
            queryset = queryset.filter(tags__name__in=tags).distinct()
        q = query_dict.get('q')
        if q:
            queryset = queryset.filter(
                    Q(title__icontains=q) |
                    Q(text__icontains=q)).distinct()
        return queryset


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = MarkdownField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    tags = TaggableManager(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)

    objects = TodoQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todos:detail', kwargs={'pk': self.pk})
