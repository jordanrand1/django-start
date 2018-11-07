from django.urls import re_path, include
from django.views.generic import ListView, DetailView
from blog.models import Post

from . import views

urlpatterns = [ 
    re_path(r'$', views.blog, name="blog"),
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post, template_name = 'blog/post.html')),
 ]