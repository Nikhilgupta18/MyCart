from django.urls import path
from . import views

urlpatterns = [
    path('clothing/', views.Clothing_Display, name='clothing'),
    path('electronics/', views.Electronics_Display, name='electronics'),
    path('sports/', views.Sports_Display, name='sports'),
    path('education/', views.Education_Display, name='education'),
]