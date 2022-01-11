from django.urls import path

from newDjangoProject.todo_app.views import index

urlpatterns = [
    path('index/', index)
]
