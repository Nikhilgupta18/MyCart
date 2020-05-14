from django.urls import path
from . import views

urlpatterns = [
   path('',views.cart, name='cart'),
   path('update/',views.cart_update, name='cart-update'),

]