from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'description','rating','owner','bought_on','updated_on')
        model = Game