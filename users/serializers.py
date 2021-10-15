from rest_framework import serializers
from .models import User

class RelatedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'avatar', 'superhost')

class WriteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =(
            'username',
            'email',
            'first_name',
            'last_name',
            'avatar',
        )