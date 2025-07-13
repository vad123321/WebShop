from django.urls import path, re_path
from .views import ajax_cart, ajax_cart_indicate, index, bill, confirm, delete_order

urlpatterns = [
    path('', index),
    path('ajax_cart', ajax_cart),
    path('ajax_cart_indicate', ajax_cart_indicate),
    re_path(r'^bill/(?P<sel_list>[0-9\,]+)$', bill),
    re_path(r'^confirm/(?P<init_list>[0-9\,]+)$', confirm),
    path('delete_order', delete_order),
]