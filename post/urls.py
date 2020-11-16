from django.urls import path
from . import views


urlpatterns = [
    path('post/list/', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/detail/<int:post_pk>/', views.post_detail, name='post_detail'),
    path('post/edit/<int:post_pk>/', views.post_edit, name='post_edit'),

]
