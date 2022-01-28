from django.shortcuts import render, redirect

from notes.app.forms import ProfileForm, NoteForm, NoteDeleteForm
from notes.app.models import Profile, Note


def home(request):
    if request.method == 'GET':
        profile = Profile.objects.first()
        if not profile:
            form = ProfileForm()
            return render(request, 'home-no-profile.html', {'form': form})
        else:
            notes = Note.objects.all()
            return render(request, 'home-with-profile.html', {'notes': notes})
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'home-no-profile.html', {'form': form})


def add_note(request):
    if request.method == 'GET':
        form = NoteForm()
        return render(request, 'note-create.html', {'form': form})
    else:
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'note-create.html', {'form': form})


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        form = NoteForm(instance=note)
        return render(request, 'note-edit.html', {'form': form})
    else:
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'note-edit.html', {'form': form})


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        form = NoteDeleteForm(instance=note)
        return render(request, 'note-delete.html', {'form': form})
    else:
        note.delete()
        return redirect('home')


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'note-details.html', {'note': note})


def profile_details(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()
    return render(request, 'profile.html', {'profile': profile, 'notes': notes.count()})


def delete_profile(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()
    profile.delete()
    notes.delete()
    return redirect('home')
