from django.db import models

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('gcash', 'GCash'),
        ('paypal', 'PayPal'),
        ('card', 'Card'),
    ]
    
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
    account_number = models.CharField(max_length=20)
    cardholder_name = models.CharField(max_length=100, blank=True, null=True)
    expiry_date = models.CharField(max_length=7, blank=True, null=True)  # MM/YY format
    cvc = models.CharField(max_length=4, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_payment_method_display()} - {self.account_number}"
