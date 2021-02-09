from django.forms import modelformset_factory
from django.shortcuts import render, redirect

from mainsite.forms import ProductForm, ProductPictureForm
from mainsite.models import Product, ProductPicture
from mainsite.views.categoryfn import category_fn


def edit(request, pk):
    ImageFormSet = modelformset_factory(ProductPicture, form=ProductPictureForm, extra=4)

    product = Product.objects.get(pk=pk)
    categories = category_fn()
    id = request.user.id

    formset = ImageFormSet(queryset=ProductPicture.objects.none())
    if request.method == 'GET':
        form = ProductForm(instance=product)
        formset = ImageFormSet(queryset=ProductPicture.objects.none())
        context = {
            'form': form,
            'categories': categories,
            'product': product,
            'id': id,
            'formset': formset,

        }
        return render(request, 'edit_product.html', context)

    else:
        form = ProductForm(request.POST, instance=product)
        formset = ImageFormSet(request.POST, request.FILES, queryset=ProductPicture.objects.none())

        if form.is_valid() and formset.is_valid():
            product = form.save(commit=False)  # Setting foreign key
            product.save()

            for f in formset.cleaned_data:
                if f:
                    image = f['image']
                    photo = ProductPicture(product=product, images=image)
                    photo.save()
            return redirect('index')
        form = ProductForm(instance=product)
        context = {
            'form': form,
            'formset': formset,
            'categories':categories,
        }
        return render(request, 'create_product.html', context)