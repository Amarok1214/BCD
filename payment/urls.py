# payment/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('payment-form/', views.payment_form, name='payment_form'),
]
