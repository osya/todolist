from django.shortcuts import render
from .forms import addForm
from .models import Todo


def add(request):
    form = addForm(request.POST or None)
    form_title = 'Add Todo'
    confirm_message = None
    if form.is_valid():
        title = form.cleaned_data['title']
        text = form.cleaned_data['text']
        todo = Todo(title=title, text=text)
        todo.save()
        confirm_message = 'New Todo added'
        form = None
    return render(request, 'todos/add.html', {'form_title': form_title, 'form': form, 'confirm_message': confirm_message})
