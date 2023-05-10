from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('<int:order_id>/', views.order_details, name='order_details'),
    path('<int:order_id>/shipping_deals/',
         views.shipping_deals, name='shipping_deals'),
]
