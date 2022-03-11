from django.shortcuts import render, redirect

from myMusicApp.albums.models import Album
from myMusicApp.profiles.forms import ProfileForm
from myMusicApp.profiles.models import Profile


def show_home(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()

    profile = Profile.objects.first()
    albums = Album.objects.all()
    context = {
        'form': form,
        'profile': profile,
        'albums': albums,
    }
    if profile:
        return render(request, 'home-with-profile.html', context)
    else:
        return render(request, 'home-no-profile.html', context)
