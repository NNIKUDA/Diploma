from django.shortcuts import render


def produc_list(request):
    return render(request, 'category-list.html')
