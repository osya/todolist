from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from precise_bbcode.fields import BBCodeTextField
from taggit_selectize.managers import TaggableManager


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = BBCodeTextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    tags = TaggableManager(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todos:detail', kwargs={'pk': self.pk})
