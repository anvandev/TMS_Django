from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Basket, ProductInBasket, ProductCategory, Review


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})


def basket(request):
    basket = get_object_or_404(Basket, user=request.user)
    products = ProductInBasket.objects.filter(basket=basket)
    return render(request, 'shop/basket.html', {'products': products})


def add_to_basket(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    basket = get_object_or_404(Basket, user=request.user)
    products_in_basket = ProductInBasket.objects.filter(basket=basket)
    if product in products_in_basket:
        products_in_basket.product_quantity += 1
        products_in_basket.save()
    else:
        product_in_basket = ProductInBasket.objects.create(product=product, basket=basket)
    return redirect('basket')
