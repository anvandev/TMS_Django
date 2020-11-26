from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Tag, Category
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.filter(draft=False)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts, 'tags': tags, 'categories': categories})


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    tags = post.tag.all()
    rating_values = post.rating.all()
    rating = 0
    for element in rating_values:
        rating += element.rating
    rating = rating / rating_values.count()
    comments = Comment.objects.filter(post=post_pk)
    comment_form = CommentForm()
    post.view += 1
    post.save()
    return render(request, 'post/post_detail.html',
                  {'post': post, 'comments': comments, 'comment_form': comment_form, 'tags': tags, 'rating': rating})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None)
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
        form = PostForm(request.POST, request.FILES or None, instance=post)
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


def tag_list(request, tag_pk):
    tag = get_object_or_404(Tag, pk=tag_pk)
    posts = tag.posts.all()
    return render(request, 'post/post_list.html', {'posts': posts})


def category_posts(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    posts = category.posts.all()
    return render(request, 'post/post_list.html', {'posts': posts})


def recommended_list(request):
    posts = Post.objects.order_by('-like')[:10]
    posts_by_views = Post.objects.order_by('-view')[:10]
    posts_by_comments = Post.objects.order_by('-like')[:10]
    return render(request, 'post/post_list.html', {'posts': posts})


