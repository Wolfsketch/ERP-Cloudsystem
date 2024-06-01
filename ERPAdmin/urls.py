from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ERPWinkel.admin import admin_site  # Import your custom AdminSite

urlpatterns = [
    path('admin/', admin_site.urls),  # Use your custom AdminSite
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('ERPWinkel.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)