from django.urls import path

from djangoProject.secondary_app.views import show_secondary_app

urlpatterns = [
    path('', show_secondary_app)
]
