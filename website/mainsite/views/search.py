from django.shortcuts import render

from mainsite.models import Product


def search(request):
    query = request.GET['q']
    products = Product.objects.all()
    matched = []
    for product in products:
        if query.lower() in product.product_name.lower() or query.lower() in product.description.lower():
            matched.append(product)
    context={
        'query': query,
        'matched': matched,
    }
    return render(request, 'search.html', context)