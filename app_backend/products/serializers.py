from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'product_id',
            'name',
            'description',
            'price',
            'materials',
            'isHot',
            'img1',
            'img2',
            'img3',
            'img4',
            'img5',
            'specifications',
            'category',
            'created_at',
        ]
        read_only_fields = ['created_at']
