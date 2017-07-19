from django.shortcuts import render, redirect
from .forms import addForm
from .models import Todo


def add(request):
    form = addForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/todos')
    return render(request, 'todos/add.html', {'form': form})

