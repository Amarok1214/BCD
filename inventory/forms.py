from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "make", "model", "year", "license_plate", "image", 
            "body_type", "engine_type", "transmission", 
            "fuel_type", "color", "mileage", "seating_capacity", 
            "availability", "rental_price_per_day", "current_location", 
            "condition", "last_service_date"
        ]
        widgets = {
            "last_service_date": forms.DateInput(attrs={"type": "date"}),
        }
