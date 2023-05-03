from django.urls import path
from .views import GameList, GameDetail, GameCreate

urlpatterns = [
    path('', GameList.as_view(), name='game_list'),
    path('<int:pk>', GameDetail.as_view(), name='game_detail'),
    path('create/', GameCreate.as_view(), name='game_create'),

]