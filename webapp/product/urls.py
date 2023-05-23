from django.urls import path
from .views import *

urlpatterns = [
    path('list', produc_list, name='product_list')
]

