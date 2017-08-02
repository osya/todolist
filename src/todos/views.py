from django.views import generic
from braces import views
from .forms import TodoForm
from .models import Todo


class TodoCreateView(views.LoginRequiredMixin, views.SetHeadlineMixin, generic.CreateView):
    form_class = TodoForm
    model = Todo
    headline = 'Add Todo'


class TodoDetailView(views.LoginRequiredMixin, generic.DetailView):
    model = Todo


class TodoListView(views.LoginRequiredMixin, generic.ListView):
    queryset = Todo.objects.all().order_by('-created_at')[:10]
