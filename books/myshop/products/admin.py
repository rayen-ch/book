from django.contrib import admin
from .models import Product, ProductImage, Category

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image']

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ['name', 'autor', 'price', 'stock', 'discount']  # Added 'autor'
    search_fields = ('name', 'description', 'autor')  # Included 'autor' in search
    list_filter = ('category',)  # You can filter by category
    fields = ['name', 'autor', 'description', 'price', 'discount', 'stock', 'category', 'featured']  # Added 'autor' to fields

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Category)
