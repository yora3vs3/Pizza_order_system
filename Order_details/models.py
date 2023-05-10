# import necessary modules
from django.shortcuts import render
from django.views import View

# define a view for the Order Details page


class OrderDetailsView(View):
    def get(self, request, order_id):
        # retrieve the order details from the database based on the order_id
        order = Order.objects.get(id=order_id)

        # render the Order Details page with the order details
        return render(request, 'order_details.html', {'order': order})
