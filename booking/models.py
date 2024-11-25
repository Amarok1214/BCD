from django.db import models
from django.contrib.auth.models import User
from inventory.models import Car

class Reservation(models.Model):
    # Link to the rented car
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="reservations")
    
    # Link to the user account (making it non-nullable)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations", null=False)

    # Rental details
    pickup_date = models.DateField()
    return_date = models.DateField()
    
    # Booking status
    BOOKING_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    ]
    booking_status = models.CharField(max_length=15, choices=BOOKING_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Reservation for {self.car} by {self.user.get_full_name()} ({self.booking_status})"