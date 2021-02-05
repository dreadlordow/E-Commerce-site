from django.shortcuts import render
from django.views.generic import ListView

from mainsite.models import Product
from mainsite.views.categoryfn import category_fn


# def search(request):
#     query = request.GET['q']
#     products = Product.objects.filter(
#         product_name__icontains=query) | Product.objects.filter(description__icontains=query)
#     categories = category_fn()
#
#     context = {
#         'query': query,
#         'matched': products,
#         'categories': categories,
#     }
#     return render(request, 'search.html', context)

class SearchView(ListView):
    template_name = 'search.html'
    model = Product
    context_object_name = 'products'


    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        categories = category_fn()
        context['query'] = query
        context['categories'] = categories

        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = None
        if query:
            object_list = Product.objects.filter(product_name__icontains=query) | Product.objects.filter(description__icontains=query)

        return object_list

