from django.urls import path

from store import views

app_name = 'store'

urlpatterns = [
    path('<slug:slug>', views.product, name='product'),
    path('product-list', views.product_list, name='product_list'),
]
