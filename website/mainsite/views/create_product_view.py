from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from mainsite.forms import ProductForm
from mainsite.views.categoryfn import category_fn


@login_required(login_url='login')
def create_product(request):
    categories = category_fn()
    if request.method == 'GET':
        form = ProductForm()
        context = {
            'form': form,
            'categories': categories,
        }
        return render(request, 'create_product.html', context)
    else:
        owner = request.user
        form = ProductForm(request.POST)

        if form.is_valid():
            new = form.save(commit=False) # Setting foreign key
            new.owner = owner
            new.save()
            return redirect('index')

        form = ProductForm()
        context = {
            'form': form,
            'categories':categories,
        }
        return render(request, 'create_product.html', context)