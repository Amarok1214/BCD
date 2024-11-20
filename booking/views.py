from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from datetime import datetime
from inventory.models import Car
from booking.models import Reservation

# Booking home page showing available cars
def booking_home(request):
    car_id = request.GET.get('car_id')
    car_make = request.GET.get('car_make')
    car_model = request.GET.get('car_model')
    car_price = request.GET.get('car_price')

    context = {
        'car_id': car_id,
        'car_make': car_make,
        'car_model': car_model,
        'car_price': car_price,
    }
    return render(request, 'booking/booking.html', context)

def reservation_page(request):
    if request.method == "GET":
        # Get user data
        user = request.user
        full_name = f"{user.first_name} {user.last_name}"
        email = user.email

        # Get data from the query params sent from the booking form
        car_id = request.GET.get('car_id')
        car_make = request.GET.get('car_make')
        car_model = request.GET.get('car_model')
        car_price = float(request.GET.get('car_price', 0))  # Ensure car_price is treated as a float
        pickup_date = request.GET.get('pickup_date')
        return_date = request.GET.get('return_date')

        # Calculate total rental days and total price
        if pickup_date and return_date:
            # Parse the dates
            pickup_date_obj = datetime.strptime(pickup_date, '%Y-%m-%d')
            return_date_obj = datetime.strptime(return_date, '%Y-%m-%d')

            # Calculate rental duration in days
            total_days = (return_date_obj - pickup_date_obj).days
            total_days = max(total_days, 0)  # Ensure no negative days

            # Calculate total price
            total_price = total_days * car_price
        else:
            total_days = 0
            total_price = 0

        formatted_car_price = f"{car_price:.2f}"
        formatted_total_price = f"{total_price:.2f}"

        # Pass all data to the reservation template
        context = {
            "car_id": car_id,
            "car_make": car_make,
            "car_model": car_model,
            "car_price": formatted_car_price,
            "pickup_date": pickup_date,
            "return_date": return_date,
            "full_name": full_name,
            "email": email,
            "total_days": total_days,
            "total_price": formatted_total_price,
        }
        return render(request, 'booking/reservation.html', context)
    else:
        return redirect('booking:booking_page')

def confirm_reservation_page(request):
    if request.method == "POST":

        user = request.user
        full_name = f"{user.first_name} {user.last_name}"
        email = user.email

        # Get form data
        car_id = request.POST.get('car_id')
        pickup_date = request.POST.get('pickup_date')
        return_date = request.POST.get('return_date')

        # Fetch the car object and ensure it's available
        car = get_object_or_404(Car, id=car_id, availability="Available")

        # Create a reservation linked to the authenticated user
        reservation = Reservation.objects.create(
            car=car,
            user=request.user,
            pickup_date=pickup_date,
            return_date=return_date,
            booking_status="Pending"
        )

        # Update the car's availability status
        car.availability = "Rented"
        car.save()

        context = {
            "pickup_date": pickup_date,
            "return_date": return_date,
            "full_name": full_name,
            "email": email,
        }

        # Redirect or render confirmation page
        return render(request, 'booking/confirm_reservation.html', context)
    else:
        return redirect('booking:reservation_page')
    
def user_reservations(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('-pickup_date')
    return render(request, 'booking/user_reservations.html', {'reservations': reservations})

# def finalize_reservation(request):
#     if request.method == 'POST':
#         # Save the reservation to the database
#         Reservation.objects.create(
#             car_id=request.POST.get('car_id'),
#             car_make=request.POST.get('car_make'),
#             car_model=request.POST.get('car_model'),
#             car_price=request.POST.get('car_price'),
#             full_name=request.POST.get('full_name'),
#             email=request.POST.get('email'),
#             phone=request.POST.get('phone'),
#             pickup_date=request.POST.get('pickup_date'),
#             return_date=request.POST.get('return_date'),
#         )

#         # Redirect to confirmation page with a success message
#         messages.success(request, 'Your reservation has been successfully confirmed!')
#         return redirect('booking:reservation_confirmation')

#     return redirect('booking:booking_page')
