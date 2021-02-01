from django import forms
from django.contrib.auth.models import User
from django.forms import HiddenInput

from mainsite.models import Product, Cart, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('owner',)


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'


class OrderForm(forms.ModelForm):
    telephone = forms.CharField(min_length=13, max_length=13, initial='+359')

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'telephone', 'address')
        exclude=('user', 'date')
