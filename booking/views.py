from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Booking home page showing available cars
def booking_home(request):
    return render(request, 'booking/booking.html')

# Calculate the price of the reservation based on the selected dates
def calculate_price(price_per_day, start_date, end_date):
    delta = datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")
    return price_per_day * delta.days

@login_required
def booking_view(request):
    return render(request, 'booking/booking.html')