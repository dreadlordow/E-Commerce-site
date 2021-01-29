from django.urls import path
from mainsite.views import cart_view, indexviews, create_product_view, profile_view
urlpatterns = [
    path('', indexviews.index, name='index'),
    path('product/<int:pk>', indexviews.product, name='product'),
    path('create/<int:pk>', create_product_view.create_product, name='create'),
    path('profile/<int:pk>', profile_view.profile, name='profile'),
    path('cart/<int:pk>', cart_view.add_to_cart, name='add_to_cart'),
    path('remove/<int:pk>', cart_view.remove_from_cart, name='remove_from_cart')
]