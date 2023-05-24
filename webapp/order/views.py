from django.shortcuts import render


def order_view(request):
    return render(request, "cart.html")


def checkout_view(request):
    return render(request, 'checkout.html')
