from django.urls import path
from . import views


urlpatterns = [
    path('', views.GameList.as_view(), name='home'),
    path('game_page/<slug:ref_name>',
         views.GamePostList.as_view(), name='game_page'),
    path('post_page/<slug:id>', views.GameComment.as_view(), name='post_page'),
    path('create_post/<slug:ref_name>',
         views.CreatePost.as_view(), name='create_post'),
    path('edit_post/<slug:id>', views.EditPost.as_view(), name='edit_post'),
    path('delete_post/<slug:id>', views.delete_post, name='delete_post'),
    path('delete_comment/<slug:id>',
         views.delete_comment, name='delete_comment')
]
