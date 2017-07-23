from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todos:detail', kwargs={'pk': self.pk})
