from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from ERPWinkel import views
from ERPWinkel.admin import admin_site  # Importeer je aangepaste AdminSite

urlpatterns = [
    path('admin/', admin_site.urls),  # Gebruik je aangepaste AdminSite
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('ERPWinkel.urls')),
    path('grappelli/', include('grappelli.urls')),  # grappelli URL's
    path('my_view/', views.my_view, name='my_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

