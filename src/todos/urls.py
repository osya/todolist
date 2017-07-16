from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Todo
from . import views

urlpatterns = [
    url(r'^todos/(?P<pk>\d+)$', DetailView.as_view(model=Todo, template_name='todos/todo.html')),
    url(r'^add/$', views.add, name='add'),
    url(r'^$', ListView.as_view(queryset=Todo.objects.all().order_by('-created_at')[:10],
                                template_name='todos/todos.html'))
]
