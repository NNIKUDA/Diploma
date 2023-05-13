from django import template
from blog.models import Comment, News

register = template.Library()


@register.simple_tag()
def get_comment_count_by_news(news_id=None):
    return Comment.objects.filter(news_id=news_id).count()

