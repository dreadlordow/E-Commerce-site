from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from mainsite.forms import ProductForm
from mainsite.views.categoryfn import category_fn


def create_product(request, pk):
    categories = category_fn()
    if request.method == 'GET':
        form = ProductForm()
        context = {
            'form': form,
            'categories': categories,
        }
        return render(request, 'create_product.html', context)
    else:
        owner = User.objects.get(pk=pk)
        form = ProductForm(request.POST)

        if form.is_valid():
            new = form.save(commit=False)
            new.owner = owner
            new.save()
            return redirect('index')

        form = ProductForm()
        context = {
            'form': form,
            'categories':categories,
        }
        return render(request, 'create_product.html', context)