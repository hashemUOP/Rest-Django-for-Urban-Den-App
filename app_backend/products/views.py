from rest_framework import generics
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
    queryset = Product.objects.all() #this will fetch only id
    serializer_class = ProductSerializer