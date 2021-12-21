from django.urls import path

from djangoProject.main_app.views import show_main_app

urlpatterns = [
    path('', show_main_app)
]
