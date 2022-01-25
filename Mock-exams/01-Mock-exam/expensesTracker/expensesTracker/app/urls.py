from django.urls import path

from expensesTracker.app.views import home, create, edit, delete, profile, profile_edit, profile_delete

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete'),
    path('profile/', profile, name='profile'),
    path('profile/edit', profile_edit, name='profile edit'),
    path('profile/delete', profile_delete, name='profile delete'),
]
