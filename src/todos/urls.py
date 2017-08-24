from django.conf.urls import url, include

from todos.views import TodoDetail, TodoCreate, TodoList, TodoListApi, TodoDetailApi

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

# TODO: Implement 2FA & update corresponding Cover letter
# TODO: Implement TBA using django-allauth & update corresponding Cover letter
# TODO: Implement dependencies (Bootsrap) installation via Bower or Webpack
# TODO: Add Travis & update corresponding Cover letter
