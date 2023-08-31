from django.shortcuts import render


def order_create_view(request):
    return render(request, 'orders/order_created.html')
