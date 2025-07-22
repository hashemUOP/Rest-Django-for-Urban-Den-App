from django.urls import path
from .views import ReviewCreation,ReviewList
urlpatterns = [
    path('create/',ReviewCreation.as_view(), name='review_creation'),

    path('', ReviewList.as_view(), name='review_list')
]
