from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-most_recent')
    template_name = 'index.html'
    
class DeadByDaylight(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-most_recent')
    template_name = 'dead_by_daylight.html'
    # paginate_by = 10

class RocketLeague(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-most_recent')
    template_name = 'rocket_league.html'
    # paginate_by = 10