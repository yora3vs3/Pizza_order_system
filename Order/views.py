from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Order


def order_details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'order_details.html', {'order': order})


def shipping_deals(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    # logic for shipping deals
    return render(request, 'shipping_deals.html', {'order': order})





@login_required
def current_order_status(request):
    order = Order.objects.filter(
        user=request.user, is_accepted=True, is_in_production=True).first()
    context = {'order': order}
    return render(request, 'current_order_status.html', context)


@login_required
def historical_orders(request):
    orders = Order.objects.filter(
        user=request.user, is_accepted=True, is_in_production=True).order_by('-created_at')
    context = {'orders': orders}
    return render(request, 'historical_orders.html', context)
