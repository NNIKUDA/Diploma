from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Product, Category


def mixin_context():
    context = {
        "category_list": Category.objects.all(),
    }
    return context


def product_list_view(request, category):
    if category == "None":
        products = Product.objects.all()
    elif category:
        products = Product.objects.filter(category=category)

    paginator = Paginator(products, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    context.update(mixin_context())
    return render(request, "category-list.html", context=context)


def product_view(request, id):
    product = Product.objects.get(id=id)
    context = {
        "product": product,
        "reviews": Product.reviews.through.objects.filter(product=id)
    }
    context.update(mixin_context())
    return render(request, "product.html", context=context)




