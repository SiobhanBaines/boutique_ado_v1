from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51It6A8HXaEBIcMEEvxdqfecnZpIkIA4Zkgkv4KUQtfCPH3dUwUC87f8NYvWaVnQEOJc4g1riYkLVDCoA5kDcggXv00VIN5ffWh',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)
