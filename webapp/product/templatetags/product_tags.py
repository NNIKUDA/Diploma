from django import template
from product.models import Product, Review

register = template.Library()


@register.simple_tag()
def get_product_review_count(product_id=None):
    return Review.objects.filter(product_id=product_id).count()


@register.simple_tag()
def get_rating(rating):
    return rating*20


@register.simple_tag()
def get_product_avg_review(product_id=None):
    review_count = Review.objects.filter(product_id=product_id).count()
    if review_count>0:
        return sum([review.rating*20 for review in Review.objects.filter(product_id=product_id)])/review_count
    else:
        return 0



