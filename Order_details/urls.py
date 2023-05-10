# import the views
from .views import OrderDetailsView, ShippingDealsView

urlpatterns = [
    # map the Order Details page to the OrderDetailsView
    path('order_details/<int:order_id>/',
         OrderDetailsView.as_view(), name='order_details'),
    # map the Shipping Deals page to the ShippingDealsView
    path('shipping_deals/', ShippingDealsView.as_view(), name='shipping_deals'),
]
