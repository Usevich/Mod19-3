from django.urls import path, include
from .views import index_view, shop_view, cart_view
from .views import register_buyer, list_games

urlpatterns = [
    path('', index_view, name='home'),
    path('shop/', shop_view, name='shop'),
    path('cart/', cart_view, name='cart'),
    path('register/', register_buyer, name='register'),
    path('games/', list_games, name='list_games'),
]
