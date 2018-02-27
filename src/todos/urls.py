from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from todolist.urls import ROUTER
from todos.views import TodoCreate, TodoDetail, TodoList, TodoViewSet

app_name = 'todos'

ROUTER.register(r'todos', TodoViewSet, base_name='todo')

urlpatterns = [
    path(r'', TodoList.as_view(), name='list'),
    path(r'<int:pk>', TodoDetail.as_view(), name='detail'),
    path(r'create/', TodoCreate.as_view(), name='create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# TODO: Implement 2FA & update corresponding Cover letter
# TODO: Implement TBA using django-allauth & update corresponding Cover letter
