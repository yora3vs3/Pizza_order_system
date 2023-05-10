from django.shortcuts import render, redirect
from .models import Product, Order, OrderItem


def product_menu(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_menu.html', context)


def shopping_cart_order(request):
    if request.method == 'POST':
        # Handle the order confirmation logic here
        return redirect('submit_order')
    else:
        # Retrieve the current order for the user
        order = Order.objects.get(id=request.session.get('order_id'))
        order_items = OrderItem.objects.filter(order=order)
        context = {'order_items': order_items}
        return render(request, 'shopping_cart_order.html', context)


def confirm_order(request):
    if request.method == 'POST':
        # Handle the order submission logic here
        return redirect('product_menu')
    else:
        return render(request, 'confirm_order.html')


def cancel_order(request):
    # Cancel the current order and redirect to the product menu
    return redirect('product_menu')
