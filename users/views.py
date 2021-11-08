from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view , permission_classes
from .serializers import UserSerializer , WriteUserSerializer
from rooms.serializers import RoomSerializer
from .models import User
from rooms.models import Room

class MeView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        return Response(UserSerializer(request.user).data)

    def put(self, request):
        serializer = WriteUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


@api_view(["GET"])
def user_detail(request, pk ):
    try:
        user = User.objects.get(pk=pk)
        return Response(UserSerializer(user).data)
    except User.DoesNotExist:
        return Response(status=404)



class FavView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        user = request.user
        serliazer = RoomSerializer(user.favs.all(), many=True).data
        return Response(serliazer)

    def put(self, request):
        pk = request.data.get("pk", None)
        user = request.user
        if pk is not None:
            try:
                room = Room.objects.get(pk=pk)
                if room in user.favs.all():
                    user.favs.remove(room)
                else:
                    user.favs.add(room)
                user.save()
                return Response(status=200)
            except Room.DoesNotExist:
                pass
            return Response(status=400)