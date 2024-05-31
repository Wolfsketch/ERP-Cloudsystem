from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from ERPWinkel.admin import admin_site  # Importeer je aangepaste AdminSite

urlpatterns = [
    path('admin/', admin_site.urls),  # Gebruik je aangepaste AdminSite
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('ERPWinkel.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
