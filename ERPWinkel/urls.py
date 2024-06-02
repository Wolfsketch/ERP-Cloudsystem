from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('dashboard/', views.admin_dashboard, name='dashboard'),  # Nieuwe URL voor het dashboard
]
