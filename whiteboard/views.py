from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Game

# Create your views here.


# class PostList(generic.ListView):
#     model = Post
#     queryset = Post.objects.order_by('-most_recent')
#     template_name = 'index.html'

class GameList(generic.ListView):
    model = Game
    template_name = 'index.html'


# class GameDetail(View, obj):


#     def get(self, request, id):
#         queryset = Post.objects.filter(game=obj.)

    
    # queryset = Game.objects.order_by('id')


# class DeadByDaylight(generic.ListView):
#     model = Post
#     queryset = Post.objects.order_by('-most_recent')
#     template_name = 'dead_by_daylight.html'
#     # paginate_by = 10


# class RocketLeague(generic.ListView):
#     model = Post
#     queryset = Post.objects.order_by('-most_recent')
#     template_name = 'rocket_league.html'
#     # paginate_by = 10

# class PostDetail(View):

#     def get(self, request, *args, **kwargs):
