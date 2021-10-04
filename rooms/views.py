from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Room
from .serializers import ReadRoomSerializer, WriteRoomSerializer



class RoomsView(APIView):

    def get(self, request): 
        rooms = Room.objects.all()[:5]
        serializer = ReadRoomSerializer(rooms, many=True).data
        return Response(serializer)


    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=401)

        serializer = WriteRoomSerializer(data=request.data)
        # print(dir(serializer))
        if serializer.is_valid():
            room = serializer.save(user=request.user)
            room_serializer = ReadRoomSerializer(room).data
            return Response(data=room_serializer,status=200)
        else:
            print(serializer.errors)
            return Response(data=serializer.errors, status=400) 
        

# class ListRoomsView(ListAPIView):
#     """
#     View to list all rooms
#     """
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer


class RoomView(APIView):
    """
    View to retrieve a room
    """


    def get_room(self, pk):
        try:
            room = Room.objects.get(pk=pk)
            return room
        except Room.DoesNotExist:
            return None

    
    def get(self, request, pk):
        room = self.get_room(pk)
        if room is not None:
            serializer = ReadRoomSerializer(room).data
            return Response(data=serializer, status=200)
        else:
            return Response(status=404)



    def put(self, request, pk):
       pass

    def delete(self, request, pk):
        room = self.get_room(pk)
        if room.user != request.user:
            return Response(status=403)
        if room is not None:
            room.delete()
            return Response(status=200)
        else:
            return Response(status=404)