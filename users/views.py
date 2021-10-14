from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ReadUserSerializer


class MeView(APIView):
    def get(self, request):
        if request.user.is_authenticated():
            return Response(ReadUserSerializer(request.user).data)

    def put(self, request):
        pass


@api_view(["GET"])
def user_detail():
    pass