from django.urls import path

from model_forms.demo.views import index, create, edit

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('edit/<int:pk>', edit, name='edit')
]
