from django.urls import path
from .views import *

urlpatterns = [
    path("list/<str:category>", product_list_view, name="product_category"),
    path("product/<int:id>", product_view, name="product"),
]

