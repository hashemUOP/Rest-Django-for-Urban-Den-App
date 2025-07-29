# favorites/views.py

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Favorite
from .serializers import FavoritesSerializer

@method_decorator(csrf_exempt, name='dispatch')
class GetFavoritesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Favorite.objects.filter(user=request.user)
        serializer = FavoritesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class PostFavoriteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FavoritesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        product_id = request.query_params.get('product_id')
        try:
            fav = Favorite.objects.get(user=request.user, product_id=product_id)
            fav.delete()
            return Response({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)

        except Favorite.DoesNotExist:
            return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)



