from django.db.migrations import serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserDetailView(APIView):
    #difference between the two below:
    #this tells DRF:only allow access to this view if the request has an authenticated user.
    permission_classes = [IsAuthenticated]
    #this tells DRF:Look at the incoming request’s headers for a token.
    #If you find a valid token, associate the request with the corresponding user
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

