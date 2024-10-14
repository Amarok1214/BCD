from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=255)
    car_type = models.CharField(max_length=100)  # E.g., SUV, Compact, Luxury
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/')
    description = models.TextField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Temporarily make user optional
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Reservation for {self.car.name} from {self.start_date} to {self.end_date}"