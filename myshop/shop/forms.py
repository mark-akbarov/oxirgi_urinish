from django import forms
from .models import Product


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'image', 'description', 'available', 'total_quantity', 'sold_quantity']
