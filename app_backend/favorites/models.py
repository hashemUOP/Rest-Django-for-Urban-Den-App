from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from reviews.models import ReviewsModels

class Favorite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')  # this prevents user duplicating the products in favorite

    def __str__(self):
        return f"Favorite: {self.user.username} - {self.product.name}"
