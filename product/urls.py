from django.urls import path
from . import views

urlpatterns = [
    path('clothing/', views.ClothingDisplay, name='clothing'),
    path('electronics/', views.ElectronicsDisplay, name='electronics'),
    path('sports/', views.SportsDisplay, name='sports'),
    path('education/', views.EducationDisplay, name='education'),
    path('product_view/<int:pk>',views.ProductView.as_view(), name='product_view'),

]