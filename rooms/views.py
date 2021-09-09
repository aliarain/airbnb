from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Room
from .serializers import ReadRoomSerializer, WriteRoomSerializer


@api_view(['GET', 'POST'])
def room_view(request):
    """
    List all rooms, or create a new room.
    """
    if request.method == 'GET':
        rooms = Room.objects.all()[:5]
        serializer = ReadRoomSerializer(rooms, many=True).data
        return Response(serializer)
    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response(status=401)

        serializer = WriteRoomSerializer(data=request.data)
        # print(dir(serializer))
        if serializer.is_valid():
            room = serializer.save(user=request.user)
            room_serializer = ReadRoomSerializer(room).data
            return Response(data=room_serializer,status=200)
        else:
            return Response(status=400)







# class ListRoomsView(ListAPIView):
#     """
#     View to list all rooms
#     """
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer


class SeeRoomView(RetrieveAPIView):
    """
    View to retrieve a room
    """
    queryset = Room.objects.all()
    serializer_class = ReadRoomSerializer