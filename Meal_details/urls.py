from django.urls import path
from .views import meal_details, meal_status, meal_phone


app_name = 'meal_details'
urlpatterns = [
    path('<int:meal_id>/', meal_details, name='meal_details'),
    path('<int:meal_id>/status/', meal_status, name='meal_status'),
    path('<int:meal_id>/phone/', meal_phone, name='meal_phone'),
]
from django.urls import path
from .views import meal_details, meal_phone

