from django.shortcuts import render


def product_list_view(request):
    return render(request, 'category-list.html')


def product_view(request):
    return render(request, 'product.html')
