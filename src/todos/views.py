from django.views import generic
from django.views.generic.base import ContextMixin, View
from braces import views

from .forms import TodoForm
from .models import Todo


class PageContextMixin(ContextMixin, View):
    def get_context_data(self, **kwargs):
        context = super(PageContextMixin, self).get_context_data(**kwargs)
        context['page'] = int(self.request.GET.get('page', 1))
        return context


class TodoCreateView(views.SetHeadlineMixin, views.LoginRequiredMixin, PageContextMixin, generic.CreateView):
    form_class = TodoForm
    model = Todo
    headline = 'Add Todo'


class TodoDetailView(views.LoginRequiredMixin, PageContextMixin, generic.DetailView):
    model = Todo


class TodoListView(views.LoginRequiredMixin, PageContextMixin, generic.ArchiveIndexView):
    queryset = Todo.objects.all().order_by('-created_at')
    paginate_by = 10
    date_field = 'created_at'
    allow_empty = True
    allow_future = True

# TODO: Сделать, чтобы для каждого аккаунта отображались только его задачи, а не весь список задач
# TODO: Create REST API
