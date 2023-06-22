from django.db import models
from django.utils.timezone import now

from user.models import User


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True, primary_key=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.title


class Discont(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
    percent = models.SmallIntegerField()
    valid = models.BooleanField(default=False)
    valid_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'discont'


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    description = models.TextField()
    image = models.ImageField(upload_to='images/product/')
    details = models.JSONField(blank=True, null=True)
    reviews = models.ManyToManyField(User, related_name='reviews', through='Review')
    favorite = models.ManyToManyField(User, related_name='favorite')

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.title


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    written_date = models.DateField(default=now)
