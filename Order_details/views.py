from django.shortcuts import render

# Create your views here.


def manager(request):
# render the Shipping Deals page with the shipping deals
  return render(request, 'shipping_deals.html', {'shipping_deals': shipping_deals})


@login_required
def current_order_details(request):
    order = Order.objects.filter(
        user=request.user, is_accepted=True, is_in_production=True).first()
    order_items = OrderItem.objects.filter(order=order)
    total_price = sum(item.price for item in order_items)
    context = {'order': order, 'order_items': order_items,
               'total_price': total_price}
    return render(request, 'current_order_details.html', context)
