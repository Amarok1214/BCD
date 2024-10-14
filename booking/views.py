from django.shortcuts import render, get_object_or_404
from .models import Car, Reservation
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import datetime

# Booking home page showing available cars
def booking_home(request):
    cars = Car.objects.all()
    return render(request, 'booking/booking.html', {'cars': cars})

# Detailed view of a car
def car_details(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'booking/car_details.html', {'car': car})

# Make a reservation for a selected car
def make_reservation(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == "POST":
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        total_price = calculate_price(car.price_per_day, start_date, end_date)
        
        # Save reservation without user authentication for now
        reservation = Reservation.objects.create(
            car=car,
            start_date=start_date,
            end_date=end_date,
            total_price=total_price
        )
        return HttpResponseRedirect(reverse('reservation_success'))
    return render(request, 'booking/make_reservation.html', {'car': car})

# Calculate the price of the reservation based on the selected dates
def calculate_price(price_per_day, start_date, end_date):
    delta = datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")
    return price_per_day * delta.days
