from django.urls import path
from .views import add_to_cart, view_cart, update_cart_item, empty_cart, remove_cart_item, add_to_wishlist, remove_from_wishlist, view_wishlist, add_all_to_cart


app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('', view_cart, name='view_cart'),
    path('update/<int:cart_item_id>/', update_cart_item, name='update_cart_item'),
    path('remove/<int:cart_item_id>/', remove_cart_item, name='remove_cart_item'),
    path('empty/', empty_cart, name='empty_cart'),
    path('wishlist/add/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:wishlist_item_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/', view_wishlist, name='view_wishlist'),
    path('add-all-to-cart/', add_all_to_cart, name='add_all_to_cart'),
]
