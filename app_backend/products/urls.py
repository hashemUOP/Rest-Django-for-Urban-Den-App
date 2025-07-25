from django.urls import path
from .views import ProductViewSet,ProductDetail

urlpatterns = [

    #this view is triggered when client send http://ip4address/api/products/5
    path('<int:pk>/',ProductDetail.as_view(), name='product-detail'),

    # this view is triggered when client send http://ip4address/api/products/?category = chair
    path('', ProductViewSet.as_view(), name='products_list')
]
