from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    return render(request, 'post/post_detail.html', {'post': post})


def post_new(request):
    form = PostForm()
    return render(request, 'post/post_new.html', {'form': form})

