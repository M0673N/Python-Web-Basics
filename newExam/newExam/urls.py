from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from newExam.profile_app.views import show_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_home, name='home'),
    path('', include('newExam.expense_app.urls')),
    path('profile/', include('newExam.profile_app.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
