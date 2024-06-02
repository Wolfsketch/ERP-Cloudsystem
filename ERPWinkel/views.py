from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Product

def home(request):
    producten = Product.objects.all()
    return render(request, 'home.html', {'producten': producten})

def about(request):
    return render(request, 'about.html')

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'admin/register.html'

def admin_dashboard(request):
    return render(request, 'admin/admin.html')
