from django.shortcuts import render
from .models import Product

def home(request):
    producten = Product.objects.all()
    return render(request, 'home.html', {'producten':producten})

def about(request):
    return render(request, 'about.html')

def my_view(request):
    print("View wordt aangeroepen")  # Debug statement
    return render(request, 'admin/base_site.html', {})