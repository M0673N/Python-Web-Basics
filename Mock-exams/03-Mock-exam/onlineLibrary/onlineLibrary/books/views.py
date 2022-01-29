from django.shortcuts import render, redirect

from onlineLibrary.books.forms import BookForm
from onlineLibrary.books.models import Book
from onlineLibrary.profiles.forms import ProfileForm
from onlineLibrary.profiles.models import Profile


def home(request):
    if request.method == 'GET':
        profile = Profile.objects.first()
        if not profile:
            form = ProfileForm()
            return render(request, 'home-no-profile.html', {'form': form, 'profile': profile})
        else:
            books = Book.objects.all()
            return render(request, 'home-with-profile.html', {'books': books, 'profile': profile})
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'home-no-profile.html', {'form': form})


def add_book(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = BookForm()
        return render(request, 'add-book.html', {'form': form, 'profile': profile})
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'home-no-profile.html', {'form': form, 'profile': profile})


def book_details(request, pk):
    profile = Profile.objects.first()
    book = Book.objects.get(pk=pk)
    return render(request, 'book-details.html', {'book': book, 'profile': profile})


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('home')


def edit_book(request, pk):
    profile = Profile.objects.first()
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
        return render(request, 'edit-book.html', {'form': form, 'profile': profile})
    else:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'home-no-profile.html', {'form': form, 'profile': profile})
