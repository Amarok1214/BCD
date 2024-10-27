from django.shortcuts import render, get_object_or_404
from .models import Car  # Assuming you have a Car model

def car_inventory(request):
    # Fetch all cars from the database
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'inventory/car_inventory.html', context)

def car_details(request, car_id):
    # Fetch a single car by ID
    car = get_object_or_404(Car, id=car_id)
    context = {'car': car}
    return render(request, 'inventory/car_details.html', context)