from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from mainsite.forms import SortForm, CommentForm
from mainsite.models import Product, Comment
from mainsite.views.categoryfn import category_fn


def extract_filter_value(params):
    order = params['order'] if 'order' in params else 'date_added'
    return order


def index(request):
    order = extract_filter_value(request.GET)
    products = Product.objects.all().order_by(order)
    form = SortForm()
    categories = category_fn()
    context = {
        'products': products,
        'categories': categories,
        'form': form,
        'sort_form' : SortForm(),
    }
    return render(request, 'index.html', context)


def product(request, pk, slug=None):
    product = Product.objects.get(pk=pk)
    if request.method == 'GET':
        if slug and product.product_name.lower() != slug.lower():
            return redirect('404')

        comment_form = CommentForm()
        product_comments = [c for c in Comment.objects.filter(product_id=pk)]
        owner = User.objects.get(pk=product.owner_id)
        context={
            'product': product,
            'owner': owner,
            'comment_form': comment_form,
            'product_comments': product_comments,
        }
        return render(request, 'single_product.html', context)

    else:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            product_comments = [c for c in Comment.objects.filter(product_id=pk)]
            owner = User.objects.get(pk=product.owner_id)
            context = {
                'product': product,
                'owner': owner,
                'comment_form': CommentForm(),
                'product_comments': product_comments,
            }
            return render(request, 'single_product.html', context)
