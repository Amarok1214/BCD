from django.db import models

class Branch(models.Model):
    # Information about rental branches
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.city}"


class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    license_plate = models.CharField(max_length=20, unique=True)

    BODY_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Hatchback', 'Hatchback'),
    ]
    body_type = models.CharField(max_length=20, choices=BODY_TYPES, default='Sedan')
    
    ENGINE_TYPES = [
        ('V6', 'V6'),
        ('V8', 'V8'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
        ('Diesel', 'Diesel'),
    ]
    engine_type = models.CharField(max_length=20, choices=ENGINE_TYPES)
    
    TRANSMISSIONS = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    ]
    transmission = models.CharField(max_length=10, choices=TRANSMISSIONS)
    
    FUEL_TYPES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPES)
    
    color = models.CharField(max_length=30)
    mileage = models.PositiveIntegerField()  # mileage in miles
    seating_capacity = models.PositiveIntegerField()
    
    # Car Status
    AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Rented', 'Rented'),
        ('Maintenance', 'Maintenance'),
    ]
    availability = models.CharField(max_length=15, choices=AVAILABILITY_CHOICES)
    rental_price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    current_location = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    
    CONDITION_CHOICES = [
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Needs Maintenance', 'Needs Maintenance'),
    ]
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    last_service_date = models.DateField()
    
    # Image of the Car
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}) - {self.license_plate}"


class Rental(models.Model):
    # Link to the rented car
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    # Customer Information (basic for now, can be extended)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)

    # Rental Details
    rental_start_date = models.DateField()
    rental_end_date = models.DateField()

    BOOKING_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    ]
    booking_status = models.CharField(max_length=15, choices=BOOKING_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Rental - {self.car} by {self.customer_name} ({self.booking_status})"
