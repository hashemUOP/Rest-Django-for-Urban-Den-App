from django.urls import path
from .views import GetFavoritesView,PostFavoriteView,DeleteFavoriteView

urlpatterns = [
    path('get/',GetFavoritesView.as_view(),name='get_favorites'),
    path('post/',PostFavoriteView.as_view(),name='post_favorites'),
    path('delete/',DeleteFavoriteView.as_view(),name='delete_favorites'),
]