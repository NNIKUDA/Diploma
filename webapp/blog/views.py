from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsTag, News, Comment
from django.utils import timezone
from product.views import mixin_context


def blog(request, tag=None):
    if tag:
        news = News.objects.filter(date__lte=timezone.now(), tag=tag).order_by('-date')
    else:
        news = News.objects.filter(date__lte=timezone.now()).order_by('-date')
    paginator = Paginator(news, 3)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'comments': Comment.objects.all(),
        'tags': sorted(((tag, News.objects.filter(date__lte=timezone.now(), tag=tag.title).count()) for tag in
                        NewsTag.objects.all()), key=lambda x: x[1], reverse=True)
    }
    context.update(mixin_context())
    return render(request, 'blog.html', context=context)


def single(request, id):
    article = News.objects.get(id=id)
    context = {
        'page_obj': News.objects.filter(date__lte=timezone.now()).order_by('-date'),
        'tags': sorted(((tag, News.objects.filter(date__lte=timezone.now(), tag=tag.title).count()) for tag in
                        NewsTag.objects.all()), key=lambda x: x[1], reverse=True),
        'article': article,
    }
    context.update(mixin_context())
    return render(request, 'single.html', context=context)
