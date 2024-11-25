from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.booking_home, name='booking_home'),
    path('reservation/', views.reservation_page, name='reservation_page'),
    path('confirm-reservation-page/', views.confirm_reservation_page, name='confirm_reservation_page'),
]