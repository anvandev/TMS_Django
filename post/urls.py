from django.urls import path
from . import views


urlpatterns = [
    path('post/list/', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/detail/<int:post_pk>/', views.post_detail, name='post_detail'),
    path('post/edit/<int:post_pk>/', views.post_edit, name='post_edit'),
    path('post/remove/<int:post_pk>/', views.post_remove, name='post_remove'),
    path('comment/remove/<int:comment_pk>/', views.comment_remove, name='comment_remove'),

]
