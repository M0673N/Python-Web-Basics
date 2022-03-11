from django.shortcuts import render, redirect

from newExam.expense_app.forms import ExpenseForm, DeleteExpenseForm
from newExam.expense_app.models import Expense
from newExam.profile_app.models import Profile


def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm()
    context = {'form': form, 'profile': Profile.objects.first()}
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm(instance=expense)
    context = {'form': form, 'profile': Profile.objects.first()}
    return render(request, 'expense-create.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('home')
    else:
        form = DeleteExpenseForm(instance=expense)
    context = {'form': form, 'profile': Profile.objects.first()}
    return render(request, 'expense-delete.html', context)
