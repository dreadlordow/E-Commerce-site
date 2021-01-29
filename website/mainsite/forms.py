from django import forms
from django.forms import HiddenInput

from mainsite.models import Product, Cart


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('owner',)


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'
