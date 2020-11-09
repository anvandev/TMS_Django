from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def post_list(request):
    post = Post.objects.all()
    return HttpResponse(post)
#    return render(request, 'post/post_list.html', {'posts': posts})
