from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from mainsite.forms import CartForm
from mainsite.models import Cart, Product


def add_to_cart(request, pk):
    user = User.objects.get(pk=pk)
    my_cart = Cart.objects.get_or_create(user=user)[0]
    if request.method == 'POST':
        product_id = request.POST['add']
        product = Product.objects.get(pk=product_id)
        my_cart.products.add(product)
        return redirect('index')

    else:
        products = my_cart.products.all()
        context= {
            'products': products,
            'cart_pk': pk
        }
        return render(request, 'cart.html', context)


def remove_from_cart(request, pk):
    if request.method == 'GET':
        cart_pk = request.GET['delete']
        cart = Cart.objects.get(user_id=cart_pk)
        product = Product.objects.get(pk=pk)
        cart.products.remove(product)

        products = cart.products.all()
        context = {
            'products': products,
            'cart_pk': pk
        }
        return render(request, 'cart.html', context)