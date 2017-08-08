from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)$', views.TodoDetailView.as_view(), name='detail'),
    url(r'^create/$', views.TodoCreateView.as_view(), name='create'),
    url(r'^$', views.TodoListView.as_view(), name='list'),
    url(r'^accounts/', include('allauth.urls')),
]

# TODO: Implement 2FA & update corresponding Cover letter
# TODO: Implement TBA using django-allauth & update corresponding Cover letter
# TODO: Implement dependencies (Bootsrap) installation via Bower or Webpack
