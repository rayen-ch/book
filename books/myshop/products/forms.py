from django import forms
from .models import Product, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'autor', 'description', 'price', 'discount', 'stock', 'category', 'featured']

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']

ProductImageFormSet = forms.inlineformset_factory(Product, ProductImage, form=ProductImageForm, fields=['image'], extra=1, can_delete=True)
