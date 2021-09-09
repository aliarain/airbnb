from rest_framework import viewsets
from .models import Room
from .serializers import BigRoomSerializers

class RoomViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing rooms.
    """
    queryset = Room.objects.all()
    serializer_class = BigRoomSerializers