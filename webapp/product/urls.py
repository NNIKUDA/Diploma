from django.urls import path
from .views import *

urlpatterns = [
    path('list', product_list_view, name='product_list'),
    path('product', product_view, name='product'),
]

