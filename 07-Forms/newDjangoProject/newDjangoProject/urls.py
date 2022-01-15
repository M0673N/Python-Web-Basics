from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newDjangoProject.todo_app.urls')),
    path('form/', include('newDjangoProject.formsDemo.urls')),
]
