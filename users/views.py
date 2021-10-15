from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from .serializers import UserSerializer , WriteUserSerializer
from .models import User


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
