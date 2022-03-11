import os

from django.conf import settings
from django.shortcuts import render, redirect

from newExam.expense_app.models import Expense
from newExam.profile_app.forms import ProfileForm
from newExam.profile_app.models import Profile


def show_home(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()

    profile = Profile.objects.first()
    expenses = Expense.objects.all()
    context = {
        'form': form,
        'profile': profile,
        'expenses': expenses,
    }
    if expenses:
        context.money_left = profile.budget - sum([expense.price for expense in expenses])
    if profile:
        return render(request, 'home-with-profile.html', context)
    else:
        return render(request, 'home-no-profile.html', context)


def show_profile(request):
    profile = Profile.objects.first()
    expenses = Expense.objects.all()
    count = expenses.count()
    money_left = profile.budget - sum([expense.price for expense in expenses])
    context = {'profile': profile, 'count': count, 'money_left': money_left}
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    old_picture = None
    if profile.profile_image:
        old_picture = os.path.join(settings.MEDIA_ROOT, str(profile.profile_image))
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            if old_picture:
                os.remove(old_picture)
            return redirect('show_profile')
    else:
        form = ProfileForm(instance=profile)

    context = {'form': form, 'profile': profile}
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.first()
        expenses = Expense.objects.all()
        profile.profile_image.delete()
        profile.delete()
        expenses.delete()

        return redirect('home')
    else:
        return render(request, 'profile-delete.html', {'profile': Profile.objects.first()})
