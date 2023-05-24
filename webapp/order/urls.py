from django.urls import path
from .views import *

urlpatterns = [
    path('', order_view, name="order"),
]
