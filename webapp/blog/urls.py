from django.urls import path
from .views import blog, single


urlpatterns = [
    path('', blog, name='blog'),
    path('<int:id>', single, name='single'),
    path('<str:tag>', blog, name='tag')
]

