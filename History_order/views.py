from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order


@login_required
def history_order(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    context = {'orders': orders}
    return render(request, 'history_order.html', context)


@login_required
def search_order(request):
    if request.method == 'POST':
        search_date = request.POST.get('search_date')
        orders = Order.objects.filter(user=request.user, created_at__date=search_date)
        context = {'orders': orders, 'search_date': search_date}
        return render(request, 'search_order.html', context)
    return render(request, 'search_order.html')


@login_required
def order_dates(request):
    order_dates = Order.objects.filter(user=request.user).dates('created_at', 'day', order='DESC')
    context = {'order_dates': order_dates}
    return render(request, 'order_dates.html', context)


@login_required
def specific_order(request, search_date):
    orders = Order.objects.filter(user=request.user, created_at__date=search_date)
    context = {'orders': orders, 'search_date': search_date}
    return render(request, 'specific_order.html', context)
