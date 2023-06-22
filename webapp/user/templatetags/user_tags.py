from django import template
from user.models import User

register = template.Library()


@register.simple_tag()
def get_wishlist_count(user_id=None):
    return User.favorite.through.objects.filter(user_id=user_id).count()

