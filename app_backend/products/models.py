from django.db import models

CATEGORY_CHOICES = [
    ('chair', 'Chair'),
    ('table', 'Table'),
    ('sofa', 'Sofa'),
    ('lamp', 'Lamp'),
    ('stools', 'Stools'),
]


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    materials = models.TextField(blank=True)
    isHot = models.BooleanField(default=False)

    img1 = models.URLField(blank=True, null=True)
    img2 = models.URLField(blank=True, null=True)
    img3 = models.URLField(blank=True, null=True)
    img4 = models.URLField(blank=True, null=True)
    img5 = models.URLField(blank=True, null=True)

    specifications = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "product name: "+self.name+" product id: "+str(self.product_id)
