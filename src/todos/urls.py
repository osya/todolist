from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from todos.views import TodoCreate, TodoDetail, TodoDetailApi, TodoList, TodoListApi

api_patterns = [
    url(r'^$', TodoListApi.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', TodoDetailApi.as_view(), name='detail'),
]

urlpatterns = [
    url(r'^$', TodoList.as_view(), name='list'),
    url(r'^api/', include(api_patterns, namespace='api')),
    url(r'^(?P<pk>\d+)$', TodoDetail.as_view(), name='detail'),
    url(r'^create/$', TodoCreate.as_view(), name='create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# TODO: Implement 2FA & update corresponding Cover letter
# TODO: Implement TBA using django-allauth & update corresponding Cover letter
# TODO: Implement dependencies (Bootsrap) installation via Bower or Webpack
# TODO: Add Travis & update corresponding Cover letter
