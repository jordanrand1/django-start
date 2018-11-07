from django.shortcuts import render
from blog.models import Post

def blog(request):
    queryset = Post.objects.all().order_by("-date")[:25]
    return render(request, "blog.html", {"posts": queryset})

def post(request):
    return render(request, 'post.html', {})
