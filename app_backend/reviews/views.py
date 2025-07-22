from django.shortcuts import render
from rest_framework import generics
from .models import ReviewsModels
from .serializers import ReviewSerializers


# Create your views here.
class ReviewCreation(generics.CreateAPIView):
    queryset = ReviewsModels.objects.all()
    serializer_class = ReviewSerializers

class ReviewList(generics.ListAPIView):
    queryset = ReviewsModels.objects.all()
    serializer_class = ReviewSerializers
    # from pip install django-filter,filterset_fields = ['product_id']: “If the client passes in url data like
    # ?product_id=…, filter the queryset by that field automatically.”
    filterset_fields = ['product_id']

#http://192.168.0.1/api/reviews/?product_id = 5