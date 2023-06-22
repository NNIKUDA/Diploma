from django.contrib import admin
from .models import Product, Category, Discont


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Discont)
class ProductAdmin(admin.ModelAdmin):
    pass


