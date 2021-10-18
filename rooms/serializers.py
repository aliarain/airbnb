from rest_framework import serializers
from .models import Room
from users.serializers import RelatedUserSerializer

class RoomSerializer(serializers.ModelSerializer):

    user = RelatedUserSerializer()
    class Meta:
        model = Room
        exclude = ["modified"]
        read_only_fields = ("id", "user", "created" , "updated")

    def validate(self, data):
        if self.instance:
            check_in = data.get("check_in", self.instance.check_in)
            check_out = data.get("check_out", self.instance.check_out)
        else:
            check_in = data.get('check_in')
            check_out = data.get('check_out')
            if check_in == check_out:
                raise serializers.ValidationError("Check in must be before check out")

        return data




# class BigRoomSerializers(serializers.ModelSerializer):

#     class Meta:
#         model = Room
#         exclude = ()