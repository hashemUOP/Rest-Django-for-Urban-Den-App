from django.contrib.auth.models import User
from django.db import models
from products.models import Product


# Create your models here.
class ReviewsModels(models.Model):
    review_id = models.AutoField(primary_key=True)
    review_title = models.CharField(max_length=200)
    review_content = models.TextField()
    review_rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    firestore_user_uid = models.CharField(max_length=300,null=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return "title: "+self.review_title+" user id: "+self.firestore_user_uid
