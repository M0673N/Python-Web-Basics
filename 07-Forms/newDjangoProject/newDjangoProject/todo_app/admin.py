from django.contrib import admin

from newDjangoProject.todo_app import models

admin.site.register(models.Todo)
