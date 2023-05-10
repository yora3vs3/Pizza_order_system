from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Meal, Order


@login_required
def meal_details(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    order = Order.objects.filter(user=request.user, meal=meal).first()
    context = {'meal': meal, 'order': order}
    return render(request, 'meal_details.html', context)


@login_required
def meal_status(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    order = Order.objects.filter(user=request.user, meal=meal).first()
    if order and order.is_accepted and order.is_delivered:
        status = 'Delivered'
    elif order and order.is_accepted:
        status = 'Being Prepared'
    elif order:
        status = 'Order Accepted'
    else:
        status = 'Not Ordered'
    context = {'meal': meal, 'order': order, 'status': status}
    return render(request, 'meal_status.html', context)

@login_required
def meal_phone(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    phone_number = meal.phone_number
    context = {'meal': meal, 'phone_number': phone_number}
    return render(request, 'meal_phone.html', context)