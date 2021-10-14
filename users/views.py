from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer


class MeView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return Response(UserSerializer(request.user).data)

    def put(self, request):
        pass


@api_view(["GET"])
class user_detail():
    pass