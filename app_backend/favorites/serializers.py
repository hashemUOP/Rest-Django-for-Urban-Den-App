# favorites/serializers.py

from rest_framework import serializers
from .models import Favorite

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'product', 'user']
        extra_kwargs = {
            'user': {'read_only': True},
        }
