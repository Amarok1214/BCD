from django.shortcuts import render, get_object_or_404
from .models import Car
from django.contrib.auth.decorators import login_required

@login_required
def car_inventory(request):
    # Fetch all cars from the database
    cars = Car.objects.filter(availability="Available")
    context = {'cars': cars}
    return render(request, 'inventory/car_inventory.html', context)

@login_required
def car_details(request, car_id):
    cars = get_object_or_404(Car, id=car_id)
    return render(request, 'inventory/car_details.html', {'car': cars})