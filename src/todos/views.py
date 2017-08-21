from braces import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views import generic
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin

from .forms import TodoForm
from .models import Todo


class SuccessUrlMixin(View):
    def get_success_url(self):
        url = reverse('todos:list')
        query = self.request.GET.urlencode()
        if query:
            url = f'{url}?{query}'
        return url


class RestrictToUserMixin(View):
    object = None

    def get_queryset(self):
        assert isinstance(self, (SingleObjectMixin, MultipleObjectMixin))
        assert isinstance(self, View)
        queryset = super(RestrictToUserMixin, self).get_queryset()
        if self.request.user.is_authenticated() and not self.request.user.is_superuser:
            queryset = queryset.filter(user=self.request.user)
        return queryset

    def post(self, request, *args, **kwargs):
        assert isinstance(self, SingleObjectMixin)
        self.object = self.get_object()
        assert isinstance(self, View)
        return super(RestrictToUserMixin, self).post(request, *args, **kwargs) \
            if self.request.user == self.object.user or self.request.user.is_superuser \
            else redirect(reverse('login'))


class TodoCreateView(views.SetHeadlineMixin, LoginRequiredMixin, generic.CreateView):
    form_class = TodoForm
    model = Todo
    headline = 'Add Todo'
    object = None

    def get_initial(self):
        initial = super(TodoCreateView, self).get_initial()
        if self.request.GET.get('tags'):
            initial['tags'] = self.request.GET.get('tags')
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(TodoCreateView, self).form_valid(form)


class TodoDetailView(LoginRequiredMixin, RestrictToUserMixin, generic.DetailView):
    model = Todo


class TodoListView(LoginRequiredMixin, RestrictToUserMixin, generic.ArchiveIndexView):
    queryset = Todo.objects.all().order_by('-created_at')
    paginate_by = 10
    date_field = 'created_at'
    allow_empty = True
    allow_future = True

    def get_queryset(self):
        return Todo.objects.list(self.request.GET)

# TODO: Create REST API
# TODO: Implement Update & Delete tasks
