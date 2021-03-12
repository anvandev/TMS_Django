from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Basket, ProductInBasket


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})


def basket(request):
    basket = get_object_or_404(Basket, user=request.user)
    products = ProductInBasket.objects.filter(basket=basket)
    return render(request, 'shop/basket.html', {'products': products,
                                                'basket': basket})


def add_to_basket(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    user_basket = get_object_or_404(Basket, user=request.user)
    if ProductInBasket.objects.filter(basket=user_basket, product=product):
        product_in_basket = ProductInBasket.objects.get(basket=user_basket, product=product)
        product_in_basket.product_quantity += 1
        product_in_basket.save()
    else:
        ProductInBasket.objects.create(product=product, basket=user_basket)
    return redirect('basket')


def reduce_product_from_basket(request, product_pk):
    product = get_object_or_404(ProductInBasket, pk=product_pk)
    product.product_quantity -= 1
    product.save()
    if product.product_quantity == 0:
        product.delete()
    return redirect('basket')


def remove_product_from_basket(request, product_pk):
    product = get_object_or_404(ProductInBasket, pk=product_pk)
    product.delete()
    return redirect('basket')


def remove_all_from_basket(request):
    basket = get_object_or_404(Basket, user=request.user)
    products_in_basket = ProductInBasket.objects.filter(basket=basket)
    products_in_basket.delete()
    return redirect('basket')


def order(request):
    basket = get_object_or_404(Basket, user=request.user)
    products = basket.productinbasket_set.all()
    return render(request, 'shop/order.html', {'products': products,
                                               'basket': basket})


# def order(request):
#     basket = get_object_or_404(Basket, user=request.user)
#     products = basket.productinbasket_set.all()
#     ordered_products = Order.objects.create(products=products, user=request.user)
#     return render(request, 'shop/order.html', {'ordered_products': ordered_products,
#                                                'basket': basket})
