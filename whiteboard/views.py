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

class GamePostList(View):

      def get(self, request, ref_name):
        game_obj= Game.objects.get(ref_name=ref_name)
        post = Post.objects.filter(game=game_obj)

        return render(request, 'game_page.html',
                        {
                        "post": post,
                        "game": game_obj
                        },
                )

class MenuList(View):
    

    def get(self, request, ref_name):
        game_obj= Game.objects.get(ref_name=ref_name)

        return render(request, 'nav.html',
                        {
                        "game": game_obj
                        },
                )

        # queryset = Post.objects.filter


# class GamePostList(generic.ListView):

#     template_name = 'game_page.html'
#     model = Post
#     queryset = Post.objects.filter(Post.game.ref_name =  )

#     def get_queryset(self):
#         content = {
#             'game': self.kwargs['game'],
#             'post': Review.objects.filter(game__name=self.kwargs['game'])
#             .filter(status=1),
#         }

#         return content

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post_exists = Post.objects.filter(name=self.kwargs['game']).exists()
#         context['genre_exists'] = genre_exists
#         return context




# class GamePosts(View, game):

#      def get(self, request, game.id):
#          queryset = Post.objects.filter(game.ref_name)


         

    
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
    # paginate_by = 10

# class PostDetail(View):

#     def get(self, request, *args, **kwargs):
