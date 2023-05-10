from django.urls import path
from .views import history_order, search_order, order_dates, specific_order


app_name = 'pizza_orders'
urlpatterns = [
    path('history_order/', history_order, name='history_order'),
    path('search_order/', search_order, name='search_order'),
    path('order_dates/', order_dates, name='order_dates'),
    path('specific_order/<str:search_date>/',
         specific_order, name='specific_order'),
]
