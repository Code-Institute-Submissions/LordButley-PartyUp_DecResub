from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Game, Comment

# Create your views here.

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

class GameComment(View):

    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        comments = Comment.objects.filter(post=post)
        # comments = post.comments.order_by("-created_on")

        return render(request, 'post_page.html',
            {
              "post": post,
              "comment": comments,
            }
      
        )


