from rest_framework import serializers
from .models import Room
from users.serializers import UserSerializer

class ReadRoomSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Room
        exclude = ()

class WriteRoomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=140)
    address = serializers.CharField(max_length=140)
    price = serializers.IntegerField(help_text="USD per night")
    beds = serializers.IntegerField(default=1)
    lat = serializers.DecimalField(max_digits=10, decimal_places=6)
    lng = serializers.DecimalField(max_digits=10, decimal_places=6)
    bedrooms = serializers.IntegerField(default=1)
    bathrooms = serializers.IntegerField(default=1)
    check_in = serializers.TimeField(default="00:00:00")
    check_out = serializers.TimeField(default="00:00:00")
    instant_book = serializers.BooleanField(default=False)
    

    def create(self, validated_data):
        print(validated_data)
        return Room.objects.create(**validated_data)
    






# class BigRoomSerializers(serializers.ModelSerializer):

#     class Meta:
#         model = Room
#         exclude = ()