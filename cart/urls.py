from django.urls import path
from . import views

urlpatterns = [
   path('cart_home',views.cart, name='cart'),

]