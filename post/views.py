from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    return render(request, 'post/post_detail.html', {'post': post})

