from rest_framework import serializers
from .models import Room
from users.serializers import UserSerializer

class RoomSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Room
        fields = ("name", "price", "instant_book","user")

