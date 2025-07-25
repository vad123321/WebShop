from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup),
    path('signin', views.signin),
    path('signout', views.signout),
    path('profile', views.profile),
    path('ajaxreg', views.ajaxreg),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
]