from django.shortcuts import render, get_object_or_404
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
                # "post_form": PostForm()
            },
        )

    # def post(self, request, ref_name):
    #     game_obj= Game.objects.get(ref_name=ref_name)

    #     post = Post.objects.filter(game=game_obj)

    #     return render(request, 'game_page.html',
    #         {
    #             "post": post,
    #             "game": game_obj
    #             "post_form": PostForm()
    #         },
    #     )

    #     post_form = PostForm(data=request.POST)
    #     if post_form.is_valid():
    #         post_form.instance.name = request.user.username
    #         post = post_form.save(commit=False)
    #         # comment.post = post
    #         post.save()
    #     else:
    #         post_form = PostForm()

class GameComment(View):

    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        comments = Comment.objects.filter(post=post)
        # comments = post.comments.order_by("-created_on")

        return render(request, 'post_page.html',
            {
              "post": post,
              "comments": comments,
              "comment_form": CommentForm()
            }
      
    )

    def post(self, request, id):
        post = get_object_or_404(Post, id=id)
        comments = Comment.objects.filter(post=post)
        # comments = post.comments.order_by("-created_on")

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

    def get(self, request):
        # model = Post()

        return render(request, 'create_post.html',
        {
            "post_form": PostForm()
        }
        )

    def post(self, request):
        # model = Post()
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post_form.instance.name = request.user.username
            post = post_form.save(commit=False)
            post.author = get_user(request)
            post.save()
        else:
            post_form = PostForm()

        return render(request, 'create_post.html',
        {
            "post_form": PostForm()
        }
        )



