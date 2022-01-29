from django.urls import path

from onlineLibrary.profiles.views import show_profile, delete_profile, edit_profile

urlpatterns = [
    path('', show_profile, name='profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
]
