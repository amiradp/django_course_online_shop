from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import OrderForms
from cart.cart import Cart
from .models import OrderItem


@login_required
def order_create_view(request):
    order_form = OrderForms()
    cart = Cart(request)

    if len(cart) == 0:
        return redirect('ProductListView')

    if request.method == 'POST':
        order_form = OrderForms(request.POST, )

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price
                )

            cart.clear()

            request.first_name = order_obj.first_name
            request.last_name = order_obj.last_name
            request.user.save()

            request.session['order_id'] = order_obj.id
            return redirect('payment:payment_process')

    return render(request, 'orders/order_created.html', {
        'form': order_form,
    })
