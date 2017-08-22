from django.conf.urls import url, include

from todos.views import TodoDetailView, TodoCreateView, TodoListView

urlpatterns = [
    url(r'^(?P<pk>\d+)$', TodoDetailView.as_view(), name='detail'),
    url(r'^create/$', TodoCreateView.as_view(), name='create'),
    url(r'^$', TodoListView.as_view(), name='list'),
]

# TODO: Implement 2FA & update corresponding Cover letter
# TODO: Implement TBA using django-allauth & update corresponding Cover letter
# TODO: Implement dependencies (Bootsrap) installation via Bower or Webpack
# TODO: Add Travis & update corresponding Cover letter
