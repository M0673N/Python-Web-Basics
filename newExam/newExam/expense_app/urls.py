from django.urls import path

from newExam.expense_app.views import create_expense, edit_expense, delete_expense

urlpatterns = [
    path('create/', create_expense, name='create_expense'),
    path('edit/<int:pk>', edit_expense, name='edit_expense'),
    path('delete/<int:pk>', delete_expense, name='delete_expense'),
]
