from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    # URL for viewing the entire car inventory
    path('', views.car_inventory, name='car_inventory'),
    
    # URL for viewing a specific car's details
    path('car/<int:car_id>/', views.car_details, name='car_details'),
]
