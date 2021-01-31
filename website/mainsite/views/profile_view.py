from django.contrib.auth.models import User
from django.shortcuts import render

from mainsite.views.categoryfn import category_fn


def profile(request, pk):
    if request.method == 'GET':
        owner = User.objects.get(pk=pk)
        products = owner.product_set.all()
        categories = category_fn()
        context = {
            'products': products,
            'owner': owner,
            'categories': categories,
        }
        return render(request, 'profile.html', context)