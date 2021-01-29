from django.contrib.auth.models import User
from django.shortcuts import render


def profile(request, pk):
    if request.method == 'GET':
        owner = User.objects.get(pk=pk)
        products = owner.product_set.all()
        context = {
            'products': products,
            'owner': owner,
        }
        return render(request, 'profile.html', context)