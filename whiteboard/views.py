from django.shortcuts import render, get_object_or_404, redirect, reverse
# from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Post, Game, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth import get_user

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
        game_obj = Game.objects.get(post=post)

        comments = Comment.objects.filter(post=post)

        return render(request, 'post_page.html',
            {
              "post": post,
              "game": game_obj,
              "comments": comments,
              "comment_form": CommentForm()
            }
      
    )

    def post(self, request, id):
        post = get_object_or_404(Post, id=id)
        comments = Comment.objects.filter(post=post)

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(request, 'post_page.html',
            {
              "post": post,
              "comments": comments,
              "comment_form": CommentForm()
            }
      
    )


class CreatePost(View):

    def get(self, request, ref_name):
        game_obj= Game.objects.get(ref_name=ref_name)

        return render(request, 'create_post.html',
        {
            "post_form": PostForm(),
            "game": game_obj
        }
        )

    def post(self, request, ref_name):
        game_obj= Game.objects.get(ref_name=ref_name)

        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post_form.instance.name = request.user.username
            post = post_form.save(commit=False)
            post.author = get_user(request)
            post.game = Game.objects.get(ref_name=ref_name)
            post.save()
            # return HttpResponseRedirect('game_page' 'ref_name')
            url = request.POST.get("url")
            return redirect(reverse("game_page", args=(url,)))
        else:
            post_form = PostForm()

        return render(request, 'create_post.html',
        {
            "post_form": PostForm()
        }
        )



