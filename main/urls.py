from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('search/', views.search_results, name='search'),
    path('change-password/', views.change_password, name='change_password'),
    path('reset-password/', views.user_search_reset_password, name='user_search_reset_password'),
#     path('download/<str:query>', views.download_data, name='download'),
]