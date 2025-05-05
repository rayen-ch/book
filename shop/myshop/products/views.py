from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.db.models import Avg, Q
from django.contrib import messages
from myshop.reviews.models import Review
from myshop.reviews.forms import ReviewForm



def product_list(request):
    products = Product.objects.all()
    for product in products:
        product.discounted_price = get_discounted_price(product)
        product.stock_status = get_stock_status(product)
    context = {
        'products': products,
        'EMPTY_STOCK': EMPTY_STOCK,
        'LIMITED_STOCK_STATUS': LIMITED_STOCK_STATUS,
    }  
    return render(request, 'products/product_list.html', context)


def average_rating(self):
    return self.reviews.aggregate(Avg('rating'))['rating__avg']

from django.contrib.auth.decorators import login_required

def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    user_review = None
    form = None

    if request.user.is_authenticated:
        user_review = Review.objects.filter(product=product, user=request.user).first()
        
        if request.method == 'POST':
            if 'review_action' in request.POST:
                if request.POST['review_action'] == 'create_or_edit':
                    form = ReviewForm(request.POST, instance=user_review)
                    if form.is_valid():
                        review = form.save(commit=False)
                        review.product = product
                        review.user = request.user
                        review.save()
                        messages.success(request, 'Your review has been submitted successfully.')
                    else:
                        messages.error(request, 'There was an error with your review. Please try again.')
                elif request.POST['review_action'] == 'delete':
                    if user_review:
                        user_review.delete()
                        messages.success(request, 'Your review has been deleted successfully.')
                    else:
                        messages.error(request, 'You can only delete your own reviews.')
            return redirect('product_detail', pk=pk)

        form = ReviewForm(instance=user_review)

    # Handle sorting of reviews
    sort = request.GET.get('sort', 'date-desc')
    if sort == 'date-asc':
        reviews = product.reviews.all().order_by('created_at')
    elif sort == 'rating-desc':
        reviews = product.reviews.all().order_by('-rating')
    elif sort == 'rating-asc':
        reviews = product.reviews.all().order_by('rating')
    else:  # 'date-desc' or default
        reviews = product.reviews.all().order_by('-created_at')

    product.discounted_price = get_discounted_price(product)
    product.stock_status = get_stock_status(product)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]

    context = {
        'product': product,
        'EMPTY_STOCK': EMPTY_STOCK,
        'LIMITED_STOCK_STATUS': LIMITED_STOCK_STATUS,
        'user_review': user_review,
        'review_form': form,
        'related_products': related_products,
        'reviews': reviews,
        'sort': sort,
    }
    return render(request, 'products/product_detail.html', context)


EMPTY_STOCK = "This product is not available at the moment"
LIMITED_STOCK_STATUS = "Limited products available"
IN_STOCK = "This product is available"

def get_discounted_price(product):
    if product.discount:
        return product.price * (1 - product.discount / 100)
    return product.price

def get_stock_status(product):
    if product.stock == 0:
        return EMPTY_STOCK
    elif product.stock < 5:
        return LIMITED_STOCK_STATUS
    else:
        return IN_STOCK

def romance_list(request):
    category = get_object_or_404(Category, name='Romance')
    romances = Product.objects.filter(category=category)
    for roma in romances:
        roma.discounted_price = get_discounted_price(roma)
        roma.stock_status = get_stock_status(roma)
    context = {
        'products': romances,
        'category_name': 'Romance',
        'EMPTY_STOCK': EMPTY_STOCK,
        'LIMITED_STOCK_STATUS': LIMITED_STOCK_STATUS,
    }
    return render(request, 'products/romance_list.html', context)

def sciFi_list(request):
    category = get_object_or_404(Category, name='Sci-Fi')
    scis = Product.objects.filter(category=category)
    for sci in scis:
        sci.discounted_price = get_discounted_price(sci)
        sci.stock_status = get_stock_status(sci)
    context = {
        'products': scis,
        'category_name': 'Sci-Fi',
        'EMPTY_STOCK': EMPTY_STOCK,
        'LIMITED_STOCK_STATUS': LIMITED_STOCK_STATUS,
    }
    return render(request, 'products/sciFi_list.html', context)

def horror_list(request):
    category = get_object_or_404(Category, name='Horror')
    horror = Product.objects.filter(category=category)
    for item in horror:
        item.discounted_price = get_discounted_price(item)
        item.stock_status = get_stock_status(item)
    context = {
        'products': horror,
        'category_name': 'Horror',
        'EMPTY_STOCK': EMPTY_STOCK,
        'LIMITED_STOCK_STATUS': LIMITED_STOCK_STATUS,
    }
    return render(request, 'products/horror_list.html', context)

def thriller_list(request):
    category = get_object_or_404(Category, name='Thriller')
    products = Product.objects.filter(category=category)
    for product in products:
        product.discounted_price = get_discounted_price(product)
        product.stock_status = get_stock_status(product)
    context = {
        'products': products,
        'category_name': 'Thriller',
        'EMPTY_STOCK': EMPTY_STOCK,
        'LIMITED_STOCK_STATUS': LIMITED_STOCK_STATUS,
    }
    return render(request, 'products/thriller_list.html', context)

def adventure_list(request):
    category = get_object_or_404(Category, name='Adventure')
    products = Product.objects.filter(category=category)
    for product in products:
        product.discounted_price = get_discounted_price(product)
        product.stock_status = get_stock_status(product)
    context = {
        'products': products,
        'category_name': 'Adventure',
        'EMPTY_STOCK': EMPTY_STOCK,
        'LIMITED_STOCK_STATUS': LIMITED_STOCK_STATUS,
    }
    return render(request, 'products/adventure_list.html', context)

# search view
def search_products(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(reviews__rating__icontains=query)
        ).distinct()
    else:
        products = Product.objects.all()

    for product in products:
        product.discounted_price = get_discounted_price(product)
        product.stock_status = get_stock_status(product)

    context = {
        'products': products,
        'query': query,
        'EMPTY_STOCK': EMPTY_STOCK,
        'LIMITED_STOCK_STATUS': LIMITED_STOCK_STATUS,
    }
    return render(request, 'products/search_results.html', context)