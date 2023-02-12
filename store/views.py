from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product


# Create your views here.

def product_list(request):
    product_all = Product.objects.all()
    context = {
        'product': product_all
    }
    return render(request, 'templates/store/products/product_list.html', context)


def product(request, slug):
    single_product = Product.objects.get(slug=slug)
    context = {
        'product': single_product,
    }
    return render(request, 'templates/store/products/product.html', context)
