from django.urls import path

from myMusicApp.albums.views import add_album, edit_album, delete_album, album_details

urlpatterns = [
    path('add/', add_album, name='add album'),
    path('edit/<int:pk>', edit_album, name='edit album'),
    path('delete/<int:pk>', delete_album, name='delete album'),
    path('details/<int:pk>', album_details, name='album details')
]
