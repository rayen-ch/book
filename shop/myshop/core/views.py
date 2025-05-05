from django.shortcuts import render
from myshop.products.models import Product

def home(request):
    featured_products = Product.objects.filter(featured=True)[:5]  # Assuming you have a 'featured' field
    latest_products = Product.objects.order_by('-created_at')[:4]  # Showing 4 latest products
    
    context = {
        'featured_products': featured_products,
        'latest_products': latest_products,
    }
    return render(request, 'core/home.html', context)