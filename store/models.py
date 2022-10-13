from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    image = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=10)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-created',)

    def __str__(self):
        return self.title


