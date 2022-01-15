from django.shortcuts import render, redirect

from newDjangoProject.todo_app.forms import TodoForm
from newDjangoProject.todo_app.models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'index.html', context=context)


def create(request):
    if request.method == 'GET':
        form = TodoForm()
        context = {'form': form}
        return render(request, 'create.html', context=context)

    form = TodoForm(request.POST)
    if form.is_valid():
        todo = Todo(**form.cleaned_data)
        todo.save()
        return redirect('index')

    return render(request, 'create.html', context={'form': form})


def edit(request, pk):
    if request.method == 'GET':
        form = TodoForm()
        context = {'pk': pk, 'form': form}
        return render(request, 'edit.html', context=context)

    form = TodoForm(request.POST)
    if form.is_valid():
        todo = Todo.objects.get(pk=pk)
        todo.title = form.cleaned_data['title']
        todo.description = form.cleaned_data['description']
        todo.save()
        return redirect('index')

    return render(request, 'edit.html', context={'form': form})


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('index')
