from django.urls import path

from newDjangoProject.formsDemo.views import demo_form

urlpatterns = [
    path('', demo_form, name='demo form'),
]
