from django.views import generic
from braces import views
from .forms import TodoForm
from .models import Todo


class TodoCreateView(views.SetHeadlineMixin, generic.CreateView):
    form_class = TodoForm
    model = Todo
    headline = 'Add Todo'


class TodoDetailView(generic.DetailView):
    model=Todo


class TodoListView(generic.ListView):
    queryset=Todo.objects.all().order_by('-created_at')[:10]
