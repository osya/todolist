from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from todos.views import TodoCreate, TodoDetail, TodoList, TodoViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet, base_name='todo')

urlpatterns = [
    url(r'^$', TodoList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', TodoDetail.as_view(), name='detail'),
    url(r'^create/$', TodoCreate.as_view(), name='create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# TODO: Implement 2FA & update corresponding Cover letter
# TODO: Implement TBA using django-allauth & update corresponding Cover letter
