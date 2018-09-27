

from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request,post):
    post = Post.objects.all()
    post = Post(request.GET, queryset = post)
    return render(request,'blog/post/list.html',
    {'posts': post})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    return render(request,'blog/post/detail.html',
    {'post': post})
