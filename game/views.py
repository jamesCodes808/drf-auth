from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Game
from .serializer import GameSerializer
from .permissions import isOwnerOrReadOnly

class GameList(ListAPIView):
    # permission_classes = (isOwnerOrReadOnly,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameCreate(CreateAPIView):
    # permission_classes = (isOwnerOrReadOnly,)
    serializer_class = GameSerializer

class GameDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (isOwnerOrReadOnly,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer