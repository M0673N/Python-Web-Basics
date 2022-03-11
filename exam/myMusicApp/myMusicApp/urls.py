from django.contrib import admin
from django.urls import path, include

from myMusicApp.views import show_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_home, name='home'),
    path('album/', include('myMusicApp.albums.urls')),
    path('profile/', include('myMusicApp.profiles.urls')),
]
