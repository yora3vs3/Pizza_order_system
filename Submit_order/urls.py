from django.urls import path
from .views import product_menu, shopping_cart_order, confirm_order, cancel_order


app_name = 'product_app'
urlpatterns = [
    path('product_menu/', product_menu, name='product_menu'),
    path('shopping_cart_order/', shopping_cart_order, name='shopping_cart_order'),
    path('submit_order/', confirm_order, name='submit_order'),
    path('cancel_order/', cancel_order, name='cancel_order'),
]
