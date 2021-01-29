
from django.contrib import admin
from django.urls import path, include

from register.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainsite.urls')),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),

]
