from django.shortcuts import render

from newDjangoProject.todo_app.models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'index.html', context=context)
