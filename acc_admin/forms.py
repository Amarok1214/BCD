from django import forms
from inventory.models import Car, Branch
from booking.models import Reservation

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'make', 'model', 'year', 'license_plate', 'image', 'body_type',
            'engine_type', 'transmission', 'fuel_type', 'color', 'mileage',
            'seating_capacity', 'availability', 'rental_price_per_day',
            'current_location', 'condition', 'last_service_date'
        ]
        widgets = {
            'body_type': forms.Select(choices=Car.BODY_TYPES),
            'engine_type': forms.Select(choices=Car.ENGINE_TYPES),
            'transmission': forms.Select(choices=Car.TRANSMISSIONS),
            'fuel_type': forms.Select(choices=Car.FUEL_TYPES),
            'availability': forms.Select(choices=Car.AVAILABILITY_CHOICES),
            'condition': forms.Select(choices=Car.CONDITION_CHOICES),
        }
        

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'car', 'pickup_date', 'return_date', 'booking_status']
        widgets = {
            'pickup_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_status': forms.Select(),
        }

