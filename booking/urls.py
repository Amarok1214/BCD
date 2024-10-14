from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_home, name='booking'),
    path('car/<int:car_id>/', views.car_details, name='car_details'),
    path('reserve/<int:car_id>/', views.make_reservation, name='make_reservation'),
]