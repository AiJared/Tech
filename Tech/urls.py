from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from Tech.settings import MEDIA_ROOT, STATIC_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('techapp.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=STATIC_ROOT)