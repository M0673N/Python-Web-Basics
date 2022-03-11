from django.shortcuts import render, redirect

from myMusicApp.albums.forms import AlbumForm, DeleteAlbumForm
from myMusicApp.albums.models import Album
from myMusicApp.profiles.models import Profile


def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumForm()
    profile = Profile.objects.first()
    context = {'form': form, 'profile': profile}
    return render(request, 'add-album.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumForm(instance=album)
    profile = Profile.objects.first()
    context = {'form': form, 'profile': profile}
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('home')
    else:
        form = DeleteAlbumForm(instance=album)
    profile = Profile.objects.first()
    context = {'form': form, 'profile': profile}
    return render(request, 'delete-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    profile = Profile.objects.first()
    context = {'album': album, 'profile': profile}
    return render(request, 'album-details.html', context)
