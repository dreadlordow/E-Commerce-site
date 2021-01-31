from django.shortcuts import render

from mainsite.models import Product
from mainsite.views.categoryfn import category_fn


def category_view(request, category):
    category = category
    categories = category_fn()
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products,
        'categories': categories,
        'len': len(products),
    }
    return render(request, 'category.html', context)