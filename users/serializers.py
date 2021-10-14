from rest_framework import serializers
from .models import User

class RelatedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'avatar',
            'superhost'

        )

class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
    exclude = (
        'password',
        'last_login', 
        'is_superuser',
        'groups',
        'user_permission',
        'is_staff',
        'is_active',
        'date_joined',
    )
