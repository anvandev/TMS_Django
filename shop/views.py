from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


def product_list(request):
    products = Product.objects.all()
    for product in products:
        categories = product.categories.all
        reviews = product.review.all
    return render(request, 'shop/product_list.html', {'products': products,
                                                      'categories': categories,
                                                      'reviews': reviews})
