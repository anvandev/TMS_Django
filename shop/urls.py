from django.urls import path
from . import views


urlpatterns = [
    path('shop/product/list/', views.product_list, name='product_list'),
    path('shop/basket/', views.basket, name='basket'),
    path('shop/add_to_basket/<int:product_pk>/', views.add_to_basket, name='add_to_basket'),
]
