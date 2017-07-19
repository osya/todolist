from django.shortcuts import render_to_response, redirect
from .forms import addForm
from .models import Todo


def add(request):
    form = addForm(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data['title']
        text = form.cleaned_data['text']
        todo = Todo(title=title, text=text)
        todo.save()
        return redirect('/todos')
    return render_to_response('todos/add.html', {'form': form})

