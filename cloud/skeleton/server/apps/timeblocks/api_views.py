from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your API views here


class HelloApiView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'message': 'Hello, World!'
        }

        return Response(data, status=status.HTTP_200_OK)
