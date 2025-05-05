# admin_panel/urls.py
from django.urls import path
from .views import (
    dashboard, product_list, product_create, product_update, product_delete,
    review_list, review_create_or_edit, review_delete, user_list, user_update, user_delete
)

urlpatterns = [
    path('', dashboard, name='admin_dashboard'),
    path('products/', product_list, name='admin_product_list'),
    path('products/create/', product_create, name='admin_product_create'),
    path('products/update/<int:pk>/', product_update, name='admin_product_update'),
    path('products/delete/<int:pk>/', product_delete, name='admin_product_delete'),
    path('reviews/', review_list, name='admin_review_list'),
    path('reviews/create/', review_create_or_edit, name='admin_review_create'),
    path('reviews/update/<int:pk>/', review_create_or_edit, name='admin_review_update'),
    path('reviews/delete/<int:pk>/', review_delete, name='admin_review_delete'),
    path('users/', user_list, name='admin_user_list'),
    path('users/update/<int:pk>/', user_update, name='admin_user_update'),
    path('users/delete/<int:pk>/', user_delete, name='admin_user_delete'),
]
