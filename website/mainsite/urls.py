from django.urls import path
from mainsite.views import categories, search, cart_view, indexviews, create_product_view, profile_view, edit_view, \
    delete_item, checkout

urlpatterns = [
    path('', indexviews.index, name='index'),
    path('product/<int:pk>', indexviews.product, name='product'),
    path('create/<int:pk>', create_product_view.create_product, name='create'),
    path('profile/<int:pk>', profile_view.profile, name='profile'),
    path('cart/<int:pk>', cart_view.add_to_cart, name='add_to_cart'),
    path('edit/<int:pk>', edit_view.edit, name='edit_item'),
    path('remove/<int:pk>', cart_view.remove_from_cart, name='remove_from_cart'),
    path('search/', search.search, name='search'),
    path('category/<str:category>', categories.category_view, name='category_view'),
    path('delete/<int:pk>', delete_item.delete, name='delete item'),
    path('checkout', checkout.checkout, name='checkout'),
    path('order/<int:pk>', checkout.order, name='order'),

]