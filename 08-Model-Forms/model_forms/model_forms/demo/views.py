from django.shortcuts import render, redirect

from model_forms.demo.forms import BookForm
from model_forms.demo.models import Book


def create(request):
    if request.method == 'GET':
        return render(request, 'create.html', {'form': BookForm()})

    form = BookForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        return render(request, 'create.html', {'form': form})


def edit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'edit.html', {'form': BookForm(initial=book.__dict__, instance=book)})

    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        return render(request, 'edit.html', {'form': form})


def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})
