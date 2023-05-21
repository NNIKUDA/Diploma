from django.urls import path
from .views import *

urlpatterns = [
    path('index', index, name='home'),
    path('sing_up', sing_up, name='sing_up'),
    path('sing_in', sing_in, name='sing_in'),
    path('login', login_view, name='login'),
    path('logout', sing_out, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
    path('dashboard', dashboard, name='register'),

]

