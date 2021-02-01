from django.shortcuts import render, redirect

from mainsite.forms import ProductForm
from mainsite.models import Product
from mainsite.views.categoryfn import category_fn


def edit(request, pk):
    product = Product.objects.get(pk=pk)
    categories = category_fn()
    if request.method == 'GET':
        form = ProductForm(instance=product)
        context = {
            'form': form,
            'categories': categories,
            'product': product,
        }
        return render(request, 'edit_product.html', )

    else:
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')