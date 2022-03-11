from django.urls import path

from newExam.profile_app.views import show_profile, edit_profile, delete_profile

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('delete/', delete_profile, name='delete_profile')
]
