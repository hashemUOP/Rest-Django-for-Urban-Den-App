from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(generics.ListAPIView):
    def get_queryset(self):
        category = self.request.query_params.get('category')
        if category:
            return Product.objects.filter(category__iexact=category)
        return Product.objects.all()

    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductInstance(APIView):
    def get(self, request, *args, **kwargs):
        instance = Product.objects.get(pk=kwargs['pk'])
        serializer = ProductSerializer(instance)
        return Response(serializer.data)