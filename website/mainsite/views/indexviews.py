from django.shortcuts import render

from mainsite.models import Product
from mainsite.views.categoryfn import category_fn


def index(request):
    products = Product.objects.all()
    categories = category_fn()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context)


def product(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        context={
            'product': product
        }
        return render(request, 'product.html', context)
