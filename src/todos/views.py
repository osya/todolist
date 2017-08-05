from django.views import generic
from braces import views
from .forms import TodoForm
from .models import Todo


class TodoCreateView(views.SetHeadlineMixin, views.LoginRequiredMixin, generic.CreateView):
    form_class = TodoForm
    model = Todo
    headline = 'Add Todo'


class TodoDetailView(views.LoginRequiredMixin, generic.DetailView):
    model = Todo

    def get_context_data(self, **kwargs):
        context = super(TodoDetailView, self).get_context_data(**kwargs)
        context['page'] = self.request.GET.get('page', 1)
        return context


class TodoListView(views.LoginRequiredMixin, generic.ListView):
    queryset = Todo.objects.all().order_by('-created_at')
    paginate_by = 10

# TODO: Сделать, чтобы для каждого аккаунта отображались только его задачи, а не весь список задач
# TODO: Create REST API
