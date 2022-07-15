from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-most_recent')
    template_name = 'index.html'
    
