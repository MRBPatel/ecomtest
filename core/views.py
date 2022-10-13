from django.shortcuts import render


# Create your views here.


def base(request):
    return render(request, 'base.html')


def index(request):
    return render(request, 'index.html')


def today(request):
    return render(request, 'store/products/trending_today.html')


def error(request):
    return render(request, '404.html')


def about(request):
    return render(request, 'about.html')


def cart(request):
    return render(request, 'store/basket/cart.html')


def product_list(request):
    return render(request, 'store/products/product_list.html')


def category_market(request):
    return render(request, 'store/products/category-market.html')


def checkout(request):
    return render(request, 'checkout.html')


def coming_soon(request):
    return render(request, 'coming-soon.html')


def contact(request):
    return render(request, 'contact.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def faq(request):
    return render(request, 'faq.html')


def login(request):
    return render(request, 'login.html')


def product(request):
    return render(request, 'store/products/product.html')


def single_blog(request):
    return render(request, 'store/products/single.html')


def wishlist(request):
    return render(request, 'wishlist.html')

