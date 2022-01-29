from django.shortcuts import render, redirect

from onlineLibrary.books.models import Book
from onlineLibrary.profiles.forms import ProfileForm, DeleteProfileForm
from onlineLibrary.profiles.models import Profile


def show_profile(request):
    profile = Profile.objects.first()
    return render(request, 'profile.html', {'profile': profile})


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileForm(instance=profile)
        return render(request, 'edit-profile.html', {'form': form, 'profile': profile})
    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return render(request, 'edit-profile.html', {'form': form, 'profile': profile})


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
        return render(request, 'delete-profile.html', {'form': form, 'profile': profile})
    else:
        books = Book.objects.all()
        profile.delete()
        books.delete()
        return redirect('home')
