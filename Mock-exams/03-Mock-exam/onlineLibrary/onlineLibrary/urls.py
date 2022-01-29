from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('onlineLibrary.profiles.urls')),
    path('', include('onlineLibrary.books.urls')),
]
