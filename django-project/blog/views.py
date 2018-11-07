from django.shortcuts import render

def blog(request):
    queryset = Post.objests.all().order_by("-date")[:25]
    return render(request, "blog.html", {})

def post(request):
    return render(request, 'post.html', {})
