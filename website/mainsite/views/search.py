from django.shortcuts import render
from mainsite.models import Product
from mainsite.views.categoryfn import category_fn


def search(request):
    query = request.GET['q']
    products = Product.objects.all()
    categories = category_fn()
    matched = []
    for product in products:
        if query.lower() in product.product_name.lower() or query.lower() in product.description.lower():
            matched.append(product)
    context={
        'query': query,
        'matched': matched,
        'categories': categories,
    }
    return render(request, 'search.html', context)