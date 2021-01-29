from django.shortcuts import render

from mainsite.models import Product


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)


def product(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        context={
            'product': product
        }
        return render(request, 'product.html', context)
