from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.filter(draft=False)
    return render(request, 'post/post_list.html', {'posts': posts})


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comments = Comment.objects.filter(post=post_pk)
    comment_form = CommentForm()
    post.view += 1
    post.save()
    return render(request, 'post/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})


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


def post_remove(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.delete()
    return redirect('post_list')


def comment_remove(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    post_pk = comment.post.pk
    return redirect('post_detail', post_pk=post_pk)


def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.created_date = timezone.now()
            comment.post = post
            comment.save()
            return redirect('post_detail', post_pk=comment.post.pk)
    else:
        comment_form = PostForm()
    return render(request, 'post/post_detail.html', {'comment_form': comment_form})


def comment_edit(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.created_date = timezone.now()
            comment.save()
            return redirect('post_detail', post_pk=comment.post.pk)
    else:
        comment_form = CommentForm(instance=comment)
    return render(request, 'post/comment_edit.html', {'comment_form': comment_form})


def post_like(request, post_pk, like):
    post = get_object_or_404(Post, pk=post_pk)
    if like == 1:
        post.like += 1
    if like == 2:
        post.dislike += 1
    post.save()
    return redirect('post_detail', post_pk=post_pk)


def draft_list(request):
    posts = Post.objects.filter(draft=True)
    return render(request, 'post/post_list.html', {'posts': posts})


def publish(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.draft = False
    post.save()
    return redirect('post_detail', post_pk=post_pk)



# def post_dislike(request, post_pk):
#     post = get_object_or_404(Post, pk=post_pk)
#     post.dislike += 1
#     post.save()
#     return redirect('post_detail', post_pk=post.pk)
