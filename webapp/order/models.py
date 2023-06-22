from django.db import models

from product.models import Product
from user.models import User


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User)
    items = models.ManyToManyField(Product, through="OrderItem")


class OrderItem(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product)
    order = models.ForeignKey(Order)
