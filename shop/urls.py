from django.urls import path
from . import views


urlpatterns = [
    path('product/list/', views.product_list, name='product_list'),
    path('basket/', views.basket, name='basket'),
    path('add_to_basket/<int:product_pk>/', views.add_to_basket, name='add_to_basket'),
    path('reduce_product_from_basket/<int:product_pk>/', views.reduce_product_from_basket,
         name='reduce_product_from_basket'),
    path('remove_product_from_basket/<int:product_pk>/', views.remove_product_from_basket,
         name='remove_product_from_basket'),
    path('remove_all_from_basket/', views.remove_all_from_basket, name='remove_all_from_basket'),
    path('order/', views.order, name='order'),
]
