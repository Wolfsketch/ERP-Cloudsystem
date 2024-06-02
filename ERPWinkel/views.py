from django.shortcuts import render
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def home(request):
    producten = Product.objects.all()
    return render(request, 'home.html', {'producten':producten})

def about(request):
    return render(request, 'about.html')

def my_view(request):
    print("View wordt aangeroepen")  # Debug statement
    return render(request, 'admin/base_site.html', {})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'admin/signup.html'