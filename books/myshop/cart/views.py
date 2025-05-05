from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from myshop.products.models import Product
from .models import CartItem, WishlistItem
from decimal import Decimal
from django.contrib import messages
from django.urls import reverse


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    
    # Remove from wishlist if it exists
    WishlistItem.objects.filter(user=request.user, product=product).delete()
    
    # Add to cart
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if created:
        cart_item.quantity = quantity
    else:
        cart_item.quantity += quantity
    cart_item.save()
    
    messages.success(request, f'{quantity} {product.name}(s) moved to your cart.')
    
    # Check the referer to determine where to redirect
    referer = request.META.get('HTTP_REFERER')
    if referer and 'wishlist' in referer:
        return redirect('cart:view_wishlist')
    elif referer and 'cart' in referer:
        return redirect('cart:view_cart')
    else:
        return redirect(reverse('product_detail', args=[product_id]))

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    total_price = Decimal(sum(item.get_total_price() for item in cart_items))

    shipping_cost = Decimal('39.90')
    total_with_shipping = total_price + shipping_cost
    tax = total_with_shipping * Decimal('0.19')  # Assuming 19% tax rate

    context = {
        'cart_items': cart_items,
        'wishlist_items': wishlist_items,
        'total_price': total_price,
        'shipping_cost': shipping_cost,
        'total_with_shipping': total_with_shipping,
        'tax': tax,
    }
    return render(request, 'cart/view_cart.html', context)

@login_required
def update_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increase':
            cart_item.quantity += 1
        elif action == 'decrease':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
        cart_item.save()
    return redirect('cart:view_cart')

@login_required
def remove_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('cart:view_cart')

@login_required
def empty_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    return redirect('cart:view_cart')

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Remove from cart if it exists
    CartItem.objects.filter(user=request.user, product=product).delete()
    
    # Add to wishlist
    WishlistItem.objects.get_or_create(user=request.user, product=product)
    
    messages.success(request, f'{product.name} moved to your wishlist.')
    
    # Check the referer to determine where to redirect
    referer = request.META.get('HTTP_REFERER')
    if referer and 'cart' in referer:
        return redirect('cart:view_cart')
    elif referer and 'wishlist' in referer:
        return redirect('cart:view_wishlist')
    else:
        return redirect(reverse('product_detail', args=[product_id]))

@login_required
def remove_from_wishlist(request, wishlist_item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=wishlist_item_id, user=request.user)
    wishlist_item.delete()
    return redirect('cart:view_wishlist')

@login_required
def view_wishlist(request):
    cart_items = CartItem.objects.filter(user=request.user)
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    wishlist_total = sum(Decimal(item.product.price) for item in wishlist_items)

    context = {
        'cart_items': cart_items,
        'wishlist_items': wishlist_items,
        'wishlist_total': wishlist_total,
    }
    return render(request, 'cart/view_wishlist.html', context)

@login_required
def add_all_to_cart(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    for wishlist_item in wishlist_items:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=wishlist_item.product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    wishlist_items.delete()
    messages.success(request, 'All items from your wishlist have been added to your cart.')
    return redirect('cart:view_cart')
