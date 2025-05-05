from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings  # importing settings to get the custom user model
from django.db.models import Avg



class Category(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=255)
  autor= models.CharField(max_length=100, blank=True, null=True, default='Unknown')
  description = models.TextField()
  price = models.FloatField()
  # image = models.ImageField(upload_to='products/')
  #pdf = models.FileField(upload_to='products/pdfs/')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  cart = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='cart_products', blank=True)
  wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wishlist_products', blank=True)
  discount = models.IntegerField(default=0)
  stock = models.IntegerField(default=0)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  featured = models.BooleanField(default=False)  # New field

  def average_rating(self):
    return self.reviews.aggregate(average=Avg('rating'))['average'] or 0.0


  def __str__(self):
    return self.name
  

class ProductImage(models.Model):
  product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
  image = models.ImageField(upload_to='products/')
  
  def __str__(self):
    return f"{self.product.name} Image"