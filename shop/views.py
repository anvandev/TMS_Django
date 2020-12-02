from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})
