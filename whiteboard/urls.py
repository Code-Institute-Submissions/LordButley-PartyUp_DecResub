from . import views
from django.urls import path

urlpatterns = [
    path('', views.GameList.as_view(), name='home'),
    path('game_page/<slug:ref_name>', views.GamePostList.as_view(), name='game_page'),
    path('<slug:id>', views.GameComment.as_view(), name='game_comment'),
]