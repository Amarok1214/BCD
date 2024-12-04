from django.urls import path
from .views import payment_page, payment_success_page

app_name = 'payment'

urlpatterns = [
    path('payment/', payment_page, name='payment'),
    path('payment_success/', payment_success_page, name='payment_success_page'),
]