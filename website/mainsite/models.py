from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Product(models.Model):
    cat = (
        ('Electronic', 'Electronic'),
        ('Clothing', 'Clothing'),
        ('Automobiles', 'Automobiles'),
        ('Sport', 'Sport'),
        ('Books', 'Books'),
        ('Services', 'Services'),
        ('Other', 'Other')
    )
    product_name = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=200, blank=False)
    category = models.CharField(max_length=30, choices=cat, blank=False)
    price = models.FloatField(blank=False)
    image_url = models.URLField(blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)