from braces.views import SetHeadlineMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import ArchiveIndexView, CreateView
from django.views.generic.base import ContextMixin, View
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin
from rest_framework import permissions, viewsets

from todos.forms import SearchForm, TodoForm
from todos.models import Todo
from todos.permissions import IsOwnerOrReadOnly
from todos.serializers import TodoSerializer


class RestrictToUserMixin(View):
    object = None

    def get_queryset(self):
        assert isinstance(self, (SingleObjectMixin, MultipleObjectMixin))
        queryset = super(RestrictToUserMixin, self).get_queryset()
        if self.request.user.is_authenticated() and not self.request.user.is_superuser:
            queryset = queryset.filter(user=self.request.user)
        return queryset

    def post(self, request, *args, **kwargs):
        assert isinstance(self, SingleObjectMixin)
        self.object = self.get_object()
        return super(RestrictToUserMixin, self).post(request, *args, **kwargs) \
            if self.request.user == self.object.user or self.request.user.is_superuser \
            else redirect(reverse('login'))


class SearchFormMixin(ContextMixin, View):
    def get_context_data(self, **kwargs):
        context = super(SearchFormMixin, self).get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context


class TodoCreate(LoginRequiredMixin, SetHeadlineMixin, SearchFormMixin, CreateView):
    form_class = TodoForm
    model = Todo
    headline = 'Add Todo'
    object = None

    def get_initial(self):
        initial = super(TodoCreate, self).get_initial()
        if self.request.GET.get('tags'):
            initial['tags'] = self.request.GET.get('tags')
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(TodoCreate, self).form_valid(form)


class TodoDetail(LoginRequiredMixin, RestrictToUserMixin, SearchFormMixin, DetailView):
    model = Todo


class TodoList(LoginRequiredMixin, RestrictToUserMixin, SearchFormMixin, ArchiveIndexView):
    paginate_by = 10
    date_field = 'created_at'
    allow_empty = True
    allow_future = True

    def get_queryset(self):
        return Todo.objects.list(self.request.GET)


# TODO: Implement Update & Delete tasks
# class TodoDelete(LoginRequiredMixin, RestrictToUserMixin, SearchFormMixin):
#
#     def get_success_url(self):
#         url = reverse('todos:list')
#         query = self.request.GET.urlencode()
#         if query:
#             url = f'{url}?{query}'
#         return url


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_queryset(self):
        return Todo.objects.list(self.request.GET)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# TODO: Write tests for the API calls
