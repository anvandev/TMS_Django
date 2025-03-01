from django.urls import path
from . import views


urlpatterns = [
    path('post/list/', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/detail/<int:post_pk>/', views.post_detail, name='post_detail'),
    path('post/edit/<int:post_pk>/', views.post_edit, name='post_edit'),
    path('post/remove/<int:post_pk>/', views.post_remove, name='post_remove'),
    path('comment/remove/<int:comment_pk>/', views.comment_remove, name='comment_remove'),
    path('post/<int:post_pk>/comment/new/', views.comment_new, name='comment_new'),
    path('post/comment/edit/<int:comment_pk>/', views.comment_edit, name='comment_edit'),
    path('post/detail/like/<int:post_pk>/<int:like>/', views.post_like, name='post_like'),
    path('post/draft/list/', views.draft_list, name='draft_list'),
    path('post/publish/<int:post_pk>/', views.publish, name='publish'),
    path('post/tag/posts/<int:tag_pk>/', views.tag_posts, name='tag_posts'),
    path('post/category/posts/<int:category_pk>/', views.category_posts, name='category_posts'),
    path('post/recommended/posts/<int:order>/', views.recommended_list, name='recommended_list'),
    path('post/add_to_favorites/<int:post_pk>/', views.add_to_favorites, name='add_to_favorites'),
    path('post/favorites/', views.favorites, name='favorites'),
]
