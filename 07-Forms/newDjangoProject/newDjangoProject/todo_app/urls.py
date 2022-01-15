from django.urls import path

from newDjangoProject.todo_app.views import index, create, edit, delete

urlpatterns = [
    path('index/', index, name='index'),
    path('create/', create, name='create_todo'),
    path('edit/<int:pk>', edit, name='edit_todo'),
    path('delete/<int:pk>', delete, name='delete_todo'),
]
