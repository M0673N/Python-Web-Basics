from django.urls import path

from onlineLibrary.books.views import home, add_book, book_details, edit_book, delete_book

urlpatterns = [
    path('', home, name='home'),
    path('add', add_book, name='add book'),
    path('details/<int:pk>', book_details, name='details'),
    path('edit/<int:pk>', edit_book, name='edit book'),
    path('delete/<int:pk>', delete_book, name='delete book'),
]
