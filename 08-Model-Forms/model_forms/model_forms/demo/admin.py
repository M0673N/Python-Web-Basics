from django.contrib import admin

from model_forms.demo.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'pages', 'description', 'author']
