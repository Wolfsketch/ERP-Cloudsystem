from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from ERPWinkel import views
from django.contrib.auth import views as auth_views
from ERPWinkel.admin import admin_site  # Importeer je aangepaste AdminSite
from . import views

urlpatterns = [
    path('admin/', admin_site.urls),  # Gebruik je aangepaste AdminSite
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('ERPWinkel.urls')),
    path('grappelli/', include('grappelli.urls')),  # grappelli URL's
    path('admin/login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(template_name='admin/password_reset.html'), name='password_reset'),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='admin/password_reset_done.html'), name='password_reset_done'),
    path('admin/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='admin/password_reset_confirm.html'), name='password_reset_confirm'),
    path('admin/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='admin/password_reset_complete.html'), name='password_reset_complete'),
    path('admin/signup/', views.SignUpView.as_view(), name='signup'),  # Voeg deze regel toe
    # andere URL-patronen
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

