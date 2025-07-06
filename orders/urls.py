from django.urls import path
from .views import ajax_cart

urlpatterns = [
    path('ajax_cart', ajax_cart)
]