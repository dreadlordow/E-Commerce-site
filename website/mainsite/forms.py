from django import forms
from django.contrib.auth.models import User
from django.forms import HiddenInput

from mainsite.models import Product, Cart, Order, Comment


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


class SortForm(forms.Form):
    choices = (
        ('date_added', 'Date Ascending'),
        ('-date_added', 'Date Descending'),
        ('price', 'Price Ascending'),
        ('-price', 'Price Descending'),
        ('product_name', 'Name A-Z'),
        ('-product_name', 'Name Z-A'),
    )
    order = forms.ChoiceField(choices=choices)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('user', 'product')