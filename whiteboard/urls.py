from . import views
from django.urls import path

urlpatterns = [
    path('', views.GameList.as_view(), name='home'),
    path('dead_by_daylight', views.DeadByDaylight.as_view(), name="dead_by_daylight"),
    path('rocket_league', views.RocketLeague.as_view(), name="rocket_league")
]