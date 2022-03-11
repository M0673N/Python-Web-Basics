from django.shortcuts import render, redirect

from myMusicApp.albums.models import Album
from myMusicApp.profiles.models import Profile


def profile_details(request):
    profile = Profile.objects.first()
    albums_count = Album.objects.count()
    context = {'profile': profile, 'albums_count': albums_count}
    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        albums = Album.objects.all()
        albums.delete()
        profile.delete()
        return redirect('home')
    else:
        return render(request, 'profile-delete.html', {'profile': profile})
