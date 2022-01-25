from django.shortcuts import render, redirect

from expensesTracker.app.forms import ProfileForm, ExpenseForm
from expensesTracker.app.models import Profile, Expense


def home(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'home-no-profile.html', {'form': form})
    else:
        profile = Profile.objects.all()
        if profile:
            profile = Profile.objects.all()[0]
            expenses = Expense.objects.all()
            cash_left = profile.budget - sum([expense.price for expense in expenses])
            return render(request, 'home-with-profile.html',
                          {'profile': profile, 'expenses': expenses, 'cash_left': cash_left})
        else:
            return render(request, 'home-no-profile.html')


def create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return render(request, 'expense-create.html')


def edit(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return render(request, 'expense-edit.html', {'expense': expense})


def delete(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('home')
    else:
        return render(request, 'expense-delete.html', {'expense': expense})


def profile(request):
    profile = Profile.objects.all()[0]
    expenses = Expense.objects.all()
    budget = profile.budget - sum([expense.price for expense in expenses])
    return render(request, 'profile.html', {'profile': profile, 'budget': budget})


def profile_edit(request):
    profile = Profile.objects.all()[0]
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        return render(request, 'profile-edit.html', {'profile': profile})


def profile_delete(request):
    profile = Profile.objects.all()[0]
    if request.method == 'POST':
        profile.delete()
        expenses = Expense.objects.all()
        expenses.delete()
        return redirect('home')
    else:
        return render(request, 'profile-delete.html')