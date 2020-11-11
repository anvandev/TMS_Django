from django.urls import path
from . import views


urlpatterns = [
    path('post/list/', views.post_list, name='post_list'),
    path('post/detail/<int:post_pk>/', views.post_detail, name='post_detail')

]
