from django.urls import path, include
from . import views

urlpatterns = [
  path('home/', views.product_list, name='product_list'),
  path('article/<int:pk>/', views.product_detail, name='product_detail'),
  path('Romance/', views.romance_list, name='romance_list'),
  path('Sci-Fi/', views.sciFi_list, name='sciFi_list'),
  path('Horror/', views.horror_list, name='horror_list'),
  path('search/', views.search_products, name='search_products'),
  path('thriller/', views.thriller_list, name='thriller_list'),
  path('adventure/', views.adventure_list, name='adventure_list'),
]
