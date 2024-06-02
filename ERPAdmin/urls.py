from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from ERPWinkel.admin import admin_site
from ERPWinkel import views as winkel_views

urlpatterns = [
    path('admin/', winkel_views.admin_dashboard, name='admin_dashboard'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('ERPWinkel.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(template_name='admin/password_reset.html'), name='password_reset'),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='admin/password_reset_done.html'), name='password_reset_done'),
    path('admin/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='admin/password_reset_confirm.html'), name='password_reset_confirm'),
    path('admin/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='admin/password_reset_complete.html'), name='password_reset_complete'),
    path('admin/register/', winkel_views.RegisterView.as_view(), name='register'),
    path('admin/', admin_site.urls),
    # andere URL-patronen
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
