from .models import ReviewsModels
from rest_framework import serializers

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReviewsModels
        fields =  ['review_id','review_title','review_content','created_at','review_rating','firestore_user_uid','product_id']