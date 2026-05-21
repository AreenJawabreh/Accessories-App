from django.shortcuts import render

# Create your views here.
from .models import Product, Category

def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'store/home.html', {'products': products})