from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base, name='base'),
    path('today', views.today, name='today'),
    path('error', views.error, name='error'),
    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('market', views.category_market, name='category_market'),
    path('checkout', views.checkout, name='checkout'),
    path('coming-soon', views.coming_soon, name='coming_soon'),
    path('contact', views.contact, name='contact'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('faq', views.faq, name='faq'),
    path('login', views.login, name='login'),
    path('single-blog', views.single_blog, name='single_blog'),
    path('wishlist', views.wishlist, name='wishlist'),


]
