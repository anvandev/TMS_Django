from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    return render(request, 'post/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/post_new.html', {'form': form})


def post_edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_edit.html', {'form': form})
