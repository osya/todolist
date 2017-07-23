from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Todo
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)$', views.TodoDetailView.as_view(), name='detail'),
    url(r'^create/$', views.TodoCreateView.as_view(), name='create'),
    url(r'^$', views.TodoListView.as_view(), name='list')
]
