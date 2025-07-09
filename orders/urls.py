from django.urls import path
from .views import ajax_cart, ajax_cart_indicate, index

urlpatterns = [
    path('', index),
    path('ajax_cart', ajax_cart),
    path('ajax_cart_indicate', ajax_cart_indicate),
]